#!/usr/bin/env python

################ Zaladuj moduly ###################
import numpy as np
import sys
import os
#import operator
#import matplotlib.pyplot as plt
from scipy import interpolate
######## Koniec modulow ###########################

########## Definicje funkcji ##################################

def get_cross(stech,u,s):
    x=np.arange(u[0],u[-1],(u[1]-u[0]))
    y=x*0+stech
    return cros;



#######poczatek funkcji find_path_for #########################
# Iteruje po a i dla kazdego a szuka                          #
# takiego b dla ktorego c rowna sie iloraz +/- limit          #
# Dokladnosc przeszukiwania po b jest okreslona przez density #
###############################################################
def find_path_for(a,b,c,v,tdi,u):
    x=[];y=[];yv=[];yt=[];i=0;
    bufor=a[0];
    while i < len(a):
		pkt=a[i]
#	print i,len(a),bufor,pkt
#	o=raw_input("dalej:")
		if(bufor==pkt):
			x.append(b[i])
			y.append(c[i])
			yv.append(v[i])
			yt.append(tdi[i])
		elif(bufor!=pkt):
			rezultat=crossu1(bufor,x,y,yv,yt)
			fout.write("%f %f %f %f %f\n" % rezultat)
			bufor=pkt
			i=i-1
			x=[];y=[];yv=[];yt=[];
		i+=1
#    print x
    rezultat=crossu1(bufor,x,y,yv,yt)
#    np.savetxt("stech.dat",' '.join(rezultat),fmt='%f',newline="\n")
    fout.write("%f %f %f %f %f\n" % rezultat)
###############bufor,centter,fstech(centter),fcv(centter),ftdi(centter)## Koniec funkcji find_path_for ################

#######poczatek funkcji cross #################################
# Uzywana w funkcji find_path_for                             #
# Skanuje po wartosciach a i szuka takiwgo a dla ktorego      #
# b rowna sie iloraz z dokladnoscia limit i density           #
# Zapisuje wyniki w pliku chem.dat			      #
###############################################################
def crossu1(bufor,x,y,yv,yt):
    atu2=[]
    atstech=[]
    atCV=[]
    atTDI=[]
    vau2=[]
    vastech=[]
    vaCV=[]
    vaTDI=[]
    kk=0
    newx,newy= zip(*sorted(zip(x,y)))
    fstech=interpolate.interp1d(newx,newy,kind='linear',bounds_error=False,fill_value=newy[0])
    newx,newy= zip(*sorted(zip(x,yv)))
    fcv=interpolate.interp1d(newx,newy,kind='linear',bounds_error=False,fill_value=newy[0])
    newx,newy= zip(*sorted(zip(x,yt)))
    ftdi=interpolate.interp1d(newx,newy,kind='linear',bounds_error=False,fill_value=newy[0])
    for kk in np.arange(0,len(yv),1):
	if(yv[kk] <= 0.4):
	    atu2.append(x[kk])
	    atstech.append(y[kk])
	    atCV.append(yv[kk])
	    atTDI.append(yt[kk])
	if(yv[kk] > 0.6):
	    vau2.append(x[kk])
	    vastech.append(y[kk])
	    vaCV.append(yv[kk])
	    vaTDI.append(yt[kk])
    if(len(atu2) > 0):    
	newa,newb= zip(*sorted(zip(atstech,atu2)))
	newc=np.diff(newb)
#	newa=list(newa)
#        newb=list(newb)
#        newc=list(newc)
        kr=0;pure_a=[];pure_b=[];pure_c=[];
        for kkk in newc: #np.arange(0,len(newc),1):
            if(kkk < 0):
        	pure_a.append(newa[kr])
        	pure_b.append(newb[kr])
        	pure_c.append(newc[kr])
	    kr=kr+1
        centter=np.interp(iloraz,pure_a,pure_b,left=pure_b[0], right=pure_b[-1])		#mediana
    else:
	newa,newb=zip(*sorted(zip(vastech,vau2)))
	newc=np.diff(newb)
        kr=0;pure_a=[];pure_b=[];pure_c=[];
        for kkk in newc:
	    if(kkk < 0):
        	pure_a.append(newa[kr])
        	pure_b.append(newb[kr])
        	pure_c.append(newc[kr])
	    kr=kr+1
        centter=np.interp(iloraz,pure_a,pure_b,left=pure_b[0], right=pure_b[-1])		#mediana
    np.savetxt("test.dat",zip(pure_a,pure_b,pure_c),fmt='%f')
    return (bufor,centter,fstech(centter),fcv(centter),ftdi(centter))
######## Koniec funkcji cross  ##################




### Koniec definicji funkcji ###########

############### Inicjalizacja ###############
#wczytuje argumenty uruchomieniowe programu
iloraz=float(sys.argv[1])
#density=int(sys.argv[2])
limit=0.0001 #float(sys.argv[2])

u1,u2,v1,sv1,v2,sv2,a1,sa1,a2,sa2,b1,sb1,b2,sb2,stech=np.loadtxt("map.dat",skiprows=0, unpack=True)

#narazie puste zmienne
CHEM1=[];CHEM2=[];
#plik do kotrego zapisujemy
nazwa="stech"+str(iloraz)+".dat"
fout=open(nazwa,"w")

V=v1+v2
N=v1+v2+a1+a2+b1+b2
CV=V/N
TDI=V/N	#a2/v1
#print v1,v2,CV






############# Run and Save ##################
#wywolujemy funkcje
#print type(u1)
#if(type(u1)==type(np.float64(0)) or type(u1)==type(np.float32(0))):
#    fout.write("%f %f %f %f %f\n" % (u1,u2,stech,CV,TDI))
#find_path_for(u1,u2,stech,CV,TDI,1)

if(type(u1)==type(np.float64(0)) or type(u1)==type(np.float32(0))):
    fout.write("%f %f %f %f %f\n" % (u1,u2,stech,CV,TDI))
else:
    find_path_for(u1,u2,stech,CV,TDI,1);

#fout.write("%f %f %f %f %f\n" % (c,centter,f(centter),fsmoth(centter),ftdi(centter)))

#chem1,chem2,stechu2,CVu2=zip(*sorted(zip(u1,u2,stech,CV),key=operator.itemgetter(1)))
#for i in np.arange(0,41,1):
#    print u1[i],u2[i],stech[i],CV[i],chem1[i],chem2[i],stechu2[i],CVu2[i]
#fout.write("u2:\n")
#find_path_for(chem2,chem1,stechu2,CVu2,2);

    
#zamknij strumien do pliku
fout.close()

print nazwa
#polecenia systemowe
#bashCommand= "cat nazwa" # -> wypisze zawartosc pliku cehm.dat w terminalu
#wywolanie w shellu polecenia zdefinowanego w bashCommand
#os.system(bashCommand)

####### KONIEC #######

#tck=interpolate.splrep(x,y,s=0)
#f2=interpolate.splev(xnew,tck,der=0)
#f2=interpolate.InterpolatedUnivariateSpline(x,y)

#
#plt.plot(x,y,'o',xnew,f(xnew),'-',xnew,f2(xnew),'--')
#plt.plot(x,y,'o',xnew,f(xnew),'-',xnew,f2(xnew),'--')
#plt.legend(['data','linear','cubic'], loc = 'best')
#plt.show()
