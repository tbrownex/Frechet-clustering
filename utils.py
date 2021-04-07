import similaritymeasures
import itertools

def getDistance(a, b):
    ''' Given two points, compute the Frechet distance between them '''
    return similaritymeasures.frechet_dist(a, b)

def getComboDistance(data, points):
    ''' Given a set of points, compute the total distance (squared) between all of them '''
    totalDistance=0
    for a,b in itertools.combinations(points,2):
        dist=getDistance(data[a], data[b])
        totalDistance+=dist*dist
    return totalDistance