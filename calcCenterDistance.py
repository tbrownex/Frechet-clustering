import numpy as np

import utils

def calc(center, cluster):
    ''' 
    'center' is a candidate for the cluster center
    'cluster' has all the points in the cluster
    The return value indicates how far all the points are from the candidate center
    ''' 
    distList=[]
    for c in range(len(cluster)):
        dist=utils.getDistance(center, cluster[c])
        distList.append(dist)
    return np.sqrt(sum(i*i for i in distList))