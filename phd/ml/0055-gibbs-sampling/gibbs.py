from math import *
#from RandomArray import *
from matplotlib.pylab import * 


n=10000
rho=.99 #correlation
#Means
m1 = 10
m2 = 20
#Standard deviations
s1 = 1
s2 = 1
#Initialize vectors
x=zeros(n)
y=zeros(n)
sd=sqrt(1-rho**2)

sx = s1 * sd
sy = s2 * sd
rx = rho / s2
ry = rho / s1
# the core of the method: sample recursively from two normal distributions
# Tthe mean for the current sample, is updated at each step.
for i in range(1,n):
	x[i] = normal(m1 + rx * (y[i-1] - m2), sx)
	y[i] = normal(m2 + ry * (x[i-1] - m1), sy)

scatter(x,y,marker='o',c='r')
title('Amostrador de Gibbs')
xlabel('x')
ylabel('y')
grid()

show()

