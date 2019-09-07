import cv2 as cv
import numpy as np
# OLD CODE, useful for analysing every pixel of an image, not needed for
# what I am doing, however is useful if you want a higher resolution grid
# IE 1 pixel is 1 square to travel, useful for mazes


def analyseSquare(image):
    # Counter for amount of empty pixels and the colour an empty pixel is
    empty = 0
    white = np.array([255, 255, 255])
    # Counter for amount of wall pixels and the colour a wall pixel is
    wall = 0
    black = np.array([0, 0, 0])
    # Counter for amount of danger pixels and the colour a danger pixel is
    danger = 0
    red = np.array([0, 0, 0])
    # Counter for amount of start pixels and the colour an start pixel is
    start = 0
    blue = np.array([128, 47, 47])
    # Counter for amount of goal pixels and the colour a goal pixel is
    goal = 0
    green = np.array([34, 177, 76])

    # Gets Image width and height, also gets colour channels
    height, width, channels = image.shape

    # First Loop, travels down the y axis on each iteration, takes image width to know when to stop
    for y in range(0, height):
        # Second Loop, travels across the x axis on each iteration, takes image height  to know when to stop
        for x in range(0, width):
            # Gets the RGB value of the current pixel
            px = image[x, y]
            # Uncomment to check colour of each pixel
            # print(px)
            # Checks the colour of the pixel and then does something depending on what it is
            if(px == white).all():
                empty = empty + 1
            if(px == black).all():
                return "wall"
            if(px == blue).all():
                return "start"
            if(px == green).all():
                return "goal"

    #         Uncomment for visual Benefit, looks COOL
    #         clone = image.copy()
    #         cv.rectangle(clone, (x, y), (x, y), (0, 255, 0), 2)
    #         cv.imshow("Window", clone)
    #         cv.waitKey(1)
    # Checks if the amount of empty pixels is equal to amount of pixels
    if(empty == (width*height)):
        return "empty"

    return "ERROR"
