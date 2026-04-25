mu_0 = 4 * pi * 1e-7;
mu_r = 1000;
A_outer = 1e-4;
A_middle = 2e-4;
N = 300;

% Range of x
x = linspace(0, 0.001, 100); % 100 points between 0 and 0.001 m

% Reluctances
R_left_core = (0.1 - x) ./ (mu_0 * mu_r * A_outer);
R_right_core = R_left_core; % Symmetric
R_left_gap = x ./ (mu_0 * A_outer);
R_right_gap = R_left_gap;
R_middle_core = (0.04 - (x + 0.001)) ./ (mu_0 * mu_r * A_middle);
R_middle_gap = (x + 0.001) ./ (mu_0 * A_middle);

% Total reluctances
R_left = R_left_core + R_left_gap;
R_right = R_right_core + R_right_gap;
R_parallel = 1 ./ (1 ./ R_left + 1 ./ R_right);
R_middle = R_middle_core + R_middle_gap;
R_total = R_parallel + R_middle;

% Inductance
L = N^2 ./ R_total;

% Plot
plot(x, L);
xlabel('Air Gap Length (x, m)');
ylabel('Inductance (L, H)');
title('Inductance vs Air Gap Length');
grid on;