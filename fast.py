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

            cityArray.append(cityArray[0])

            #finalList is the matrix form of the graph
            tourLength = 0

            for i in range(len(cityArray)-2):
                tourLength += distance(xArray[i],xArray[i+1],yArray[i],yArray[i+1])

            tourLength += distance(xArray[(len(cityArray)-2)],xArray[0],yArray[(len(cityArray)-2)],yArray[0])

            print tourLength

            outputFile.write("%s\n" % tourLength)

            for item in cityArray:
                outputFile.write("%s\n" % item)



def distance(x1, x2, y1, y2):
    distance = 0
    distance = math.sqrt(math.pow((x1 - x2),2) + math.pow((y1 - y2),2))
    return int(distance)

