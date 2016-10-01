#!/usr/bin/env python

import sys
import numpy as np

#print "Licze srednia..."

#1 1000 3000 14125 14125 1.01882e+06 1.4327e+06 428.963 7.89112
#1 2    3    4     5     6           7          8       9


start=int(sys.argv[1])
name=sys.argv[2]
iterr=0

step,temp,v,a,b,aa,ba,ar,br=np.loadtxt(name,skiprows=start, unpack=True)

N=len(step)

#aa=aa/N
#ba=ba/N
#ar=ar/N
#br=br/N

kb=8.61733034E-5
beta=1.0/(kb*temp[0])
#aa=aa/N	#	np.exp(-beta*aa)
#ba=ba/N	#	np.exp(-beta*ba)
#ar=ar/N	#	np.exp(-beta*ar)
#br=br/N	#	np.exp(-beta*br)

Aa=np.mean(aa)
sAa=np.std(aa)
Ar=np.mean(ar)
sAr=np.std(ar)
Ba=np.mean(ba)
sBa=np.std(ba)
Br=np.mean(br)
sBr=np.std(br)

name="sr.dat"
outf=open(name,"w")
outf.write("%f %f %f %f %f %f %f %f %f %f %5.10f %5.10f\n" % (temp[0],v[0],a[0],b[0],Aa,sAa,Ar,sAr,Ba,sBa,Br,sBr))
outf.close()