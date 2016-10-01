#!/usr/bin/env python

import sys
import numpy as np

#print "Licze srednia..."



ile=int(sys.argv[1])
lista=sys.argv[2:2+ile]
init=str(sys.argv[ile+2])
s=float(sys.argv[ile+3])
err=float(sys.argv[ile+4])
iterr=0

#name="u"+u1+"u"+u2+"N.dat"

#print ile,lista,init,s,err

X=[];V=[];B=[];A=[];
for name in lista:
    x1,x2,v,a,b=np.loadtxt(name, unpack=True)
    X.extend(x1);V.extend(v);A.extend(a);B.extend(b);
#    print name,len(V),len(A),len(B)

X=np.array(X)
V=np.array(V)
A=np.array(A)
B=np.array(B)
cv=V/(V+A+B)

if(init=="nul"):
    sr=np.mean(cv)
    od=np.std(cv)
else:
    sr=float(init)
    od=0.5*sr
    
print sr,od,len(V),len(X)

while (od>err):
    cv_new=[]
    x_new=[]
    old=od
    iterr=0
    for i in cv:
	if ((i>sr-od*s) and(i<sr+od*s)):
	    cv_new.append(i)
	    x_new.append(X[iterr])
	iterr+=1
    #cv=cv_new
    #X=x_new
    sr=np.mean(cv_new)
    od=np.std(cv_new)
    print sr,od,len(cv_new),len(x_new)
    if(old==od):
	break;


nameout="sr.dat"
#outf=open(nameout,"w")
np.savetxt(nameout,zip(x_new,cv_new),"%f")
#outf.write("%f %f\n" % (sr,od))
#outf.close()