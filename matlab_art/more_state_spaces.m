%% reggie's knot
A = @(t)[-sin(3*t) cos(2*t); -cos(31*t) -sin(3*t)];
F = @(t,x)[(A(t)*x)];
F_invariant = @(t,x)[(A(100)*x)];
F_invariant2 = @(t,x)[(A(.413)*x)];

for l=1:100
    y0 = [1; 1];
    tspan = (l-1)*100:.01:l*100;
    [t,y] = ode45(F,tspan,y0);
    % [ti,yi] = ode45(F_invariant,tspan,y0);
    % [tr,yr] = ode45(F_invariant2,tspan,y0);

    plot(y(:,1),y(:,2),'p'); hold on;
end

%% slinky loop
A = @(t)[-sin(3*t) cos(3*t); -cos(3*t) -sin(3*t)];
F = @(t,x)[(A(t)*x)];
F_invariant = @(t,x)[(A(100)*x)];
F_invariant2 = @(t,x)[(A(.413)*x)];

for l=1:100
    y0 = [1; 1];
    tspan = (l-1)*100:.01:l*100;
    [t,y] = ode45(F,tspan,y0);
    % [ti,yi] = ode45(F_invariant,tspan,y0);
    % [tr,yr] = ode45(F_invariant2,tspan,y0);

    plot(y(:,1),y(:,2)); hold on;
    disp(l);
end

%% pretty ball
A = @(t)[-sin(3*t) cos(3*t); -cos(3*t) -sin(3*t)]*sin(t);
F = @(t,x)[(A(t)*x)];
F_invariant = @(t,x)[(A(100)*x)];
F_invariant2 = @(t,x)[(A(.413)*x)];

for l=1:100
    y0 = [1; 1];
    tspan = (l-1)*100:.01:l*100;
    [t,y] = ode45(F,tspan,y0);
    % [ti,yi] = ode45(F_invariant,tspan,y0);
    % [tr,yr] = ode45(F_invariant2,tspan,y0);

    plot(y(:,1),y(:,2)); hold on;
    disp(l);
end
%% caterpillar
A = @(t)[-sin(3*t) cos(3*t); -cos(3*t) -sin(3*t)]*sin(50*t);
F = @(t,x)[(A(t)*x)];
F_invariant = @(t,x)[(A(100)*x)];
F_invariant2 = @(t,x)[(A(.413)*x)];

for l=1:100
    y0 = [1; 1];
    tspan = (l-1)*100:.01:l*100;
    [t,y] = ode45(F,tspan,y0);
    % [ti,yi] = ode45(F_invariant,tspan,y0);
    % [tr,yr] = ode45(F_invariant2,tspan,y0);

    plot(y(:,1),y(:,2)); hold on;
    disp(l);
end

%% dopestar
A = @(t)[-sin(3*t) cos(3*t); -cos(3*t) -sin(3*t)]*sin(5*t);
F = @(t,x)[(A(t)*x)];
F_invariant = @(t,x)[(A(100)*x)];
F_invariant2 = @(t,x)[(A(.413)*x)];

for l=1:1000
    y0 = [1; 1];
    tspan = (l-1)*100:.01:l*100;
    [t,y] = ode45(F,tspan,y0);
    % [ti,yi] = ode45(F_invariant,tspan,y0);
    % [tr,yr] = ode45(F_invariant2,tspan,y0);

    plot(y(:,1),y(:,2),'p'); hold on;
    disp(l);
end