import random
import numpy as np

# Function to create 10 random target positions
def randpos():
    theta = [] # angle array
    r = []     # distance array
    
    for i in range(5):
        angle = random.randrange(5,360)      # generate random number between 5 and 360
        angle = np.deg2rad(angle)            # convert degree to radian

        distance = random.randrange(10,100) # generate random nmber between 10 and 100
        
        # add value into array
        theta.append(angle)                  
        r.append(distance)                   

        # sort data - ascending
        theta.sort()
        r.sort()
    
    return theta, r
