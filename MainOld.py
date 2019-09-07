import time

import cv2 as cv
import numpy as np

import analyse_image as analyse
import algorithms as alg

mapToPath = []
start = []
goal = []
startNode = []
goalNode = []

checkedNodes = []
finalPath = []

# Size of each square in the grid
squareHeight = 5
squareWidth = 5

# Reads the Image and creates a path through it
image = cv.imread("testMaps/test7.png")
mapToPath, start, goal = analyse.readImage.convertImageToGrid(image, squareWidth, squareHeight)
print("Image Analysed")
np.savetxt("mapToPath.csv", mapToPath, delimiter=",", fmt="%s", header="header")

start_time = time.time()

# checkedNodes, finalPath = dijkstra.dijkstraSearch(image, mapToPath, start, goal, squareHeight, squareWidth)
# checkedNodes, finalPath = astar.astarSearch(image, mapToPath, start, goal, squareHeight, squareWidth)
# checkedNodes, finalPath = depthFirst.depthFirstSearch(image, mapToPath, start, goal)
# checkedNodes, finalPath = dijkstraModification1.dijkstraSearch(image, mapToPath, start, goal, squareHeight, squareWidth)
# checkedNodes, finalPath = astarModification1Less.astarSearch(image, mapToPath, start, goal, squareHeight, squareWidth)
checkedNodes, finalPath = alg.astarModification1Greater.astarSearch(image, mapToPath, start, goal, squareHeight, squareWidth)

print("%s s" % (str(round((time.time() - start_time), 6))))

num = 0
# for i in range(0, 10):
#     start_time = time.time()
#     checkedNodes, finalPath = dijkstraModification1.dijkstraSearch(image, mapToPath, start, goal, squareHeight, squareWidth)
#     checkedNodes, finalPath = astarModification1Less.astarSearch(image, mapToPath, start, goal, squareHeight, squareWidth)
#     checkedNodes, finalPath = astarModification1Greater.astarSearch(image, mapToPath, start, goal, squareHeight, squareWidth)

#     num = num + round((time.time() - start_time),6)

alg.showAlgo.drawAlgo(checkedNodes, finalPath, image, squareWidth, squareHeight)
print(round((num/10), 6))
print("Number of Nodes Checked = ", (len(checkedNodes)))
print("Number of Nodes in Final Path = ", (len(finalPath)))
