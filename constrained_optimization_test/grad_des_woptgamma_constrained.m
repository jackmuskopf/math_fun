function [xmin,fmin,n] = grad_des_woptgamma_constrained(f,grad,x0,P)
% grad_des.m is the gradient descent algorithm to solve unconstrained 
% optimization problems using a fixed step size. 
% The function accepts the objective function f, gradient grad,
% initial guess x0, and the step size gamma. 
% The function produces an approximation to the optimal solution xmin,
% minimum value of the function fmin, number of iterations n, and the 
% absolute successive error dabs.
%
% Define f and grad as a handle to the function. Ex. f=@(x) x(1)^2+x(2)^2.
% To plot contour lines for 2-variable functions, define f as a string.
% Ex. f = '@(x1,x2) x1^2+x2^2'
% Provide x0 as a vector. Ex. x0=[1;1]. Gamma is a positive number.
% 
% D.B.Ekanayake, 9/25/2017
maxn = 100000;        % maximum number of iterations
%%tol = 1e-6;         % termination tolerance for gradient
epsilon = 10e-6;     % termination tolerance for absolute error
 
x = x0; 
n = 0; 
disp('here');
% The gradient descent algorithm:
while and(n <= maxn, norm(P*grad(x)) >= epsilon)
    
    gamma=optgamma(grad,x,P);
%     disp(gamma);
    xnew = x - gamma*P*grad(x);
    disp(xnew);
    disp(norm(P*grad(x)));
  
    n = n + 1;
  
    if n==maxn
       error('maximum number of iterations reached main')
    end
   
    x = xnew;
    
end
xmin = x;
fmin= f(xmin);
n = n - 1;
disp(n);
