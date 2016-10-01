#!/usr/bin/env python

import sys
import numpy as np

name=sys.argv[1]


u1,u2,stech,cv,x=np.loadtxt(name, unpack=True)

U1=np.mean(u1)
sU1=np.std(u1)
U2=np.mean(u2)
sU2=np.std(u2)
S=np.mean(stech)
sS=np.std(stech)
V=np.mean(cv)
sV=np.std(cv)

name="sr.dat"
outf=open(name,"w")
outf.write("%f %f %f %f %f %f %f %f\n" % (U1,sU1,U2,sU2,S,sS,V,sV))
outf.close()