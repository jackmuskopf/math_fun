f= '@ (x1,x2,x3,x4) a*x1.^4 - x2.^2 + x3.^2 - x1*x2 -x2*x3 -x3*x1';
a= 1;
grad = @(x) [4*1*x(1)^3- x(2) - x(3); 2*x(2)-x(1)-x(3); 2*x(3)-x(2)-x(1);0];
%%subplot (1,2,1)
x_initial = [1;1;1;1];
P= [3/4, -1/4, -1/4, -1/4; 
   -1/4,  3/4, -1/4, -1/4; 
   -1/4, -1/4,  3/4, -1/4;
   -1/4, -1/4, -1/4, 3/4];
%%alpha = 0.05
[x1,f1,n1]= grad_des_woptgamma_constrained (f, grad, x_initial, P);
%%subplot(1,2,2)