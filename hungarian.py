
#start code
import numpy as np
import math
import copy
import time

def hungarian(tsp_prob):

    #take the problem and change it to matrix form
    name = tsp_prob + '.txt'
    name2 = name + '.tour'
    with open(name, "r") as f:
        with open(name2, 'w') as outputFile:     
            cityArray = []
            xArray = []
            yArray = []

            for line in f:
                line = line.split()
                cityArray.append(int(line[0]))
                xArray.append(int(line[1]))
                yArray.append(int(line[2]))

            finalList = []
            for i in range(len(cityArray)):
                distanceArray = []
                distanceArray.extend([None])
                for x in range(i):
                    distanceArray.extend([None])
                
                for j in range(i, len(cityArray)-1):
                    #input the distance using the helper function
                    distanceArray.extend([distance(xArray[i],xArray[j+1],yArray[i],yArray[j+1])])
                
                finalList.append(list(distanceArray))
            
            #fill in other half of the array by copying it     
            for i in range(len(cityArray)):
                for j in range(len(cityArray)-1):
                    finalList[j+1][i] = finalList[i][j+1]

            #copy the matrix
            destinationList = copy.deepcopy(finalList)

            #finalList is the matrix form of the graph
            #now go through steps 1 - 5 (hungarian method)
            tourLength = 0
            tourArray = []

            for i in range(len(destinationList)):
                #step 1: find the minimum value of each row and subtract it from every value in the row
                for i in range(len(finalList)):
                    minval = find_minimumrow(finalList,i)
                    for j in range(len(finalList)):
                        if finalList[i][j] is not None:
                            finalList[i][j] -= minval 

                #step 2: find the minimum value of each column and subtract it from every value in the row
                for i in range(len(finalList)):
                    minval = find_minimumcol(finalList,i)
                    for j in range(len(finalList)):
                        if finalList[j][i] is not None:
                            finalList[j][i] -= minval

                #step 3: calculate penalties for each zero
                penaltyArray = []
                for i in range(len(finalList)):
                    for j in range(len(finalList)):
                        if finalList[i][j] == 0:
                            minrow = find_minimumrow2(finalList,i) #row penalty
                            mincol = find_minimumcol2(finalList,i) #column penalty
                            penalty = []
                            penalty.extend([i])
                            penalty.extend([j])
                            penalty.extend([minrow + mincol])
                            penaltyArray.append(list(penalty))

                #step 4: take the highest penalty, add it to travel list, and add the distance to the tourLength
                maxPenalty = 0
                startLoc = -1
                endLoc = -1

                for i in range(len(penaltyArray)):
                    trip1 = []
                    if penaltyArray[i][2] >= maxPenalty:
                        maxPenalty = penaltyArray[i][2]
                        startLoc = penaltyArray[i][0]
                        endLoc = penaltyArray[i][1]

                tourLength += destinationList[startLoc][endLoc]
                trip1.extend([startLoc])
                trip1.extend([endLoc])
                tourArray.append(list(trip1))

                #step 5: recalculate matrix, without the row and column of the cities that were picked
                for i in range(len(destinationList)):
                    if i == startLoc:
                        for j in range(len(destinationList)):
                            finalList[i][j] = None
                for i in range(len(destinationList)):
                    if i == endLoc:
                        for j in range(len(destinationList)):
                            finalList[j][i] = None
                finalList[endLoc][startLoc] = None

            #this end result may cause 2 or more cycles to form
            #in order to get to the solution, we have to connect these various cycles

            #step 1: define path, see if cycles exist
            finalTour = []
            cycle = []
            countList = [0] * len(tourArray)
            finalTour.extend([tourArray[0][0]])
            finalTour.extend([tourArray[0][1]])
            countList[0] = 1
            counter = 1
            
            for i in range(len(tourArray)-1):
                for j in range(len(tourArray)):
                    if (finalTour[counter] == tourArray[j][0] and next((i for i, x in enumerate(countList) if x==0), None) != None):
                        for k in range(len(finalTour)):
                            if tourArray[j][1] == finalTour[k]:
                                cycle.extend([tourArray[j][0]])
                                cycle.extend([tourArray[j][1]])
                                finalTour.extend([tourArray[j][1]])
                                countList[j] = 1
                                if next((i for i, x in enumerate(countList) if x==0), None) == None:
                                    break
                                temp = next((i for i, x in enumerate(countList) if x==0), None)
                                finalTour.extend([tourArray[temp][0]])
                                finalTour.extend([tourArray[temp][1]])
                                countList[temp] = 1
                                counter += 3                              
                                break
                            
                        else:
                            finalTour.extend([tourArray[j][1]])
                            countList[j] = 1
                            counter += 1
                            break
                        break
            
            #add to tour length, subtract from tour length if needed, complete finalTour
            temp = 0

            for i in range(0,len(cycle),2):
                if i == (len(cycle)-2):
                    tourLength += destinationList[(cycle[i])][(cycle[1])]
                    tourLength -= destinationList[(cycle[i])][(cycle[i+1])]
                else:
                    tourLength += destinationList[(cycle[i])][(cycle[i+3])]
                    tourLength -= destinationList[(cycle[i])][(cycle[i+1])]

            seen = {}
            finalFinal = [seen.setdefault(x, x) for x in finalTour if x not in seen]

            if finalFinal[0] != finalFinal[len(finalFinal)-1]:
                finalFinal.extend([finalFinal[0]])

            finalFinal.insert(0,tourLength)

            #print matrix form to output file for verification
            for item in finalFinal:
                outputFile.write("%s\n" % item)
             
def distance(x1, x2, y1, y2):
    distance = 0
    distance = math.sqrt(math.pow((x1 - x2),2) + math.pow((y1 - y2),2))
    return int(distance)


def find_minimumrow(thelist,x):
    try:
        return min(value for value in thelist[x] if value is not None)
    except ValueError:
        return 0

def find_minimumrow2(thelist,x):
    try:
        return min(value for value in thelist[x] if (value is not None and value is not 0))
    except ValueError:
        return 0


def find_minimumcol(thelist,x):
    try:
        return min(value[x] for value in thelist if value[x] is not None)
    except ValueError:
        return 0

def find_minimumcol2(thelist,x):
    try:
        return min(value[x] for value in thelist if (value[x] is not None and value[x] is not 0))
    except ValueError:
        return 0
