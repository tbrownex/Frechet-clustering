import numpy as np

import utils

def assign(data, clusterCtrs):
    # Assign each point to one of the clusters
    clusterAssignments={}
    for idx in range(len(data)):
        shortestDist=np.inf
        bestCluster=None
        for n in range(len(clusterCtrs)):
            dist=utils.getDistance(clusterCtrs[n], data[idx])
            if dist<shortestDist:
                bestCluster=n
                shortestDist=dist
        clusterAssignments[idx]=bestCluster
    return clusterAssignments