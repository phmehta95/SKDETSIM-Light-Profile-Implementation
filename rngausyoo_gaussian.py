import os
import math
from array import array
import array as arr
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random



#Add up random numbers between 0 and 1 12 times
A = 0
for i in np.arange(0,12,1):
    x = random.random()
    A = A + x
print A
    
Sigbm = 0
Sigbm_hold = []

#Create array of Sigbm input values (between 0 and 8000)
for x in np.arange(0,8000,1):

    Sigbm = x
    Sigbm_hold.append(Sigbm)

Sigbm_arr = np.array(Sigbm_hold)

#print Sigbm_hold    

Sigma = 0
Sigma_hold = []

#Make array to hold values of Sigma
for x in range(len(Sigbm_hold)):
    
    Sigma = x * (math.pi)/180
    Sigma_hold.append(Sigma)


RND = 0
RND_hold = []

#A_arr = np.array(A_hold)
Sigma_arr = np.array(Sigma_hold)

RND_new = 0
RND_new_hold = []

#For each value of Sigma make array to hold RND value
for y in Sigma_arr:
    RND = (A-6)*y
    RND_hold.append(RND)
    ang = math.sqrt((RND**2)/(3610**2))
    ang1 = math.sqrt(ang)
    RND_new = math.degrees(math.atan(ang1))
    #RND_new = (math.atan(ang1))
    RND_new_hold.append(RND_new)

print RND_new_hold
RND_new_arr = np.array(RND_new_hold)

plt.figure()
plt.plot(Sigbm_arr,RND_new_arr)
plt.xlabel('Sigbm value')
plt.ylabel('RND value (degrees)')
plt.show()
