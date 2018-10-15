vm = 100;
a = 2.4;
b = -2.17;
c = 0.712;
d = 1;
q = 0.01*vm;
v = 0.05*vm;
r = 0.05*vm;
k = 0:1:100;

J = [1;0;0];
H = [a b c; 1 0 0; 0 1 0];
phi = [d 0 0];
Po = 2*eye(3,3);

% bh for beta hat
bho = [0;0;0];
bhm = bho;

beta = [10;12;-10];
dist = [];

true = [beta(1)];
pred = [bho(1)];

P = Po;
for k=0:1:100
    % initial calcs
    Pkm = H*P*H'+J*q*J';
    K = Pkm*phi'*inv(v+r+phi*Pkm*phi');
    P = Pkm - K*phi*Pkm;
    
    n = normrnd(0,q);
    nu = normrnd(0,v);
    eps = normrnd(0,r);
    beta = H*beta+J*n;
    y = phi*beta+nu+eps;
   
    bhkm = H*bhm;
    
    bhk = bhkm + K*(y-phi*bhkm);
    
    bhm = bhk;
    
    true = [true;beta(1)];
    pred = [pred;bhk(1)];
    dist = [dist;norm(bhm-beta)];

end

nx = 1:length(true);
plot(nx,true); hold on;
plot(nx,pred);
plot(1:length(dist),dist);
