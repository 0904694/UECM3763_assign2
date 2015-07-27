import pylab as p

# Let
alpha = 1;  
theta = 0.064; 
sigma = 0.27;
t = 1;
r0=3;
path = 1000
n = 1000

# Simulate 1000 runs Brownian motion
dB = p.randn(path, n+1)/p.sqrt(n)
dB[:,0] = 0
B = dB.cumsum(axis = 1)
t = p.linspace(0,1,n+1)
dt = 1 / n

R = p.zeros_like(B)
R[:,0] = r0
for col in range(n):
    R[:,col+1] = R[:,col] +(theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]

# choose 5 point to show
R_plot = p.zeros([5,1001])
R_plot[0:5,:] = R[0:5,:]
p.plot(t,R_plot.transpose())
p.title('Mean Reversal Process')
p.xlabel('Time, T')
p.ylabel('R(t) ')

# Find the probability that P[R(1)>2]
Mean = p.sum(R[:,1000]) / path
print("The expected of R(1), E[R(1)] =", Mean)
P = p.sum(R[:,n] > 2) / path
print("Probability from the simulation, P[R(1) > 2] =", P)
