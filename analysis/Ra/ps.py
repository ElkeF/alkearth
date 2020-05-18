#!/usr/bin/python


import numpy as np

fname = "EV33.dat"
#fname = "EV31.dat"
#fname = "EV11.dat"
#fname = "EV33_conf.dat"
#fname = "EV31_conf.dat"
#fname = "EV11_conf.dat"
#fname = "EV33_CK.dat"
#fname = "EV31_CK.dat"
#fname = "EV11_CK.dat"

#fname = "EVspinfree.dat"
#fname = "EVspinfree_conf.dat"
#fname = "EVspinfree_CK.dat"

a = np.loadtxt(fname)

b= []
for i in range (0,len(a)):
   tmp = a[i][4]
   b.append(tmp**2)

print sum(b)
