import numpy as np
import math
import cv2

#input hsvColor:[h,s,v], ranges between (0-180, 0-255, 0-255)
#and output true hsvColor:[h,s,v]
def get_right_V(hsvColor):
    h = float(hsvColor[0])
    s = float(hsvColor[1])
    s1 = float(hsvColor[1])/255
    v1 = float(hsvColor[2])
    h60 = h / 60.0
    h60f = math.floor(h60)
    f = h60 - h60f
    if f<0.5:
        v = 3*v1*(1-f*s1)/(3-2*s1)
    elif f>=0.5:
        v = 3*v1*(1-s1+f*s1)/(3-2*s1)
    return [h, s, min(v,255)]  


if __name__=="__main__":
    #input and ouput path for image.
    PATH_TO_WRONG_IMAGE = './wrong_image.jpg'
    PATH_TO_RIGHT_IMAGE = './right_image.jpg'

    image_wrong = cv2.imread(PATH_TO_WRONG_IMAGE)
    image_wrong_hsv = cv2.cvtColor(image_wrong, cv2.COLOR_BGR2HSV)
    shape = image_wrong.shape
    image_right_hsv = np.zeros(shape, dtype=np.uint8)

    #iterate over every pixel to change the V value.
    for row in range(shape[0]):
        for col in range(shape[1]):
            image_right_hsv[row][col] = get_right_V(image_wrong_hsv[row][col])
    
    image_right = cv2.cvtColor(image_right_hsv, cv2.COLOR_HSV2BGR)
   
    cv2.imwrite(PATH_TO_RIGHT_IMAGE, image_right)  