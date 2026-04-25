% Constants
mu_0 = 4 * pi * 1e-7; % Permeability of free space (H/m)
mu_r = 15000; % Relative permeability of the core (High-Quality Material)
A_outer = 1e-4; % Cross-sectional area of the outer legs (m^2)
A_middle = 2e-4; % Cross-sectional area of the middle leg (m^2)
F = 300; % Magnetomotive force (Ampere-Turns)

% Generate 100 datapoints for x in meters
x_m = linspace(0, 0.001, 100); % x from 0 to 0.001 m (SI units)

% Preallocate arrays
L = zeros(size(x_m)); % Inductance
B_left = zeros(size(x_m)); % Flux density in left air gap
B_middle = zeros(size(x_m)); % Flux density in middle air gap

% Loop through all x values
for i = 1:length(x_m)
    % Air gap lengths in meters
    g_left = x_m(i); % Left and right gap lengths in meters
    g_middle = x_m(i) + 0.001; % Middle gap length in meters

    % Reluctances
    l_left_core = 0.1 - x_m(i); % Left core length in meters
    R_left_core = l_left_core / (mu_0 * mu_r * A_outer); % Core reluctance
    R_left_gap = g_left / (mu_0 * A_outer); % Left gap reluctance
    R_left = R_left_core + R_left_gap; % Total reluctance of left branch

    l_middle_core = 0.04 - g_middle; % Middle core length in meters
    R_middle_core = l_middle_core / (mu_0 * mu_r * A_middle); % Core reluctance
    R_middle_gap = g_middle / (mu_0 * A_middle); % Middle gap reluctance
    R_middle = R_middle_core + R_middle_gap; % Total reluctance of middle branch

    % Parallel reluctance of left and right branches
    R_left_right = R_left / 2;

    % Total reluctance of the circuit
    R_total = R_middle + R_left_right;

    % Inductance
    L(i) = 300^2 / R_total;

    % Flux calculations
    Phi_middle = F / R_total; % Flux in the middle branch
    Phi_left = Phi_middle / 2; % Flux in the left branch

    % Flux densities
    B_left(i) = Phi_left / A_outer; % Flux density in the left air gap
    B_middle(i) = Phi_middle / A_middle; % Flux density in the middle air gap
end

% Plot Inductance
figure;
plot(x_m, L, '-k', 'LineWidth', 1.5);
xlabel('Air Gap Length (x, m)');
ylabel('Inductance (L, H)');
title('Inductance vs Air Gap Length');
grid on;

% Plot Flux Densities with Offset
figure;
plot(x_m, B_middle, '-b', 'LineWidth', 1.5, 'DisplayName', 'Middle Air Gap'); % Middle air gap
hold on;
plot(x_m, B_left + 0.005, '--r', 'LineWidth', 1.5, 'DisplayName', 'Left Air Gap (Offset)'); % Left air gap with offset
xlabel('Air Gap Length (x, m)');
ylabel('Flux Density (B, T)');
title('Flux Density in Air Gaps vs Air Gap Length');
legend('Location', 'best');
grid on;
hold off;
