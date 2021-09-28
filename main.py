import cv2 as cv 
import numpy as np 
import time
import AiPhile as ap


camera = cv.VideoCapture(0)
start_time = time.time()
frame_counter = 0
fonts = cv.FONT_HERSHEY_PLAIN
fonts =cv.FONT_HERSHEY_SIMPLEX
while True:
    frame_counter +=1
    ret, frame = camera.read()

    # ap.textBG(frame, 'Computer Vision Test', (40, 40))
    ap.textBGoutline(frame, 'AiPhile', (90, 90), fonts, scaling= 2, thickness=4)
    cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if key ==ord('q'):
        break

cv.destroyAllWindows()
camera.release()