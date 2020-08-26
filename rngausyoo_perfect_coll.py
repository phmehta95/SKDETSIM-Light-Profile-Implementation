import os
import math
import array as arr
import numpy as np
import matplotlib.pyplot as plt
import random


x1 = random.random()
x2 = random.random()
#print x1, x2

Sigbm = 0
Sigbm_hold = []

for x in np.arange(0,8000,1):

    Sigbm = x
    Sigbm_hold.append(Sigbm)

Sigbm_arr = np.array(Sigbm_hold)

Sigma = 0
Sigma_hold = []

for x in range(len(Sigbm_hold)):

    Sigma = x * (math.pi)/180
    Sigma_hold.append(Sigma)

RND = 0
RND_hold = []
Sigma_arr = np.array(Sigma_hold)

for y in Sigma_arr:
    RND1 = x1*y - (y/2)
    RND2 = x2*y - (y/2)
    RND = abs((RND1+RND2)/2)
    RND_hold.append(RND)


RND_arr = np.array(RND_hold)
RND_new_hold=[]

for x in RND_arr:

    ang = math.sqrt((x**2)/(3610**2))
#    ang_hold.append(ang)
    ang1 = math.sqrt(ang)
#    ang1_hold.append(ang1)
    RND_new = math.degrees(math.atan(ang1))
    RND_new_hold.append(RND_new)

print RND_new_hold
RND_new_arr = np.array(RND_new_hold)

plt.figure()
plt.plot(Sigbm_arr,RND_new_arr)
plt.xlabel('Sigbm value')
plt.ylabel('RND value')
plt.show()
