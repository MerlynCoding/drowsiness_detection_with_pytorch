import cv2

from model import *

cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    cv2.imshow('CAMERA',frame)
    if cv2.waitKey(10) &0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
