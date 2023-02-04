from initialize import *

myDrone = initializeTello()
pid = [0.5, 0.5, 0]
pError = 0
startCounter = 0
w, h = 360, 240

while True :

    if startCounter == 0:
        myDrone.takeoff()
        startCounter = 1
    img = telloGetFrame(myDrone, w, h)
    img, info = findFace(img)
    #print(info[0][0])
    pError = trackFace(myDrone, info, w, pid, pError)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        myDrone.land()
        break