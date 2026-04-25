% Constants
mu_0 = 4 * pi * 1e-7; % Permeability of free space (H/m)
mu_r = 1000; % Relative permeability of the core
A_outer = 1e-4; % Cross-sectional area of the outer legs (m^2)
A_middle = 2e-4; % Cross-sectional area of the middle leg (m^2)
F = 300; % Magnetomotive force (Ampere-Turns)

% Generate 100 datapoints for x in meters
x_m = linspace(0, 0.001, 100); % x from 0 to 0.001 m (SI units)

% Preallocate arrays
B_left = zeros(size(x_m));
B_middle = zeros(size(x_m));

% Loop through all x values
for i = 1:length(x_m)
    % Air gap lengths in meters
    g_left = x_m(i); % Left and right gap lengths in meters
    g_middle = x_m(i) + 0.001; % Middle gap length in meters

    % Reluctances
    l_left_core = 0.1 - x_m(i); % Left core length in meters
    R_left_core = l_left_core / (mu_0 * mu_r * A_outer); % Core reluctance
    R_left_gap = g_left / (mu_0 * A_outer); % Left gap reluctance
    R_left = R_left_core + R_left_gap;

    l_middle_core = 0.04 - g_middle; % Middle core length in meters
    R_middle_core = l_middle_core / (mu_0 * mu_r * A_middle); % Core reluctance
    R_middle_gap = g_middle / (mu_0 * A_middle); % Middle gap reluctance
    R_middle = R_middle_core + R_middle_gap;

    % Total reluctance
    R_left_right = (1 / R_left + 1 / R_left)^-1; % Left and right branches in parallel
    R_total = R_middle + R_left_right; % Total reluctance including middle

    % Flux calculations
    Phi_middle = F / R_total; % Flux in the middle branch
    Phi_left = Phi_middle * 0.5; % Flux in the left branch

    % Flux densities
    B_left(i) = Phi_left / A_outer; % Flux density in the left air gap
    B_middle(i) = Phi_middle / A_middle; % Flux density in the middle air gap
end

% Plot results with adjustments for visibility
figure;
% Plot B_left with a slight offset
plot(x_m, B_left + 0.005, '--r', 'LineWidth', 1.5, 'DisplayName', 'Left Air Gap (Offset)');
hold on;
% Plot B_middle without an offset
plot(x_m, B_middle, '-b', 'LineWidth', 1.5, 'DisplayName', 'Middle Air Gap');
xlabel('Air Gap Length (x, m)');
ylabel('Flux Density (B, T)');
title('Flux Density in Air Gaps vs Air Gap Length');
legend('Location', 'best');
grid on;
hold off;

% Display example results
disp('Example Results (SI Units):');
disp(table(x_m', B_left', B_middle', ...
    'VariableNames', {'x_m (m)', 'B_Left_Air_Gap (T)', 'B_Middle_Air_Gap (T)'}));
