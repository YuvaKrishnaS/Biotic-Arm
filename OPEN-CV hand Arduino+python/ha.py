from cvzone import HandTrackingModule
from cvzone.SerialModule import SerialObject
import cv2

cap = cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector(maxHands=1, detectionCon=1)
mySerial = SerialObject("COM13")

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if lmList:
        fingers = detector.fingersUp()
        servo_values = [0] * 5

        # Map finger gestures to servo positions
        if fingers[0] == 1:  # Thumb
            servo_values[0] = 90
        if fingers[1] == 1:  # Index finger
            servo_values[1] = 90
        if fingers[2] == 1:  # Middle finger
            servo_values[2] = 90
        if fingers[3] == 1:  # Ring finger
            servo_values[3] = 90
        if fingers[4] == 1:  # Pinky finger
            servo_values[4] = 90

        mySerial.sendData(servo_values)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
