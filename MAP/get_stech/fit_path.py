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
    fstech=interpolate.interp1d(x,y,kind='linear')
    fcv=interpolate.interp1d(x,yv,kind='linear')
    ftdi=interpolate.interp1d(x,yt,kind='linear')
    
    for kk in np.arange(0,len(yv),1):
	if(yv[kk] <= 0.4):
	    atu2.append(x[kk])
	    atstech.append(y[kk])
	    atCV.append(yv[kk])
	    atTDI.append(yt[kk])
	elif(yv[kk] > 0.6):
	    vau2.append(x[kk])
	    vastech.append(y[kk])
	    vaCV.append(yv[kk])
	    vaTDI.append(yt[kk])
    if(len(atu2) > 0):    
	newa,newb= zip(*sorted(zip(atstech,atu2)))
	newc=np.diff(newb)
	newa=list(newa)
        newb=list(newb)
        newc=list(newc)
        kr=0
        for kkk in newc: #np.arange(0,len(newc),1):
            if(kkk >0):
    	        del newa[kr+1]
		del newb[kr+1]
	        del newc[kr+1]
	    kr=kr+1
        centter=np.interp(iloraz,newa,newb,left=10000, right=10000)		#mediana
        if(centter == 1000):
	    print centter
	    newa,newb=zip(*sorted(zip(vastech,vau2)))
	    newc=np.diff(newb)
	    newa=list(newa)
	    newb=list(newb)
	    newc=list(newc)
	    kr=0
	    for kkk in newc: #np.arange(0,len(newc),1):
		if(kkk >0):
		    del newa[kr+1]
		    del newb[kr+1]
		    del newc[kr+1]
		kr=kr+1
	    centter=np.interp(iloraz,newa,newb)		#mediana
    else:
	newa,newb=zip(*sorted(zip(vastech,vau2)))
	newc=np.diff(newb)
        newa=list(newa)
	newb=list(newb)
        newc=list(newc)
	kr=0
    #print zip(newa,newb)
        for kkk in newc: #np.arange(0,len(newc),1):
	    if(kkk >0):
	        del newa[kr+1]
		del newb[kr+1]
	        del newc[kr+1]
	    kr=kr+1
        centter=np.interp(iloraz,newa,newb)		#mediana

    np.savetxt("test.dat",zip(newa,newb,newc),fmt='%f')
    return (bufor,centter,fstech(centter),fcv(centter),ftdi(centter))
######## Koniec funkcji cross  ##################

def line(x,p):
    return p[0]*x+p[1];


### Koniec definicji funkcji ###########

############### Inicjalizacja ###############
#wczytuje argumenty uruchomieniowe programu
iloraz=float(sys.argv[1])
#density=int(sys.argv[2])
limit=0.0001 #float(sys.argv[2])

nazwa=sys.argv[1]
u1,u2,stech,cv,tdi=np.loadtxt(nazwa,skiprows=0, unpack=True)

#narazie puste zmienne
CHEM1=[];CHEM2=[];
#plik do kotrego zapisujemy
nazwa="chem"+str(stech)+".in"
fout=open(nazwa,"w")


x_to_fit=u1[:]
y_to_fit=u2[:]

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
