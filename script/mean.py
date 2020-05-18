#!/usr/bin/python


import numpy as np

fname = "L.dat"
fname = "M.dat"
fname = "M45.dat"

a = np.loadtxt(fname)

b= []
for i in range (0,len(a)):
   ratio = a[i][1] / a[i][0]
   b.append(ratio)
   print ratio


mean = np.mean(b)
std = np.std(b)

print "mean = ", mean
print "std = ", std
