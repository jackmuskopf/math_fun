% waveform params
T0 = 10;
n = 5;
w0 = 4;
T = 500;

% signal sample params
ta = 0;
te = 100;
sr = .1;
ts = [ta:sr:te];

% freq params
fs = -1*(1/2*sr);
fe = -1*fs;
fsr = (fe-fs)/length(ts);
freqs = [fs:fsr:fe-fsr];

% signal fns
v = @(t)((abs(t-n*T0)<(T0/4))*10*cos(w0*t));    % v(t)
vT = @(t)((abs(t)<(T/2))*v(t));                 % vT(t)
P = @(w)((abs(w)^2)/T);                         % Pw(f)

% calc and plot
vs = arrayfun(vT,ts);
Ft = fft(vs);
Pw = arrayfun(P, Ft);
plot(freqs,Pw); % PSD in blue
%hold on;
%plot(ts,vs);    % v(t) in red

