import os
import math
from array import array
import array as arr
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


RND_array = []
for i in np.arange(0,4000,1):

    A = 0
    for i in np.arange(0,12,1):
        x = random.random()
        A = A + x
       
#print A
    RND  = (A-6)*5.236
    ang = math.sqrt((RND**2)/(3610**2))
    ang1 = math.sqrt(ang)
    RND_new = math.degrees(math.atan(ang1))
    RND_array.append(RND_new)
 
plt.hist(RND_array,40)
plt.xlabel("Output RND value (degrees)")
plt.show()
