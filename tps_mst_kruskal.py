#JUAN DACCARETT
#kruskals to find mst for tps Algorithm

import math
import os
import sys
import time



class edge:
    u = None #from vertex (first)
    v = None #to vertex (second)
    d = 0    #distance between the vertices
    def __init__(self, u, v, d):
        self.u = u
        self.v = v
        self.d = d



def distanceToCity(city_one, city_two):
    dist_x = city_one['x'] - city_two['x']
    dist_y = city_one['y'] - city_two['y']
    dist_xSq = math.pow(dist_x, 2)
    dist_ySq = math.pow(dist_y, 2)
    return int (round(math.sqrt(dist_xSq + dist_ySq)))


def minPop(priorityQueue):
    minU = priorityQueue[0]
    priorityQueue.remove(priorityQueue[0])
    return minU


def decrementKey(priorityQueue, cost):
    for i in range(len(priorityQueue)):
        for j in range(len(priorityQueue)):
            if cost[priorityQueue[i]] < cost[priorityQueue[j]]:
                priorityQueue[i] = priorityQueue[i] + priorityQueue[j]
                priorityQueue[j] = priorityQueue[i] - priorityQueue[j]
                priorityQueue[i] = priorityQueue[i] - priorityQueue[j]




def kruskalsAlg(adjMatrix):
    edges = []
    for i in range(0, len(adjMatrix) - 1):
        for j in range(i + 1, len(adjMatrix)):
            e = edge(i, j, adjMatrix[i][j])
            edges.append(e)
    edges.sort(key=lambda x: x.d)

    prev = [None for x in range(len(adjMatrix))]
    vstd = []
    for e in edges:
        if (not (e.v in vstd)):
            vstd.append(e.v)
            prev[e.v] = e.u
    return prev

#dfs implementation with | stack
def dfs(adjList):
    visited = []
    stack = []
    stack.append(0)

    while(len(stack) > 0):
        u = stack[len(stack) - 1]
        stack.remove(stack[len(stack) - 1])
        if not (u in visited):
            visited.append(u)
            auxStack = []
            for eachAdj in sorted(adjList[u].items(), key=lambda x: x[1], reverse=True):
                v = eachAdj[0]
                if not (v in visited):
                    auxStack.append(v)
            while len(auxStack) > 0:
                v = auxStack[0]
                stack.append(v)
                auxStack.remove(v)

    return visited


def mstToAdjList(adjMatrix, mst):
    adjList = {}
    for i in range(0, len(adjMatrix)):
        adjVisited = {}
        for j in range(0, len(mst)):
            if i == mst[j]:
                adjVisited[j] = adjMatrix[i][j]
        adjList[i] = adjVisited
    return adjList


def mst_kruskals(textfile):

    #command line input
    #if (len(sys.argv) != 2):
     #   print("Error only one argument is needed")
      #  quit()
    #else:
     #   inFil = sys.argv[1]
      #  if not(os.path.isfile(inFil)):
       #     print("Error file not found")
        #    quit()

    #open files
    #base = os.path.basename(inFil)
    inFil = open(textfile, 'r')
    outFil = open(textfile+ '.tour', 'w')

    #put the cities into a list
    cities = []
    for eachLine in inFil:
        eachCity = eachLine.split()
        thisCity = {'id':int(eachCity[0]), 'x':int(eachCity[1]), 'y':int(eachCity[2])}
        cities.append(thisCity)


    #connect every city to every other city (initialize adjacency matrix for the graph)
    adjMatrix = [[0 for x in range(len(cities))] for y in range(len(cities))]
    for i in range(0, len(cities)):
        for j in range(0, len(cities)):
            for j in range(i + 1, len(cities)):
                ij = distanceToCity(cities[i], cities[j])
                adjMatrix[i][j] = ij
                adjMatrix[j][i] = ij



    #create MST using PRIMS algorithm
    mst = kruskalsAlg(adjMatrix)


    # create adjacency list from minimum spanning tree made fro prims algorithm
    adjList = mstToAdjList(adjMatrix, mst)

    # the order of the depth first search
    discovered = dfs(adjList)


    #distance calculator from city to city
    totaldistance = 0
    iterCities = iter(discovered)
    prevCity = cities[discovered[0]]
    next(iterCities) #dont count first city

    for eachItem in iterCities:
        eachCity = cities[eachItem]
        addDistance = distanceToCity(eachCity, prevCity)
        totaldistance = totaldistance + addDistance
        prevCity = eachCity

    #return distance of first -> last city
    addDistance = distanceToCity(prevCity, cities[discovered[0]])
    totaldistance = totaldistance + addDistance

    #write files
    outFil.write(str(totaldistance) + '\n')
    iterCities = iter(discovered)
    for eachCity in iterCities:
        outFil.write(str(eachCity) + '\n')

    inFil.close()
    outFil.close()


start = time.clock()
mst_kruskals('tsp_example_3.txt')
elapsed_time = (time.clock() - start)
print('Time:', elapsed_time)