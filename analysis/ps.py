#!/usr/bin/python


import numpy as np

fname = "Sr/EV33.dat"
fname = "Sr/EV31.dat"
fname = "Sr/EV11.dat"
fname = "Sr/EV33_comp.dat"
fname = "Sr/EV31_comp.dat"
fname = "Sr/EV11_comp.dat"

a = np.loadtxt(fname)

b= []
for i in range (0,len(a)):
   tmp = a[i][4]
   b.append(tmp**2)

print sum(b)
