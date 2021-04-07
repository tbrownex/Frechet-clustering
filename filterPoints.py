import utils

def filter(data, center):
    ''' Remove two sets of points:
       - most distant from the center
       - closest to the center
    Neither one will make good cluster centers '''
    distances=[]
    for idx in range(len(data)):
        d=utils.getDistance(center, data[idx])
        distances.append((idx,d))
    distances.sort(key=lambda n: n[1])
    # remove closest 10%
    closest=int(len(data)*.1)
    distances=distances[closest:]
    # remove furthest 10%
    furthest=int(len(distances)*.9)
    distances=distances[:furthest]
    return distances