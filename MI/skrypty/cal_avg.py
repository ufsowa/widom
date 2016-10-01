#!/usr/bin/env python

import sys
import numpy as np

#print "Licze srednia..."

#1 1000 3000 14125 14125 1.01882e+06 1.4327e+06 428.963 7.89112
#1 2    3    4     5     6           7          8       9


name=sys.argv[1]
iterr=0

temp,v,a,b,aa,ba,ar,br,u1,u2=np.loadtxt(name, unpack=True)

#1000.000000 300.000000 15475.000000 15475.000000 -0.523158 -0.522984 -0.523933 -0.525536 -0.522987 -0.525505

Aa=np.mean(aa)
Ar=np.mean(ar)
Ba=np.mean(ba)
Br=np.mean(br)
U1=np.mean(u1)
U2=np.mean(u2)
s1=np.std(u1)
s2=np.std(u2)

name="sr.dat"
outf=open(name,"w")
outf.write("%f %f %f %f %f %f %f %f %5.10f %5.10f %5.10f %5.10f\n" % (temp[0],v[0],a[0],b[0],Aa,Ar,Ba,Br,U1,s1,U2,s2))
outf.close()