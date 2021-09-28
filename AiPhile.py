import cv2 as cv 
# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (255,0,0)
RED = (0,0,255)
CYAN = (255,255,0)
YELLOW =(0,255,255)
MAGENTA = (255,0,255)
GRAY = (128,128,128)
GREEN = (0,255,0)
PURPLE = (128,0,128)
ORANGE = (0,165,255)
PINK = (147,20,255)

def textBG(img, text, position, fonts ,scaling=1, color=(0,255,0), thickness=1, padding=3):
    img_h, img_w = img.shape[:2]
    x, y = position
    (w, h ), p= cv.getTextSize(text, fonts, scaling, thickness)
    print(w, h)
    cv.rectangle(img, (x-p, y+p), (x+w+p, y-h-p), (255, 0,234), -1)
    
    cv.putText(img, text, position,fonts, scaling,  color, thickness)

def textBGoutline(img, text, position, fonts ,scaling=1, color=(0,255,0), thickness=1, padding=3):
    img_h, img_w = img.shape[:2]
    x, y = position
    (w, h ), p= cv.getTextSize(text, fonts, scaling, thickness)
    print(w, h)
    cv.rectangle(img, (x-p, y+p), (x+w+p, y-h-p), (255, 0,234), -1)
    cv.rectangle(img, (x-p, y+p), (x+w+p, y-h-p), (255, 255,0), 2, cv.LINE_AA)
    
    cv.putText(img, text, position,fonts, scaling,  color, thickness, cv.LINE_AA)