function gamma=optgamma(grad,x,P)
% optgamma.m is the implementation of the secant algorithm to solve for the
% optimal step size for the steepest descent method.
% The function accepts the gradient grad and initial guess x0. 
% The function produces an approximation to the optimal step size.
%
% Define grad as a handle to the gradient. Ex. grad=@(x) [2*x(1); 2*x(2)]
% Provide x as a vector. Ex. x=[1;1].
% 
% D.B.Ekanayake, 9/25/2017
maxn = 500;     % maximum number of iterations
tol=10^(-8);    % termination tolerance
% Initialization
gamma_new=0;
gamma=10^(-5);
dphi_old=-grad(x-gamma_new*grad(x))'*grad(x);
dphi_new=dphi_old;
n=0;
% The secant algorithm:
while abs(dphi_new)>tol
    gamma_old=gamma_new;
    gamma_new=gamma;
    dphi_old=dphi_new;
    dphi_new=-grad(x-gamma_new*P*grad(x))'*P*grad(x);
    gamma=(dphi_new*gamma_old-dphi_old*gamma_new)/(dphi_new-dphi_old);
    n=n+1;
    if n==maxn
       error('maximum number of iterations reached gamma')
    end
end 