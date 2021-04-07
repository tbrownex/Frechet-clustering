import numpy as np

def getCenter(data):
    '''Return the center of a cluster
    This is done by getting the mean of each feature (dimension) among all the points'''
    npData=np.array(data)
    # First dimension is the entity to which the data applies, e.g. a person
    # Middle dimension are the points in time for that entity
    # Last dimension are the features of the point
    X,Y,Z=[],[],[]
    numEntities=len(npData)
    numFeatures=npData.shape[-1]
    featureVals=[[] for x in range(numFeatures)]   # This will hold the values of a feature across all entities and points
    for x in range(numEntities):
        tmp=npData[x]
        for y in range(numFeatures):
            vals=tmp[:,y]
            featureVals[y].append(vals)
    '''for x in range(len(npData)):
        tmp=npData[x][:,1]
        Y.append(tmp)
    for x in range(len(npData)):
        tmp=npData[x][:,2]
        Z.append(tmp)'''
    npList=[]
    for x in range(numFeatures):
        vals=featureVals[x]
        tmp=np.array(vals).T.mean(axis=1)
        npList.append(tmp)
    npList = [np.reshape(x, [-1,1]) for x in npList]
    return np.concatenate(npList, axis=1)