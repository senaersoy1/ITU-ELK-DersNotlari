%% ELK342E - Hassas Frekans ve THD Analizi
clear; clc; close all;

% 1. Veriyi Oku (Önceki sağlam yöntem)
fid = fopen('Kopya CH1_Current.CSV', 'r');
rawContent = fread(fid, '*char')';
fclose(fid);
cleanContent = strrep(rawContent, ',', '.');
dataCells = textscan(cleanContent, '%f%f', 'Delimiter', ';', 'CollectOutput', true);
data = dataCells{1};

voltage = data(:, 1);
time = data(:, 2);
voltage = voltage - mean(voltage); % DC ofset temizliği

% 2. Frekans Çözünürlüğünü Artırma (Zero Padding)
L = length(voltage);
Fs = 1 / mean(diff(time));
N_fft = 2^nextpow2(L * 10); % Veriyi 10 katı kadar sıfırla besle (Hassas analiz)

% 3. FFT ve THD Hesabı
Y = fft(voltage, N_fft);
P2 = abs(Y/L);
P1 = P2(1:floor(N_fft/2)+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(floor(N_fft/2)))/N_fft;

% Temel frekans bulma
[V1_amp, idx] = max(P1);
f_fund = f(idx); 

% THD Hesabı
V_rms_total = sqrt(mean(voltage.^2));
V1_rms = V1_amp / sqrt(2);
thd_val = sqrt(V_rms_total^2 - V1_rms^2) / V1_rms;

% 4. Sonuçları Yazdır
fprintf('Gözlemlenen Frekans: %.2f Hz\n', f_fund);
fprintf('THD Oranı: %%%.2f\n', thd_val * 100);

% 5. Görselleştirme
figure;
stem(f, P1, 'Marker', 'none', 'LineWidth', 1.2);
xlim([0 250]); % 50Hz ve harmonikleri görmek için
title(['Hassas Spektrum Analizi - Temel Frekans: ', num2str(f_fund, '%.2f'), ' Hz']);
xlabel('Frekans (Hz)'); ylabel('Genlik (V)'); grid on;