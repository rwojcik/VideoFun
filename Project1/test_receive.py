import numpy as np
import cv2

# trzeba odpalic strumieniowanie w VLC na 127.0.0.1:5004
cap = cv2.VideoCapture('rtp://127.0.0.1:5004/')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
