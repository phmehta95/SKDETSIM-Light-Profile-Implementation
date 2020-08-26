import os
import math
from array import array
import array as arr
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import csv


RND_array = []
random_array = []
random_array_2 = []

for x in np.arange(0,40000,1):
    z1 = random.random()
    random_array.append(z1)

#plt.hist(random_array,40)
#plt.show()


for x in np.arange(0,40000,1):
    y1 = random.random()
    y2 = random.random()
    
    
for i in np.arange(0,40000,1):

    x1 = random.random()
    x2 = random.random()

    Sigma = 20
    RND1 = x1*Sigma - (Sigma/2)
    RND2 = x2*Sigma - (Sigma/2)
    RND = abs((RND1+RND2)/2)

    random_array_2.append(RND1)
    
#plt.hist(random_array_2,40)
#plt.show()



#    RND_hold = []
#    Sigma = 20


#    RND1 = x1*Sigma - (Sigma/2)
#    RND2 = x2*Sigma - (Sigma/2)
#    RND = abs((RND1+RND2)/2)






#    RND_hold.append(RND)
    

    ang = math.sqrt((x1**2)/(3610**2))
    ang1 = math.sqrt(ang)
    RND_new = math.degrees(math.atan(ang1))
#    RND_array.append(RND_new)
    RND_array.append(RND_new)

plt.hist(RND_array,400)
plt.xlabel("Output RND value (degrees)")
plt.show()
