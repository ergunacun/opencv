import cv2
import numpy as np

img = cv2.imread("D:\\OpenCV\\test_images\\filter.jpg")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])

mask = cv2.inRange(hsv,lower_blue,upper_blue)

cv2.imshow("Frame",img)
cv2.imshow("MASK",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
