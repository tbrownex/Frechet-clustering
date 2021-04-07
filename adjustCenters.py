import numpy as np
import calcCenterDistance
# Find the true center of the cluster. True center will have the smallest sum-squared distance to all the other points in the cluster
# Find this true center by adding noise to "startingCenter" and checking if the new center reduces that distance
def adjust(clusterCtrs, data, clusterAssignments):
    # For each clusterCtr, move it just a bit by adding some noise
    # if the new center has lower avg distance to all the points in the cluster, it becomes the new center
    for x in range(len(clusterCtrs)):
        bestDist=np.inf
        bestCtr=ctr=clusterCtrs[x]
        initDist=calcCenterDistance.calc(ctr, data)
        for _ in range(1000):
            d=calcCenterDistance.calc(ctr, data)
            if d < bestDist:
                bestDist=d
                bestCtr = ctr
            noise=np.random.normal(loc=0.0, scale=0.03, size=ctr.size)
            noise=np.reshape(noise, newshape=ctr.shape)
            ctr=bestCtr+noise
        print("cluster {} improvement: {:.1%}".format(x, (initDist-bestDist)/initDist))
        clusterCtrs[x]=bestCtr
    return clusterCtrs