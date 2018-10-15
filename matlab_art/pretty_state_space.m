%% eye space %%
%A = @(t)[-sin(19*t) cos(23*t); -cos(17*t) -sin(31*t)];
p = -.004;
tk = 0;
A = @(t)([sin(tk+sin(5*t)) cos(tk); -cos(tk) -sin(tk)]);

F = @(t,x)[(A(t)*x)];
F_invariant = @(t,x)[(A(100)*x)];
F_invariant2 = @(t,x)[(A(.413)*x)];



for l=1:100
    y0 = [1; 1];
    tspan = (l-1)*1000:.1:l*1000;
    [t,y] = ode45(F,tspan,y0);
    % [ti,yi] = ode45(F_invariant,tspan,y0);
    % [tr,yr] = ode45(F_invariant2,tspan,y0);

    plot(y(:,1),y(:,2),'LineWidth',.5); hold on;
end


%% eye space %%
%A = @(t)[-sin(19*t) cos(23*t); -cos(17*t) -sin(31*t)];
p = -.004;
tk = 0;
A = @(t)([sin(tk+sin(3*t)) cos(tk); -cos(tk) -sin(tk)]);

F = @(t,x)[(A(t)*x)];
F_invariant = @(t,x)[(A(100)*x)];
F_invariant2 = @(t,x)[(A(.413)*x)];



for l=1:100
    y0 = [1; 1];
    tspan = (l-1)*1000:.1:l*1000;
    [t,y] = ode45(F,tspan,y0);
    % [ti,yi] = ode45(F_invariant,tspan,y0);
    % [tr,yr] = ode45(F_invariant2,tspan,y0);

    plot(y(:,1),y(:,2),'LineWidth',.5); hold on;
end

%% the dragonfly %%
%A = @(t)[-sin(19*t) cos(23*t); -cos(17*t) -sin(31*t)];
p = -.004;
A = @(t)([-t^p*sin(t) t^p*cos(t); -cos(t) -sin(t)]*sin(t));

F = @(t,x)[(A(t)*x)];
F_invariant = @(t,x)[(A(100)*x)];
F_invariant2 = @(t,x)[(A(.413)*x)];

for l=1:200
    y0 = [1; 1];
    tspan = (l-1)*50:.001:l*50;
    [t,y] = ode45(F,tspan,y0);
    % [ti,yi] = ode45(F_invariant,tspan,y0);
    % [tr,yr] = ode45(F_invariant2,tspan,y0);

    plot(y(:,1),y(:,2),'LineWidth',.5); hold on;
end
plot(yi(:,1),yi(:,2));hold on;
plot(yr(:,1),yr(:,2));

%% bad slinky %%
%A = @(t)[-sin(19*t) cos(23*t); -cos(17*t) -sin(31*t)];
p = -.004;
A = @(t)[-t^p*sin(t) t^p*cos(t); -cos(t) -sin(t)];

F = @(t,x)[(A(t)*x)];
F_invariant = @(t,x)[(A(100)*x)];
F_invariant2 = @(t,x)[(A(.413)*x)];

for l=1:200
    y0 = [1; 1];
    tspan = (l-1)*50:.001:l*50;
    [t,y] = ode45(F,tspan,y0);
    % [ti,yi] = ode45(F_invariant,tspan,y0);
    % [tr,yr] = ode45(F_invariant2,tspan,y0);

    plot(y(:,1),y(:,2),'LineWidth',.5); hold on;
end
plot(yi(:,1),yi(:,2));hold on;
plot(yr(:,1),yr(:,2));

%% bad cyclones %%
%A = @(t)[-sin(19*t) cos(23*t); -cos(17*t) -sin(31*t)];
p = -.004;
A = @(t)[-t^p*sin(t) t^p*cos(t); -cos(t) -sin(t)];

F = @(t,x)[(A(t)*x)];
F_invariant = @(t,x)[(A(100)*x)];
F_invariant2 = @(t,x)[(A(.413)*x)];

for l=1:4
    y0 = [1; 1];
    tspan = (l-1)*500:.001:l*500;
    [t,y] = ode45(F,tspan,y0);
    % [ti,yi] = ode45(F_invariant,tspan,y0);
    % [tr,yr] = ode45(F_invariant2,tspan,y0);

    plot(y(:,1),y(:,2),'LineWidth',.5); hold on;
end
plot(yi(:,1),yi(:,2));hold on;
plot(yr(:,1),yr(:,2));

%% apes %%
%A = @(t)[-sin(19*t) cos(23*t); -cos(17*t) -sin(31*t)];
p = -.004;
A = @(t)[-t^p*sin(t) t^p*cos(t); -cos(t) -sin(t)];

F = @(t,x)[(A(t)*x*cos(norm(x)/100))];
F_invariant = @(t,x)[(A(100)*x)];
F_invariant2 = @(t,x)[(A(.413)*x)];

for l=1:5
    y0 = [1; 1];
    tspan = (l-1)*500:.001:l*500;
    [t,y] = ode45(F,tspan,y0);
    % [ti,yi] = ode45(F_invariant,tspan,y0);
    % [tr,yr] = ode45(F_invariant2,tspan,y0);

    plot(y(:,1),y(:,2),'LineWidth',1.9); hold on;
end
% plot(yi(:,1),yi(:,2));hold on;
% plot(yr(:,1),yr(:,2));
set(gca,'Color','g')
