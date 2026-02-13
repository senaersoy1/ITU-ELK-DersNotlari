
% Access the data from the timeseries objects
Va = out.Va.Data;  % Phase A voltage or line-to-line voltage 
Vb = out.Vb.Data;  % Phase B voltage or line-to-line voltage
Vc = out.Vc.Data;  % Phase C voltage or line-to-line voltage
Io = out.Io.Data;  % Output current
Vo = out.Vo.Data;  % Output voltage

% Define the time step based on your simulation 
time_step = 1e-5; 

% Create the time vector 
time_Vline = (0:length(Va)-1) * time_step;  % Time data for line-to-line voltage (or phase voltage)

% Plot 1: Line-to-Line Voltage (Phase A)
figure;
plot(time_Vline, Va, 'LineWidth', 1.5); 
xlabel('Time (s)');
ylabel('Line-to-Line Voltage (V)');
title('Line-to-Line Voltage (Phase A)');
grid on;
print('Line_to_Line_Voltage_A', '-dpng', '-r300');

% Plot 2: Output Current
figure;
plot(time_Vline, Io, 'LineWidth', 1.5);  % Io as the output current
xlabel('Time (s)');
ylabel('Output Current (A)');
title('Output Current');
grid on;
print('Output_Current', '-dpng', '-r300');

% Plot 3: Output Voltage
figure;
plot(time_Vline, Vo, 'LineWidth', 1.5);  % Vo as the output voltage
xlabel('Time (s)');
ylabel('Output Voltage (V)');
title('Output Voltage');
grid on;
print('Output_Voltage', '-dpng', '-r300');

Fs = 1 / time_step;  % Sampling frequency
N = length(Va);      % Length of the signal
f = (0:N-1) * (Fs / N);  % Frequency vector

% Compute the FFT for the voltage (Va), current (Io), or voltage (Vo)
Y_Va = fft(Va);
Y_Io = fft(Io);
Y_Vo = fft(Vo);

% Compute the magnitude of the FFT (only the positive frequencies)
magnitude_Va = abs(Y_Va(1:floor(N/2)));
magnitude_Io = abs(Y_Io(1:floor(N/2)));
magnitude_Vo = abs(Y_Vo(1:floor(N/2)));

% Fundamental frequency is the first peak, harmonics are subsequent peaks
V1_Va = magnitude_Va(2);  % Fundamental frequency component of Va
V1_Io = magnitude_Io(2);  % Fundamental frequency component of Io
V1_Vo = magnitude_Vo(2);  % Fundamental frequency component of Vo

% Calculate the harmonic components (sum of squares of all harmonics)
harmonics_Va = sum(magnitude_Va(3:end).^2);  % Harmonics for Va 
harmonics_Io = sum(magnitude_Io(3:end).^2);  % Harmonics for Io
harmonics_Vo = sum(magnitude_Vo(3:end).^2);  % Harmonics for Vo

% Calculate the THD for each signal
THD_Va = sqrt(harmonics_Va) / V1_Va;
THD_Io = sqrt(harmonics_Io) / V1_Io;
THD_Vo = sqrt(harmonics_Vo) / V1_Vo;

disp(['THD for Va: ', num2str(THD_Va)]);
disp(['THD for Io: ', num2str(THD_Io)]);
disp(['THD for Vo: ', num2str(THD_Vo)]);
