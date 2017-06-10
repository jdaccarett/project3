#start code
import numpy as np
import math
import copy
import time

def fast(tsp_prob):

    #take the problem and change it to matrix form
    name = tsp_prob + '.txt'
    name2 = name + '.tour'
    with open(name, "r") as f:
        with open(name2, 'w') as outputFile:     #change this to tsp_example_1.txt.tour
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

            #finalList is the matrix form of the graph
            tourLength = 0
            tourArray = []

            tourLength += finalList[0][len(cityArray)-1]
            for i in range(len(cityArray)-1):
                tourLength += finalList[i][i+1]
                tourArray.extend([i])
            tourArray.extend([len(cityArray)-1])
            
            outputFile.write("%s\n" % tourLength)

            for item in tourArray:
                outputFile.write("%s\n" % item)



def distance(x1, x2, y1, y2):
    distance = 0
    distance = math.sqrt(math.pow((x1 - x2),2) + math.pow((y1 - y2),2))
    return int(distance)
