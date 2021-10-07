import cv2 as cv 
import numpy as np
import time 
import AiPhile


# point selector funciton, which select point on mouse clicks 
def pointSelector(event, x, y , flags, parmas):
    global point, condition, old_point
    if event == cv.EVENT_LBUTTONDOWN:
        # storing coordinte of mouse pointer on window
        point = (int(x), int(y))
        condition=True 
        print('pressd button')
        old_point = np.array([[x, y]], dtype=np.float32)

# creating new window for mouse event to monitor
cv.namedWindow('img')
# calling the function on window to monitor mouse events 
cv.setMouseCallback('img', pointSelector)

# parameter dict for optical flow function 
lk_params = dict(winSize=(10, 10), maxLevel=10, criteria=(cv.TERM_CRITERIA_EPS| cv.TERM_CRITERIA_COUNT, 10, 0.01))
cap = cv.VideoCapture(1)
_, frame = cap.read()
old_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

# frame counter 
frame_counter =0
# starting time here 
starting_time = time.time()
point=()
condition =False 
old_point= np.array([[]])
while True:
    # starting counter here 
    frame_counter +=1
    ret, frame = cap.read()

    # no frame then quite loop 
    if not ret:
        break 
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if condition:
        cv.circle(frame, point, 4, AiPhile.MAGENTA, -1)
        # calling the optical flow function 
        new_point, status, error = cv.calcOpticalFlowPyrLK(old_gray, gray_frame, old_point, None, **lk_params)
        old_point = new_point
        new_point= new_point.astype(int)
        x, y = new_point.ravel()
        cv.circle(frame, (x, y), 6, AiPhile.GREEN, 2)
    # calculating Frame per second
    fps = frame_counter /(time.time() - starting_time)
    # display fps on screen 
    AiPhile.textBGoutline(frame, f'FPS: {round(fps, 2)}', (40, 30), scaling=0.7)
    # show the frame on the screen 
    cv.imshow('img', frame)
    # copying the gray frame for next frame's old frame
    old_gray = gray_frame.copy()
    # define the key to quite the program 
    key = cv.waitKey(1)
    if key ==ord('q'):
        break
# close all the windows 
cv.destroyAllWindows()
# close the camera 
cap.release()