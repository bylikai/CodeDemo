from math import sqrt




def manhatten( rating1, rating2 ):
    """
    manhatten distance
    """
    distance = 0
    for key in rating2:
        if key in rating1:
            distance += abs(rating1[key]-rating2[key])
    return distance


def euclidean( rating1, rating2 ):
    """
    Euclidean Distance
    """
    distance = 0
    for key in rating2:
        if key in rating1:
            distance += pow( (rating1[key]-rating2[key]), 2 )
    
    distance = sqrt(distance)
    return distance


def minkowski( rating1, rating2, r ):
    """
    Minkowski Distance
    """
    distance = 0
    for key in rating2:
        if key in rating1:
            distance += pow( abs(rating1[key]-rating2[key]), r )
    
    distance = pow(distance, 1/r)
    return distance


def computerNearestNeighbor1(username, users):
    """
    computer username's nearest neighbor from users, use manhatten
    """
    distanceList = []
    for key in users:
        if key != username:
            distance = manhatten( users[username],  users[key] )
            distanceList.append( (distance, key) )

    #sort
    distanceList.sort()
    print(distanceList)

    #List[ (distance, username), (distance, username) ]
    return distanceList


def computerNearestNeighbor2(username, users):
    """
    computer username's nearest neighbor from users, use euclidean
    """
    distanceList = []
    for key in users:
        if key != username:
            distance = euclidean( users[username],  users[key] )
            distanceList.append( (distance, key) )

    #sort
    distanceList.sort()
    print(distanceList)

     #List[ (distance, username), (distance, username) ]
    return distanceList


def computerNearestNeighbor3(username, users, r ):
    """
    computer username's nearest neighbor from users, use minkowski
    """
    distanceList = []
    for key in users:
        if key != username:
            distance = minkowski( users[username],  users[key], r )
            distanceList.append( (distance, key) )

    #sort
    distanceList.sort()
    print(distanceList)
    
     #List[ (distance, username), (distance, username) ]
    return distanceList


def recommand1( username, users ):
    """
    recommand book from manhatten distance
    """
    #1) find nearest neighbor
    distanceList = computerNearestNeighbor1( username, users )
    nearestNeighborname = distanceList[0][1]

    #2) get the user information
    recommandationList = []

    ratingOfNeighbor = users[nearestNeighborname]
    ratingOfUsername = users[username]
    
    #3) record the book from nearest neighbor , which book does not include in current username's ratings
    for key in ratingOfNeighbor:
        if key not in ratingOfUsername:
            recommandationList.append( (ratingOfNeighbor[key], key) ) 

    print( recommandationList )

    #4) sort recommandationList for rating
    #sorted( recommandationList, reverse=True )
    #recommandationListSorted = sorted( recommandationList, key = lambda artistTuple:artistTuple[1], reverse=True )
    
    #print( recommandationListSorted)
    #return recommandationListSorted

    recommandationList.sort(reverse=True)
    print(recommandationList)

    return recommandationList
