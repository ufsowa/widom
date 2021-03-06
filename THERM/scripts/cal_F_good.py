#!/usr/bin/env python

import sys
import numpy as np

#print "Licze srednia..."

name=sys.argv[1]
start=int(sys.argv[2])
T=float(sys.argv[3])
S=float(sys.argv[4])
iterr=0
kB=8.617332478E-5  #eV/K

print "kB= ",kB," [eV/K]"
print "T= ",T, " [K]"
#name="u"+u1+"u"+u2+"N.dat"
# 0 0 2245 44 13066 1439 314 14142


step,time,v1,v2,a1,a2,b1,b2=np.loadtxt(name,skiprows=start, unpack=True)

v=v1+v2;
a=a1+a2;
b=b1+b2;

M=v[0]+a[0]+b[0];
xv=v[0]/M
xa=a[0]/M
xb=b[0]/M
x=xv+xa+xb
print "M= ",M,xv,xa,xb,x

V=np.mean(v)
sV=np.std(v)
A=np.mean(a)
sA=np.std(a)
B=np.mean(b)
sB=np.std(b)

M=A+V+B
xv=V/M
xa=A/M
xb=B/M
x=xv+xa+xb

print "M= ",M,xv,xa,xb,x

name="sr.dat"
outf=open(name,"w")
outf.write("%f %f %f %f %f %f %f %f %f\n" % (T,S,V,sV,A,sA,B,sB,(A)/(A+B)))
outf.close()

aa=a*a;
ab=a*b;
ba=b*a;
bb=b*b;

AA=np.mean(aa)
sAA=np.std(aa)
AB=np.mean(ab)
sAB=np.std(ab)
BA=np.mean(ba)
sBA=np.std(ba)
BB=np.mean(bb)
sBB=np.std(bb)

name="sr2.dat"
outf=open(name,"w")
outf.write("%f %f %f %f %f %f %f %f %f %f %f\n" % (T,S,AA,sAA,AB,sAB,BA,sBA,BB,sBB,(AA)/(AA+BB)))
outf.close()

Obb=(BB-B*B)
Oaa=(AA-A*A)

print "O= ",Oaa,Obb
name="srO.dat"
outf=open(name,"w")
outf.write("%f %f %f %f\n" % (T,S,Oaa,Obb))
outf.close()

Fa=xb*A/Oaa
Fb=xa*B/Obb

print "Fa,Fb= ",Fa,Fb
print "dxa/dxb= ",-Fb/Fa
name="srF.dat"
outf=open(name,"w")
outf.write("%f %f %f %f %f\n" % (T,S,Fa,Fb,-Fb/Fa))
outf.close()



