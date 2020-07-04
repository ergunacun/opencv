import cv2
import numpy as np

img = cv2.imread('C:\\Users\\user\\Desktop\\OpenCV\\helikopter.jpg')

kuyruk = img[156:256, 0:80]
img[0:100,300:380] = kuyruk

cv2.imshow("image",img)
