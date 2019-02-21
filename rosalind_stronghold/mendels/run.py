
from __future__ import division

k = 22

m = 15

n = 22

s = k + m + n

a = n/s*(n-1)/(s-1)*1.0

b = 2*n/s*0.5*m/(s-1)

c = m/s*(m-1)/(s-1)*0.25

#print("%.5f" % c)

print (1-(a+b+c))
