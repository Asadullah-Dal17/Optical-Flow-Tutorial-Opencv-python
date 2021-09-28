import cv2 as cv 
import numpy as np 
import time
import AiPhile as ap


camera = cv.VideoCapture(0)
# getting old frame 
old_gray = cv.cvtColor(camera.read()[1], cv.COLOR_BGR2GRAY)
cv.imshow('old_gray', old_gray)
# cv.waitKey(0)
start_time = time.time()
frame_counter = 0
fonts =cv.FONT_HERSHEY_SIMPLEX
# optical_flow parmamters 
def pointSelector(event, x, y, flags, params):

    global point, condition, old_point
    if event ==cv.EVENT_LBUTTONDOWN:
        point = np.array([x, y]).astype(int)
        condition =True
        old_point = np.array([[x, y]], dtype=np.float32)
while True:
    frame_counter +=1
    ret, frame = camera.read()

    fps = frame_counter/(time.time() - start_time)
    ap.textBGoutline(frame, f'FPS: {round(fps,1)}', (30, 40), fonts, scaling= 0.5, thickness=1)
    cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if key ==ord('q'):
        break

cv.destroyAllWindows()
camera.release()