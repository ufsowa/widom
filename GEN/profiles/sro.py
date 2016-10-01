#!/usr/bin/env python

from __future__ import division
import numpy as np
import math
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import sys

#----------------------------------``
# Program generujacy nadstrukture B2 o zadanych rozmiarach
def B2(X,Y,Z):
    system={}
    for i in np.arange(0,X,2):
	for j in np.arange(0,Y,2):
	    for k in np.arange(0,Z,2):
		system[(i,j,k)]='Ni'
		system[(i+1,j+1,k+1)]='Al' 
    return system

# Program for getting maximal and minimal x,y,z from dictionary of form (x,y,z):atom
# OUTPUT: tuple of form (xmin, xmax, ymin,ymax,zmin,zmax)
def get_bounds(d):
    X=[]
    Y=[]
    Z=[]
    for i in d.keys():
	X.append(i[0])
	Y.append(i[1])
	Z.append(i[2])
    xmin = min(X)
    xmax = max(X)
    ymin = min(Y)
    ymax = max(Y)
    zmin = min(Z)
    zmax = max(Z)
    return (xmin, xmax, ymin,ymax,zmin,zmax)

# Boundary conditions function
# Arguments: tuple(x,y,z), tuple(xmin, xmax, ymin,ymax,zmin,zmax), lattice_constant
#OUTPUT: tuple
def period_bound(point, bounds, lc):
    px = bounds[1]-bounds[0]
    py = bounds[3]-bounds[2]
    pz = bounds[5]-bounds[4]
    p0 = 0
    p1 = 0
    p2 = 0
    if point[0]<bounds[0]:
	p0 += px+(lc/2)
	#print 'pcham_x'
    if point[0]>bounds[1]:
	p0 -= (px+(lc/2))
	#print 'cofam_x'
    if point[1]<bounds[2]:
	p1 += py +(lc/2)
	#print 'pcham_y'
    if point[1]>bounds[3]:
	p1 -=(py +(lc/2))
    if point[2]<bounds[4]:
	p2 +=(py +(lc/2))
    if point[2]>bounds[5]:
	p2 -=(py +(lc/2))
	#print 'cofam_y'
    return (point[0]+p0,point[1]+p1,point[2]+p2)

#Program do analizy domenowej [argument: plik .xyz, rozmiar oczka siatki(bok kwadratu dla ktorego analiza ETA)], OUTPUT: mapa gestosci uporzadkowania

def atom_typ(atom):
    if(atom=="Fe"):
	typ=0
    elif(atom=="Ni"):
        typ=1
    elif(atom=="Al"):
        typ=2
    else:
        print "No such atoms defined", atom; sys.exit(0);
    return typ

def hist(xyz,k,s):
    d = XYZtoDICT(xyz)
    dim = get_bounds(d)
    HIS={};
    l=int(dim[(0+k)])
    r=int(dim[(1+k)])
    k=int(k/2)
    for i in range(l,r,1):
	HIS[(i,i+s)]=[0,0,0]
    for point in d.keys():
	atom=atom_typ(d.get(point))
	key_his=(0,2)
	for element in HIS.keys():
	    if( (point[k] >= element[0]) and (point[k] < element[1])):
		HIS[element][atom]+=1;
    return HIS

def domains(xyz,grid):
    #Lattice constant -a factor which adapt BCC grid to xyz file  
    lc = 1
    # Plik XYZ zapisany jako slownik do zmiennej d
    d = XYZtoDICT(xyz)
    d_eta = d.copy()
    # Here we get sample dimensions from dictionary to introduce periodic boundary conditions 
    dim = get_bounds(d)
    print dim
    #Iteracja po kolejnych krotkach w slowniku d
    for point in d.keys():
        #Tu zapisywane beda krotki z szescianu wokol kolejnych punktow
        checkList = []
        checkList2 = []
        seq1 = ''
        seq2 = ''
        A1 = 0
        A2 = 0
	B1 = 0
	B2 = 0
	V1 = 0
	V2 = 0
#        for i in range(-lc*grid,+(lc*grid+1),2):
#	    for j in range(-lc*grid,+(lc*grid+1),2):
#                for k in range(-lc*grid,+(lc*grid+1),2):
#	            checkList.append((point[0]+lc*i,point[1]+lc*j, point[2]+lc*k))		#zaokraglic do int
        for i in range(-2,2+1,4):
	    checkList2.append((point[0]+i,point[1],point[2]))
	for i in range(-2,2+1,4):
	    checkList2.append((point[0],point[1]+i,point[2]))
        for i in range(-2,2+1,4):
           checkList2.append((point[0],point[1],point[2]+i))
        
        for a in checkList:
	# Here we use function period_bound to apply boundary conditions 
	    a = period_bound(a,dim,2)
	    #print a 
	    seq1 += d.get(a,'')
        for b in checkList2:
	    b = period_bound(b,dim,2)
	    seq2 += d.get(b,'')
        A1 = seq1.count('Ni')
        A2 = seq2.count('Ni')
        B1 = seq1.count('Al')
        B2 = seq2.count('Al')
        V1 = seq1.count('Fe')
        V2 = seq2.count('Fe')
#        eta = ETA(A1,A2)
#        d_eta[point] = round(eta,3)
	atom=d[point]
	eta=(atom,V1,A1,B1,V2,A2,B2)
        d_eta[point] = eta
    return d_eta


# Program do wczytywania pliku XYZ w formie slownika
def XYZtoDICT(xyz):
    d = {}
    with open(xyz) as f:
        for line in f:
            if line[0] == 'N' or line[0] == 'A' or line[0] == 'F':
                (at,x,y,z) = line.split()
                d[(float(x),float(y),float(z))] = at
    return d

def ETA(A1,A2):
    eta = abs(A1-A2)/(A1+A2)
    return eta

def WRITE_DICT_DENS(system,plik):
    with open(plik,'w') as p:
        for j in system.keys():
	    for i in j:
        	p.write('%.1f '%(i))
            p.write(' '.join(str(s) for s in system[j]) + '\n')
#-----------------------------------------

def PLOT_DOMAINS(plik):
    with open(plik) as f:
        X=[]
        Y=[]
        Z=[]
        C=[]
        for line in f:
            (x,y,z,c) = line.split()
	    if(float(c)>eta):
        	X.append(float(x))
        	Y.append(float(y))
        	Z.append(float(z))
        	C.append(float(c))
#    fig = plt.figure()
#    ax = fig.add_subplot(111, projection='3d')
    #plt.close()
    #plt.clf()
#    ax.scatter(X,Y,Z,c=C, s=30)
    #plt.plot(X,Y,'.')
    #plt.plot(T,D,'.')
    #plt.colorbar()
#    ax.view_init(30, -60)
#    plt.show()
#    plt.savefig("test.png")
#    plt.close()

# Program using another techniqe - real structure is compared with ideal B2 mask
def DOMAINS_HD(xyz):
    d = XYZtoDICT(xyz)
    limits = get_bounds(d)
    X = limits[1]
    Y = limits[3]
    Z = limits[5]
    ref = B2(X+1,Y+1,Z+1)
    for i in d.keys():
	paint = 0
	a = d[i]
	b = ref[i]
	if a==b:
	    paint+=1
	elif a+b == 'NiAl' or a+b=='AlNi':
	    paint+=0.1
	else:
	    #print 'O, wakancja'
	    paint+=0.5
	d[i] = paint
    return d

xyz = sys.argv[1]
plik = sys.argv[2]
grid = int(sys.argv[3])
eta = float(sys.argv[4])
#WRITE_DICT_DENS(domains(xyz,grid),plik)
WRITE_DICT_DENS(hist(xyz,0,2),("x"+plik))
WRITE_DICT_DENS(hist(xyz,2,2),("y"+plik))
WRITE_DICT_DENS(hist(xyz,4,2),("z"+plik))

#PLOT_DOMAINS(plik)


