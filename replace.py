#! /usr/bin/python

# IMPORT
import os
import sys
import shutil
import string
import glob
import math

ls = os.listdir('.')
ls.sort()

count = 0

rootdir = os.getcwd()
#outfile = open('','w')

for filename in glob.glob("*.tex"):
#for filename in glob.glob("schale08.tex"):
   print filename
   infile = open(filename, 'r')
   outfile = open('tmpfile', 'w')

   
#   replacements = {'includegraphics[scale=0.5]':'input', '/compl':'/schale', '/incompl':'/in-shell', '_':'-core', '.ps':'', 'caps':'cap'}
   replacements = {'Auger':'Meitner'}

   for line in infile:
      if 'FloatBarrier' not in line:
          for src, target in replacements.iteritems():
              line = line.replace(src, target)
          outfile.write(line)

   infile.close()
   outfile.close()

   shutil.copyfile('tmpfile',filename)
   os.remove('tmpfile')
