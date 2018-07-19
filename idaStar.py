import cv2 as cv
import numpy as np

def idaStarSearch (img, mapToPath, start, goal, squareHeight, squareWidth):
    path = []
    frontier = []
    bound = 0
    
    node
    g = 0
    f = 0
    h = []
    cost = []
    is_goal = []
    successors = []
    ida_star = []
    
    
    


    while(bound >= 0):
        frontier = sorted(frontier, key=lambda frontier: frontier[2])
        currentNode = frontier[0]
        del frontier[0]

        cy,cx,cfScore = currentNode
        
        if (cy == gy and cx == gx):
            return path


        

        
