#!/usr/bin/python

# 2p orbitals

import numpy as np
import scipy.special as sc
import scipy.constants as constants
import scipy.integrate as integrate

a_0 = constants.hbar / (constants.m_e * constants.c * constants.fine_structure)

#a = 1./137
a = 1./constants.c
Z = 1.0

#gamma = np.sqrt(1 - a**2 * Z**2)
#gammap = np.sqrt(4 - a**2 * Z**2)
#
#
#res1 =   (1 + 2*gamma)**2 \
#       + (1 + 2*gamma)**2 * (4 - 4 * np.sqrt(2 + 2*gamma))  \
#         / (4 * (2 + 2*gamma - np.sqrt(2 + 2*gamma)) )   \
#         / np.sqrt( 1 + a*Z / gamma)   
#res2 =   (3 + 2*gamma) * (2 + 2*gamma)   \
#         * (6 + 4*gamma - 4*np.sqrt(2 + 2*gamma))   \
#         / (4 * (2 + 2*gamma - np.sqrt(2 + 2*gamma)))
#res3 =   (np.sqrt(2 + 2*gamma) - 2) * (2 + 2*gamma) * (1 + 2*gamma) \
#         / (2 + 2*gamma - np.sqrt(2 + 2*gamma))
#
#res = res1 + res2 - res3
#
#print "res1 = ", res1
#print "res2 = ", res2
#print "res3 = ", res3
#print "res = ", res
#
#plus = 1 + 2*gammap
#print "plus = ", plus


gamma1 = np.sqrt(1-a**2 * Z**2)
gamma2 = np.sqrt(4 - a**2 * Z**2)
gamma3 = np.sqrt(9 - a**2 * Z**2)
N1 = 1
N2 = np.sqrt(2* (1+gamma1))
N3 = 2

eps1 = (1 + (a*Z/gamma1)**2)**(-0.5)
eps2 = (1 + (a*Z/(1+gamma1))**2)**(-0.5)
eps3 = (1 + (a*Z/gamma2)**2)**(-0.5)

#rho = lambda r: 2*Z*r / N / a_0
rho2 = lambda r: 2*Z*r / N2
rho3 = lambda r: 2*Z*r / N3

#Start from Bethe Salpeter
#g12 = lambda r: (2*Z/N2/a_0)**(3./2) \
g12 = lambda r: (2*Z/N2)**(3./2) \
                * np.sqrt((2*gamma1 + 1) / sc.gamma(2*gamma1 + 1))   \
                * np.sqrt((1 + eps2) / (4*N2 * (N2-1)))  \
                * np.exp(-1./2 * rho2(r))      \
                * ((N2-2) * rho3(r)**(gamma1 - 1)
                   - (N2 - 1)/(2*gamma1 + 1) * rho3(r)**gamma1)


f12 = lambda r: - np.sqrt((1-eps2) / (1+eps2))     \
                * (((2*gamma1 + 1)*N2 - (N2 - 1) * rho2(r))
                  / ((2*gamma1 + 1) * (N2-2) - (N2-1) * rho3(r)))   \
                * g12(r)

#g32 = lambda r: (Z / a_0)**(3./2)   \
g32 = lambda r: (Z / N3)**(3./2)   \
                * np.sqrt((1+eps3) / 2 / sc.gamma(2*gamma2 + 1))   \
                * np.exp(-1./2 * rho3(r)) * rho3(r)**(gamma3 - 1)

f32 = lambda r: - np.sqrt( (1 - eps3) / (1 + eps3)) * g32(r)

p12 = lambda r: r**3 * ( g12(r)**2 + f12(r)**2 )
p32 = lambda r: r**3 * ( g32(r)**2 + f32(r)**2 )

N = N2
exp12r = integrate.quad(p12, 0, 5000)[0]
print "exp12r = ", exp12r


for i in  range (0,50):
    print i*0.20, p12(i * 0.20)


N = N3
exp32r = integrate.quad(p32, 0,5000)[0]
print "exp32r = ", exp32r

for i in  range (0,50):
    print i*0.20, p32(i * 0.20)


#print "ratio = ", exp32r / exp12r
