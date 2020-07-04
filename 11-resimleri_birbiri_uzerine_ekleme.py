import cv2
import numpy as np

img1 = cv2.imread('C:\\Users\\user\\Desktop\\OpenCV\\helikopter.jpg')
img2 = cv2.imread('C:\\Users\\user\\Desktop\\OpenCV\\helikopter2.jpg')
img3 = img2[0:412,0:640]

dst = cv2.addWeighted(img1,0,img3,1,0)

cv2.imshow("dst",dst)
