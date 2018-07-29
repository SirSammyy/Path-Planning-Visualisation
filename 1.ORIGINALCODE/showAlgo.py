import cv2 as cv

def drawAlgo(checkedNodes, finalPath, img, squareWidth, squareHeight):
    totalOfcheckedNodes = len(checkedNodes)
    totalOffinalPath = len(finalPath)
    finalPath.reverse()
    print("Searching for Goal")
    
    for i in range(0, totalOfcheckedNodes):
        y, x = checkedNodes[i]
        cv.rectangle(img, ((x*squareWidth), (y*squareHeight)), ((x*squareWidth) + squareWidth, (y*squareHeight) + squareHeight), (255, 0, 0), 1)
        cv.imshow("Window", img)
        cv.waitKey(1)

    print("Found Goal")
    
    for i in range(0, totalOffinalPath):
        y, x = finalPath[i]
        cv.rectangle(img, ((x*squareWidth), (y*squareHeight)), ((x*squareWidth) + squareWidth, (y*squareHeight) + squareHeight), (255, 255, 0), thickness=-1)
        cv.imshow("Window", img)
        cv.waitKey(1)

    print("Path Completed")

    cv.imwrite("testMaps/finalPaths/test10AstarModification1Greater.png", img)
