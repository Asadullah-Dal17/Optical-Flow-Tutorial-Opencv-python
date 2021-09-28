import cv2 as cv 
import numpy as np 
import time
import AiPhile as ap


camera = cv.VideoCapture(0)
# getting old frame 
condition =False
old_gray = cv.cvtColor(camera.read()[1], cv.COLOR_BGR2GRAY)
cv.imshow('old_gray', old_gray)
start_time = time.time()
frame_counter = 0
fonts =cv.FONT_HERSHEY_SIMPLEX
# optical_flow parmamters 
parmas_dict = dict(winSize=(20, 20), maxLevel=4, criteria=(cv.TERM_CRITERIA_EPS| cv.TermCriteria_COUNT, 10, 0.01))
def pointSelector(event, x, y, flags, params):

    global point, condition, old_point
    if event ==cv.EVENT_LBUTTONDOWN:
        point = np.array([x, y]).astype(int)
        condition =True
        old_point = np.array([[x, y]], dtype=np.float32)

cv.namedWindow('frame')
cv.setMouseCallback('frame', pointSelector)
old_points = np.array([[]])
while True:
    frame_counter +=1
    ret, frame = camera.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if condition:
        cv.circle(frame, point,5, ap.ORANGE, -1)
        cv.circle(frame, point, 7, ap.INDIGO, 2)
        new_point,status, error = cv.calcOpticalFlowPyrLK(old_gray, gray_frame, old_point,None, **parmas_dict)

        old_point = new_point
        p = new_point.astype(int)
        x, y = p.ravel()
        print(x, y)
        cv.circle(frame, (x,y), 4, ap.GREEN, -1)
        cv.circle(frame,(x,y), 7, ap.BLACK, 2)
        
    fps = frame_counter/(time.time() - start_time)
    ap.textBGoutline(frame, f'FPS: {round(fps,1)}', (30, 40), fonts, scaling= 0.5, thickness=1)
    cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if key ==ord('q'):
        break

cv.destroyAllWindows()
camera.release()