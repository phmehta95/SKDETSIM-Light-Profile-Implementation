import numpy as np
#import scipy as sp
import random
from math import * 
import matplotlib.pyplot as plt

ilist = np.arange(0,8000,1).tolist()
random1 = []
sigbm = []
linVal = []

for i in ilist:

    rnd = 0.5*i
    ang = sqrt(rnd**2/(3610**2))
    ang = sqrt(ang)
    rnd = degrees(np.arctan(ang))

#    print(rnd)
    random1.append(rnd)


for i in ilist:
    rVAL = random.uniform(0,1)-0.5
    val = rVAL*7200
    ang2 = sqrt(val**2/(3610**2))
    ang2 = sqrt(ang2)
    val = degrees(np.arctan(ang2))
    #print(val, ang2)
    sigbm.append(val) 
    linVal.append(rVAL)


plt.plot(ilist, random1)
plt.xlabel('sigbm')
plt.ylabel('RND - angle [degrees])')
#plt.savefig("maxAng_sigbmVar.jpg")
plt.show()

plt.scatter(ilist, sigbm,s=0.1)
plt.xlabel('sigbm')
plt.ylabel('RND - angle [degrees]')
#plt.savefig("angVar_sigbm7200.jpg")
#plt.show()

plt.scatter(ilist, linVal, s=0.1)
plt.xlabel('sigbm')
#plt.savefig("rndVal.jpg")
#plt.show()


randsigm = []

for i in ilist:

    rVAL = random.uniform(0,1)-0.5
    val = rVAL*i
    ang2 = sqrt(val**2/(3610**2))
    ang2 = sqrt(ang2)
    val = degrees(np.arctan(ang2))
                                                                                                       
    randsigm.append(val)

bottom,top = plt.ylim()
start,finish = plt.xlim()
plt.ylim(0,5)
plt.xlim(0,50)
plt.plot(ilist,random1,'k-', linewidth=2)
plt.scatter(ilist, randsigm, s=0.3,c='r',marker='o',edgecolors='face')
plt.xlabel('sigbm')
plt.ylabel('Angle [degrees]')
#plt.savefig("randSigbm_angVar_zoom.jpg")
plt.show()
