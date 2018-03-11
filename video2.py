import numpy as np
import cv2

cap = cv2.VideoCapture(r"out.mp4")
while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if(cv2.waitKey(27) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyWindows()

cap.release()
cv2.destroyAllWindows()
