#!/usr/bin/env python

import sys
import numpy as np

#print "Licze srednia..."

#1 1000 3000 14125 14125 1.01882e+06 1.4327e+06 428.963 7.89112
#1 2    3    4     5     6           7          8       9

name=sys.argv[1]
iterr=0

temp,v,a,b,aa,s,ar,s,ba,s,br,s=np.loadtxt(name, unpack=True)

kb=8.61733034E-5
T=temp
V=v
A=a
B=b

N=A+B+V
Oa=A/N
Ob=B/N

miAa=-(kb*T)*(np.log((v*aa)/(a+1.0)))
miAr=(kb*T)*(np.log((a*ar)/(v+1.0)))
miBa=-(kb*T)*(np.log((v*ba)/(b+1.0)))
miBr=(kb*T)*(np.log((b*br)/(v+1.0)))

miA=((1-Oa-Ob)*miAa)/(1-Ob) + ((Oa)*miAr)/(1-Ob)
miB=((1-Oa-Ob)*miBa)/(1-Oa) + ((Ob)*miBr)/(1-Oa)


name="mi.dat"

np.savetxt(name,zip(temp,v,a,b,miAa,miAr,miBa,miBr,miA,miB), "%f")
#outf=open(name,"w")
#outf.write("%f %f %f %f %f %f %f %f %f %f\n" % (temp,v,a,b,miAa,miAr,miBa,miBr,miA,miB))
#outf.close()