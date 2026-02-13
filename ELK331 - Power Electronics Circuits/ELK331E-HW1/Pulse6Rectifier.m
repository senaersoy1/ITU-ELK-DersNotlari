% Assuming the workspace variables Vline_to_line, Iout, and Vout are saved as arrays

% Define the time step based on your simulation (adjust this value if needed)
time_step = 1e-5;  % Set to your simulation step size (check simulation settings)

% Generate the time vector assuming the time step is consistent
time_Vline = (0:length(Vline_to_line)-1) * time_step;  % Time data for line-to-line voltage
Vline = Vline_to_line;  % Signal data for line-to-line voltage

time_Iout = (0:length(Iout)-1) * time_step;            % Time data for output current
current = Iout;                                        % Output current data

time_Vout = (0:length(Vout)-1) * time_step;            % Time data for output voltage
voltage = Vout;                                       % Output voltage data

% Plot 1: Line-to-Line Voltage
figure;
plot(time_Vline, Vline, 'LineWidth', 1.5);
xlabel('Time (s)');
ylabel('Line-to-Line Voltage (V)');
title('Line-to-Line Voltage');
grid on;
% Save plot with 300 dpi resolution
print('Line_to_Line_Voltage', '-dpng', '-r300');

% Plot 2: Output Current
figure;
plot(time_Iout, current, 'LineWidth', 1.5);
xlabel('Time (s)');
ylabel('Output Current (A)');
title('Output Current');
grid on;
% Save plot with 300 dpi resolution
print('Output_Current', '-dpng', '-r300');

% Plot 3: Output Voltage
figure;
plot(time_Vout, voltage, 'LineWidth', 1.5);
xlabel('Time (s)');
ylabel('Output Voltage (V)');
title('Output Voltage');
grid on;
% Save plot with 300 dpi resolution
print('Output_Voltage', '-dpng', '-r300');
