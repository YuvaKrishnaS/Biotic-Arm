from cvzone import HandTrackingModule
from cvzone.SerialModule import SerialObject
import cv2


cap = cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector(maxHands=1, detectionCon=1)
mySerial = SerialObject("COM10")
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        if fingers == [1,1,1,1,1]:
            mySerial.sendData([150])           
        else:
            mySerial.sendData([0])  

    cv2.imshow("Image",img)
    cv2.waitKey(1)