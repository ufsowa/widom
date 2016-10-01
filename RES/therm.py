#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
from scipy.misc import derivative


def smooth(y,box_pts,tryb='valid'):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode=tryb)
    return y_smooth


tU1,tU2,tI,tV,tsV=np.loadtxt("all.dat",unpack=True)
#U1,s1,U2,s2,I,sI,V,sV=np.loadtxt("results.dat",unpack=True)

points=int(sys.argv[1])

sortedI = sorted(tI)

liczST=0;old=0;
for i in sortedI:
    if(liczST==0):
	old=i
    if(old==i):
	liczST+=1
    else:
	break

liczEND=0;old=0;
for i in sortedI[::-1]:
    if(liczEND==0):
	old=i
    if(old==i):
	liczEND+=1
    else:
	break

print liczST,liczEND,points*(liczST+liczEND)
print len(tI),len(tU1),len(tU2)

sU1=tU1[0:liczST]
#print "sU1: ",len(sU1)
for i in np.arange(1,points,1):
    sU1=np.append(sU1,tU1[0:liczST]-0.01)
#print "sU1: ",len(sU1)
mU1=np.append(sU1,tU1)
#print "mU1: ",len(mU1)
eU1=tU1[-(liczEND+1):-1]
#print "eU1: ",len(eU1)
for i in np.arange(1,points,1):
    eU1=np.append(eU1,tU1[-(liczEND+1):-1]+0.01)
#print "eU1: ",len(eU1)
U1=np.append(mU1,eU1)
#print "U1: ",len(U1)

sU2=tU2[0:liczST]
print "sU2: ",len(sU2)
for i in np.arange(1,points,1):
    sU2=np.append(sU2,(tU2[0:liczST]+0.01))
print "sU2: ",len(sU2)
mU2=np.append(sU2,tU2)
print "mU2: ",len(mU2)
eU2=tU2[-(liczEND+1):-1]
print "eU2: ",len(eU2)
for i in np.arange(1,points,1):
    eU2=np.append(eU2,tU2[-(liczEND+1):-1]-0.01)
print "eU2: ",len(eU2)
U2=np.append(mU2,eU2)
print "U2: ",len(U2)


delta = tI[0]/points

sI=np.arange(0.0,tI[0],delta/liczST)
print "sI: ",len(sI)
mI=np.append(sI,tI)
print "mI: ",len(mI)
delta = tI[0]/points
eI=np.arange((tI[-1]),(tI[-1]+delta*points),delta/liczEND)
print "eI: ",len(eI)	#	(100.0+delta/liczEND)
I=np.append(mI,eI)

print len(I),len(U1),len(U2)


tdU=tU1-tU2
dU=U1-U2
S=I
tS=tI

#S=(I/(I+1))
#tS=(tI/(tI+1))

#print I,S

#zipped = zip(U1,U2)
#data = sorted(zipped)
#u1,u2=zip(*data)

#zipped = zip(S,U1)
#data = sorted(zipped)
#S,U1=zip(*data)

x=smooth(S,points)
y1=smooth(U1,points)
y2=smooth(U2,points)
y=smooth(dU,points)

ST=liczST*(points-5)
END=liczEND*(points-20)

x=x[ST:-END]
y1=y1[ST:-END]
y2=y2[ST:-END]
dy=y1-y2
sy=y[ST:-END]
print len(x),len(y1),len(y2)

kb=8.6173324E-5
T=1000.0
beta=kb*T

cb=1.0-x

f1 = UnivariateSpline(x,y1,k=4)
f2 = UnivariateSpline(cb,y2[::-1],k=4)

df = UnivariateSpline(x,dy,k=4)
sf = UnivariateSpline(x,sy,k=4)
g = interp1d(S,dU)

X=[];P1=[];P2=[];Pd=[];Ps=[];DERR=[];XDERR=[];
for i in range(1,(len(x)-1),1):
    s=x[i]
    X.append(s)
    P1.append(derivative(f1,s,dx=0.001))
    P2.append(derivative(f2,s,dx=0.001))
    Pd.append(derivative(df,s,dx=0.001))
    Ps.append(derivative(sf,s,dx=0.001))

#for i in range(100,(len(S)-450),1):
#    s=S[i]
for i in range(0,len(tS),1):
    s=tS[i]
#    print i,s,g(s)
    XDERR.append(s)
    DERR.append(derivative(g,s,dx=0.001))

X=np.array(X)
P1=np.array(P1)
P2=np.array(P2)
Pd=np.array(Pd)
Ps=np.array(Ps)
XDERR=np.array(XDERR)
DERR=np.array(DERR)

NEW_Y=smooth(XDERR,3,'same')
#plt.plot(tS,tU1,"+",x,y1,"o-",x,f1(x),"--", lw =2)
#plt.show()

#plt.plot(tS,tU2,"+",x,y2,"o-",x,f2(x),"--",lw =2)
#plt.show()

#plt.plot(tS,tdU,"+",x,dy,"o-",x,sy,".",x,df(x),"--",x,sf(x),"-.",lw =2)
#plt.show()

plt.plot(XDERR,(1.0-XDERR)*XDERR*DERR/beta,"x",XDERR,(1.0-XDERR)*XDERR*NEW_Y/beta,".")

#X,(1.0-X)*X*Pd/beta,"--",X,(1.0-X)*X*Ps/beta,"-.")
plt.plot(X,X*P1/beta,"--",X,(1.0-X)*P2/beta,"-.")
#plt.plot(tU1,tU2,"x",f1(x),f2(x))
plt.show()


out=open("eq_path.dat",'w')
np.savetxt("eq_raw.dat",zip(S,U1,U2),newline='\n')

for i in np.arange(0.1,0.91,0.01):
    out.write('%f %f %f\n'%(i,f1(i),f2(i)))




#X=[];Y=[];
#for i in range(1,(len(s)-1),1):
#    x=s[i]
#    print i,x,g(x)
#
#    X.append(x)
#    Y.append(der)

#PHI=[]
#for i in range(0,(len(X)),1):
#    phi=(1-X[i])*X[i]*Y[i]/beta
#    PHI.append(phi)


