#!/usr/bin/env python

import sys
import numpy as np

#print "Licze srednia..."




name=sys.argv[1]
init=str(sys.argv[2])
s=float(sys.argv[3])
err=float(sys.argv[4])
iterr=0

#name="u"+u1+"u"+u2+"N.dat"
nameout="sr.dat"
outf=open(nameout,"w")

x1,x2,v,a,b=np.loadtxt(name, unpack=True)

cv=v/(v+a+b)

if(init=="nul"):
    V=np.mean(cv)
    sV=np.std(cv)
else:
    V=float(init)
    sV=0.5*V
    
print V,sV,len(x1)

while (sV>err):
    cv_new=[]
    old=sV
    for i in cv:
	if ((i>V-sV*s) and(i<V+sV*s)):	#
	    cv_new.append(i)
    cv=cv_new
    V=np.mean(cv)
    sV=np.std(cv)
    print V,sV,len(cv)
    if((old-sV)<err):
	break;

outf.write("%s %f %f\n" % (name,V,sV))
outf.close()