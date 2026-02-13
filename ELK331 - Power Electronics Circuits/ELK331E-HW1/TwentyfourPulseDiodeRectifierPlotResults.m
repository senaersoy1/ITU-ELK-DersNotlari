% Code to plot simulation results from TwentyfourPulseDiodeRectifier
%% Plot Description:
%
% These plots show the grid voltages, currents, and the dc-link voltage.

% Copyright 2024 The MathWorks, Inc.

% Generate simulation results if they don't exist
if ~exist('simlog_TwentyfourPulseDiodeRectifier', 'var')
    sim('TwentyfourPulseDiodeRectifier')
end

% Reuse figure if it exists, else create new figure
if ~exist('h1_TwentyfourPulseDiodeRectifier', 'var') || ...
        ~isgraphics(h1_TwentyfourPulseDiodeRectifier, 'figure')
    h1_TwentyfourPulseDiodeRectifier = figure('Name', 'TwentyfourPulseDiodeRectifier');
end
figure(h1_TwentyfourPulseDiodeRectifier)
clf(h1_TwentyfourPulseDiodeRectifier)

plotData(simlog_TwentyfourPulseDiodeRectifier)

% Plot grid voltages, currents, and the dc-link voltage
function plotData(simlog)

% Get simulation results
t = simlog.Primary_vi.Sending_vi.V_output.series.time;
vabc= simlog.Primary_vi.Sending_vi.V_output.series.values('V');
iabc= simlog.Primary_vi.Sending_vi.I_output.series.values('A');
vdc = simlog.Sensing_Vdc.Voltage_Sensor.V.series.values('V');

% Plot results
handles(1) = subplot(3, 1, 1);
plot(t, vabc, 'LineWidth', 1)
grid on
title('Grid Voltages')
ylabel('Voltage (V)')
handles(2) = subplot(3, 1, 2);
plot(t, iabc, 'LineWidth', 1)
grid on
title('Grid Currents')
ylabel('Current (A)')
handles(3) = subplot(3, 1, 3);
plot(t, vdc, 'LineWidth', 1)
grid on
title('DC-link Voltage')
ylabel('Voltage (V)')
xlabel('Time (s)')

linkaxes(handles, 'x')
end