import numpy as np

import utils

def getNearestNeighbor(data, cfg):
    ''' Return a dictionary with the closest neighbor of each time series '''
    d={}
    for a in range(len(data)):
        shortest=np.inf
        neighbor=None
        for b in range(len(data)):
            if a==b:
                pass
            else:
                dist=utils.getDistance(data[a], data[b])
                if dist<shortest:
                    shortest=dist
                    d[a]=b
    return d