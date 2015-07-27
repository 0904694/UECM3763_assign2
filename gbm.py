import pylab as p
import numpy as np

#Let
miu=0.1;
sigma=0.26;
s0=39;
path=5;
n=1000;
partition=1000;

#Simulate 1000 runs of Brownian motion
t=p.linspace(0,3,n+1);
dB=p.randn( path, n+1)/p.sqrt(n);
dB[:,0]=0;
B = dB.cumsum(axis=1);

a = miu-sigma*sigma/2.0;
S=p.zeros_like(B);
S[:,0]=s0;
S[:,1:]= s0*p.exp(a*t[1:]+sigma*B[:,1:]);

#Plot 5 realizations of Brownian motion
p.plot(t,S.transpose());
p.title('Geometric Brownian Motion');
p.xlabel('Time, T');
p.ylabel('Stock Price, $');
p.show();

#Calculate Expected of S(3) and Variance of S(3)
s3= S[:,1000];
exp= sum(s3)/path
print('E(s3)=', exp)
var=np.var(s3)
print('Var(s3)=',var)

#Calculate P[S(3)>39] and E[S(3)|S(3)>39]
P=sum(S[:,1000]>39)/path
print("P[S(3)>39] = ",P)
Exp=sum(S[:,1000])
print("E[S(3)|S(3)>39] =",Exp)
