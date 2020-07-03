import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.circle(img,(100,100),60,(255,0,0),-1)

cv2.imshow("img",img)
