import cv2 as cv
import numpy as np

def convertImageToGrid(img, squareWidth, squareHeight):
     
    #Image Size, Channels is uneeded but may have a use later
    height, width, channels = img.shape
    #Amount of Squares across and down
    totalAmountOfSquaresHeight = int(height / squareHeight)
    totalAmountOfSquaresWidth = int(width / squareWidth)    
    #Multi-dimensional list for storing all squares in, what is stored is dependant on what is detected at each square
    mapToPath = [[0 for y in range(totalAmountOfSquaresHeight)] for x in range(totalAmountOfSquaresWidth)]
    #List for storing all start squares, only the first is used
    start = []
    #List for storing all goal squares, only the first is used
    goal = []

    counterY = 0
    counterX = 0

    #First Loop, travels down the y axis on each iteration, takes image height to know when to stop, and increments by size of squares height 
    for y in range(0, height, squareHeight):
        #Second Loop, travels down the x axis on each iteration, takes image width to know when to stop, and increments by size of squares width 
        for x in range (0, width, squareWidth):
            clone = img.copy()
            #Crops Image at y and x adding how big the square is going to be
            crop_img = img[y:y + squareHeight, x:x +  squareWidth]
            #Find average colour of cropped image, and sticks into vars b g r
            avg_colour_per_row = np.average(crop_img, axis=0)
            avg_colour = np.average(avg_colour_per_row, axis=0)
            #OpenCV uses bgr not rgb
            b,g,r = avg_colour

            #Checks if the colour of the square is white, if it isnt 255,255,255 then it must have black in
            if(b == g == r and b == 255):
                mapToPath[counterY][counterX] = 0
            #Checks if average colour is black
            if(b == g == r and b != 255):
                mapToPath[counterY][counterX] = 1
            #checks if average colour is blue/start square
            if(b > g and b > r):
                mapToPath[counterY][counterX] = "start"
                start.append([counterY, counterX])
            #Checks if average colour is green/goal square
            if(g > b and g > r):
                mapToPath[counterY][counterX] = "goal"
                goal.append([counterY, counterX])     
        
            counterX = counterX + 1
        counterY = counterY + 1
        counterX = 0      
    
    start = start[int(len(start)/2)]
    goal = goal[int(len(goal)/2)]      
    return mapToPath, start, goal





