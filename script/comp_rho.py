#!/usr/bin/python

# 2p orbitals

import numpy as np
import scipy.special as sc
import scipy.constants as constants
import scipy.integrate as integrate

a_0 = constants.hbar / (constants.m_e * constants.c * constants.fine_structure)

a = 1./137
a = 7.2973525693E-3
Z = 1.0

n           = 2
orb         = 'p'
onset       = 1
k_plus      = -2
k_minus     = 1
nr_plus     = n - np.abs(k_plus)
nr_minus    = n - np.abs(k_minus)
def gamma_plus(Z):
   gp = np.sqrt(k_plus**2 - a**2 * Z**2)
   return gp
def gamma_minus(Z):
   gm = np.sqrt(k_minus**2 - a**2 * Z**2)
   return gm
def N_plus(Z):
   Np = np.sqrt(n**2 - 2*nr_plus * (np.abs(k_plus) - gamma_plus(Z)))
   return Np
def N_minus(Z):
   Nm = np.sqrt(n**2 - 2*nr_minus * (np.abs(k_minus) - gamma_minus(Z)))
   return Nm

def exp_rho_plus(Z):
   exp = (((gamma_plus(Z) + nr_plus) * (3*N_plus(Z)**2 - k_plus**2) - k_plus*N_plus(Z))
          / N_plus(Z))
   return exp
def exp_rho_minus(Z):
   exp = (((gamma_minus(Z) + nr_minus) * (3*N_minus(Z)**2 - k_minus**2) - k_minus*N_minus(Z))
          / N_minus(Z))
   return exp

fn = "comp" + str(n) + orb + ".dat"
comp = open(fn, mode="w")



for Z in range(onset,120):
   expm = exp_rho_minus(Z)
   expp = exp_rho_plus(Z)
   comp.write(str(Z) + '  ' + str(expm) + '  ' + str(expp) + '\n')
   print str(Z), str(expm), str(expp)
