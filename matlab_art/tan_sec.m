g = @(x)((sec(x))^2);
f = @(x)(tan(x)*sec(x));


for k=0:.1:100
    t= linspace(0,10*pi,1000);
    t = t*k;
    tan_t = g(t);
    sec_t = arrayfun(f,t);
    plot(t,sec_t);
    hold on;
    plot(t,tan_t);
    hold on;
end

k = 1;
t= linspace(0,10*pi,1000);
t = t*k;
dtan_t = arrayfun(g,t);
dsec_t = arrayfun(f,t);
plot(t,dtan_t);
hold on;
plot(t,dsec_t);
hold on;