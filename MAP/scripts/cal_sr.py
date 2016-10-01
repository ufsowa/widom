#!/usr/bin/env python

import sys
import numpy as np

#print "Licze srednia..."

u1=sys.argv[1]
u2=sys.argv[2]
start=int(sys.argv[3])
name=sys.argv[4]
iterr=0

#name="u"+u1+"u"+u2+"N.dat"

step,time,v1,v2,a1,a2,b1,b2=np.loadtxt(name,skiprows=start, unpack=True)

V1=np.mean(v1)
sV1=np.std(v1)
V2=np.mean(v2)
sV2=np.std(v2)
A1=np.mean(a1)
sA1=np.std(a1)
A2=np.mean(a2)
sA2=np.std(a2)
B1=np.mean(b1)
sB1=np.std(b1)
B2=np.mean(b2)
sB2=np.std(b2)

name="sr.dat"
outf=open(name,"w")
outf.write("%s %s %f %f %f %f %f %f %f %f %f %f %f %f %f\n" % (u1,u2,V1,sV1,V2,sV2,A1,sA1,A2,sA2,B1,sB1,B2,sB2,(A1+A2)/(A1+A2+B1+B2)))
outf.close()