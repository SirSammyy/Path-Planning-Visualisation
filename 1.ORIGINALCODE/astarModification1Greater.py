import cv2 as cv
import numpy as np

def astarSearch (img, mapToPath, start, goal, squareHeight, squareWidth):    
    #Image Size, Channels is uneeded but may have a use later
    height, width, channels = img.shape
    #Amount of Squares across and down
    totalAmountOfSquaresHeight = int(height / squareHeight)
    totalAmountOfSquaresWidth = int(width / squareWidth)
    #List of the final route, returned upon function completion
    finalPath = []
    #List of all Nodes that have been checked, returned upon function completion
    checkedNodes = [] 
    #List of all nodes to be checked, set as locY,locX,fScore
    openSet = []
    
    #Initialises cameFrom, gScore and fScore as 2D Lists that match the 2D List of mapToPath
    cameFrom = [[0 for y in range(totalAmountOfSquaresHeight)] for x in range(totalAmountOfSquaresWidth)]
    gScore = [[0 for y in range(totalAmountOfSquaresHeight)] for x in range(totalAmountOfSquaresWidth)]
    fScore = [[0 for y in range(totalAmountOfSquaresHeight)] for x in range(totalAmountOfSquaresWidth)]
    
    #Takes the Y and X coordinates for the start and goal square, and assigns them to specific variables
    sy, sx = start
    gy, gx = goal
    #Sets the gScore of the start node, which is 0
    gScore[sy][sx] = 0
    #Sets the fScore of the start node to the goal node
    fScore[sy][sx] = manhattan_distance(start, goal)
    
    #Adds start to open set, with an fScore of 0
    openSet.append([sy, sx, (fScore[sy][sx])])    

    #Sets a var to be used on the while loop to the length of the checkedNodes List
    totalOfOpenSet = len(openSet)
                       
    #Loops until totalOfOpenSet is equal to 0                    
    while(totalOfOpenSet != 0):
        #Sorts openSet by lowest fScore first
        openSet = sorted(openSet, key=lambda openSet: openSet[2])
        #Sets current to be the first item in openSet
        current = openSet[0]
        #Removes the first item from openSet, this is currently current
        del openSet[0]
        
        #Takes the y, x and fScore of current
        cy, cx, cfScore = current  

        #If current nodes location is equal to the goals then goal has been found
        if (cy == gy and cx == gx):
            #Adds goal node to checked nodes as a tuple
            checkedNodes.append([gy,gx])
            finalPath = reconstruct_path(cameFrom, current, start)
            return checkedNodes, finalPath
        
        #Adds cy and cx to checkedNodes as a tuple
        checkedNodes.append([cy,cx])
        
        #sets cgScore to be the gScore of the current Node
        cgScore = gScore[cy][cx]
        
        #Finds the neighbours and totalNeighbours of current
        neighbours, totalNeighbours = findNeighbours(cy,cx,totalAmountOfSquaresHeight,totalAmountOfSquaresWidth,gy,gx)
        
        #Loops based on the amount of Neighbours the currentNode has
        for i in range(0, totalNeighbours):
            
            #Sets ny and nx to be equal to the location of neighbours y and x
            ny, nx = neighbours[i]
            tentative_gScore = cgScore + 1
            ngScore = gScore[ny][nx]
            #if a neighbour is in checkedNodes continue to next iteration of loop
            if ([ny,nx] in checkedNodes):
                if (tentative_gScore >= ngScore):
                    continue
                
                cameFrom[ny][nx] = [cy,cx]
                
                continue

            #if the neighbour is equal to 1(wall) in mapToPath, if so continue to next iteration of loop
            if ((mapToPath[ny][nx]) == 1):
                #Adds wall node to checkedNodes so it isnt checked again
                checkedNodes.append([ny,nx])
                continue
            
            #Finds the fScore of the neighbour and sets it to nfScore
            nfScore = manhattan_distance([ny,nx],goal)
            if ([ny,nx,nfScore] not in openSet):
                #Adds neighbour to openSet, adds coords and fScore
                openSet.append([ny, nx, nfScore])
                gScore[ny][nx] = tentative_gScore
                cameFrom[ny][nx] = [cy,cx]
                continue
            
            
            if (tentative_gScore >= ngScore):
                continue

            cameFrom[ny][nx] = [cy,cx]
            gScore[ny][nx] = tentative_gScore
            fScore[ny][nx] = gScore[ny][nx] + manhattan_distance(neighbours[i], goal)     
    return (checkedNodes, finalRoute)

#Find and returns the neighbours of the current location
def findNeighbours(y,x,totalAmountOfSquaresHeight,totalAmountOfSquaresWidth,gy,gx):
    totalNeighbours = 0
    neighbours = []
    th = totalAmountOfSquaresHeight - 1
    tw = totalAmountOfSquaresWidth - 1
    if(abs(x-gx) >= abs(y-gy)):
        #Add X First
        if(x == 0):
            neighbours.append([y,x+1])
            totalNeighbours  += 1
        if(x == tw):
            neighbours.append([y,x-1])
            totalNeighbours  += 1
        if(x != 0 and x != tw):
            neighbours.append([y,x+1])
            neighbours.append([y,x-1])
            totalNeighbours  += 2
        if(y == 0):
            neighbours.append([y+1,x])
            totalNeighbours  += 1
        if(y == th):
            neighbours.append([y-1,x])
            totalNeighbours  += 1
        if(y != 0 and y!= th):
            neighbours.append([y+1,x])
            neighbours.append([y-1,x])
            totalNeighbours  += 2
        
    if(abs(y-gy) > abs(x-gx)):
        #Add Y First
        if(y == 0):
            neighbours.append([y+1,x])
            totalNeighbours  += 1
        if(y == th):
            neighbours.append([y-1,x])
            totalNeighbours  += 1
        if(y != 0 and y!= th):
            neighbours.append([y+1,x])
            neighbours.append([y-1,x])
            totalNeighbours  += 2
        if(x == 0):
            neighbours.append([y,x+1])
            totalNeighbours  += 1
        if(x == tw):
            neighbours.append([y,x-1])
            totalNeighbours  += 1
        if(x != 0 and x != tw):
            neighbours.append([y,x+1])
            neighbours.append([y,x-1])
            totalNeighbours  += 2
            
    
    return neighbours, totalNeighbours

def manhattan_distance(start, end):
    sy, sx = start
    ey, ex = end
    dx = abs(sx - ex)
    dy = abs(sy - ey)
    return 1 *(dx+dy)

def reconstruct_path(cameFrom, current, start):
    startB = False
    total_path = []
    cy, cx, score = current    
    sy, sx = start
    counter = 0
    while (startB == False):
        total_path.append([cy,cx])
        if (cy == sy and cx == sx):
            startB = True
            return total_path
        newCurrent = (cameFrom[cy][cx])
        cy, cx = newCurrent
    return


















    
