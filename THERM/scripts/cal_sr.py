#!/usr/bin/env python

import sys
import numpy as np

u1=sys.argv[1]
u2=sys.argv[2]
start=int(sys.argv[3])
files=sys.argv[4:]

res=[]

for name in files:
    data=np.loadtxt(name,skiprows=start, unpack=True)
    for col in data[2:]:
	avg=np.mean(col)
	res.append(avg)

name="sro.dat"
outf=open(name,"w")
outf.write("%s %s" % (u1,u2))
for i in res:
    outf.write(" %10.5f" % (i))
outf.write("\n")
outf.close()