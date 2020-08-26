import os
import math
from array import array
import array as arr
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import csv

#Read in the collimator profile text file
file = ("/user/pmehta/skli_warwick_opticlib_analyser_v1.0/B1coll_prof.txt")
file_data = np.loadtxt(file, usecols=(0,1))
#print file_data
ang  = np.array(file_data[:,0])
#print ang 

collval = np.array(file_data[:,1])
#print collval

cdfVecHold = 0
cdfVec = []
for x in collval:
    cdfVecHold += x
    cdfVec.append(cdfVecHold)

#print cdfVec

#Find minimum and maximum value    
cdf_vec_min = min(cdfVec)
cdf_vec_max = max(cdfVec)
#print cdf_vec_min
#print cdf_vec_max

#Find the minimum and maximum value
cdf_vec_value_norm = 0
cdf_vec_norm = []

#Do Min-Max normalisation to get CDF values between 0 and 1
for x in cdfVec:
    cdf_vec_value_norm  = (x - cdf_vec_min) / (cdf_vec_max - cdf_vec_min)
    cdf_vec_norm.append(cdf_vec_value_norm)

#final_cdf_vec = [1.00]
#ext_cdf_vec= cdf_vec_norm + final_cdf_vec


#print cdf_vec_norm
#Find the minimum value of the data, generate random number between 0 and 1, take this away from normalised CDF values and find the minimum
minval = 0
#rdummy = random.random()
#print rdummy
#rdummy = 0.52763
RND = []
RND_new_hold = []


A_array =[]
for x in np.arange(0,1,0.001):
    A_array.append(x) 

for i in A_array:
    vectorMin = []
    for j in cdf_vec_norm:
        minval = abs(j - i)
        vectorMin.append(minval)
        vectorMin_arr = np.array(vectorMin)
#    print vectorMin_arr
            

    minloc =  np.where(vectorMin_arr == vectorMin_arr.min()) #Find the angle relating to the minimum
    #print minloc
    RND = ang[minloc]
    angle = math.sqrt((RND**2)/(3610**2))
    angle1 = math.sqrt(angle)
    RND_new = math.degrees(math.atan(angle1))
    #print RND_new
    #RND_new_hold.append(RND_new)
    #print RND_new    
    RND_new_hold.append(RND_new)
#print RND_new_hold
    

plt.plot(A_array, RND_new_hold)
plt.xlabel("Value of input random number between 0 and 1")
plt.ylabel("Value of output RND value (degrees)")
plt.title("Input random number (rdummy) vs output RND value for Warwick collimator rngausyoo.F")
plt.show()
