% Motor Parameters from your Table 1
Rs = 42.62; Rr = 42.62; 
Lls = 0.220; Llr = 0.220; Lm = 1.66;
J = 0.0013; F = 0.001; p = 2;

% Frequencies to simulate
freq_list = [10, 30, 50, 70];
t_end = 0.6; % Total simulation time
fs = 10000; % Sampling freq
t = 0:1/fs:t_end;

V_rated_ph_rms = 400 / sqrt(3);

for f = freq_list
    % 1. V/f Calculation Logic
    V_ph_rms = min((f / 50) * V_rated_ph_rms, V_rated_ph_rms);
    V_peak = V_ph_rms * sqrt(2);
    
    % 2. Dynamic Simulation Initialization
    v_a = V_peak * sin(2 * pi * f * t);
    i_a = zeros(size(t));
    w_r = 0; % Start from zero speed
    dt = 1/fs;
    
    % 3. Time-Step Integration
    for k = 2:length(t)
        w_sync = (2 * pi * f) / p;
        % Slip calculation (protected against division by zero)
        slip = max((w_sync - w_r) / (w_sync + 0.01), 0.001);
        
        % Instantaneous Impedance
        X_tot = 2 * pi * f * (Lls + Llr);
        Z_mag = sqrt((Rs + Rr/slip)^2 + X_tot^2);
        phase_lag = atan(X_tot / (Rs + Rr/slip));
        
        % Current Calculation
        i_a(k) = (V_peak / Z_mag) * sin(2 * pi * f * t(k) - phase_lag);
        
        % Speed Update (Internal)
        Te = (3 * (V_ph_rms^2) * (Rr/slip)) / (w_sync * ((Rs + Rr/slip)^2 + X_tot^2));
        dw = (Te - F*w_r) / J;
        w_r = w_r + dw * dt;
    end
    
    % 4. Create a New Figure for each frequency
    figure('Name', ['Results for ', num2str(f), ' Hz'], 'Color', 'w');
    
    subplot(2,1,1);
    plot(t, v_a, 'b');
    title(['Motor Voltage (Phase A) at ', num2str(f), ' Hz']);
    ylabel('Voltage (V)'); grid on;
    
    subplot(2,1,2);
    plot(t, i_a, 'r');
    title(['Motor Current (Phase A) at ', num2str(f), ' Hz']);
    xlabel('Time (s)'); ylabel('Current (A)'); grid on;
end