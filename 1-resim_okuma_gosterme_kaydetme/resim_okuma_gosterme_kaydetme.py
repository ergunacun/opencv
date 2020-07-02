import cv2

img = cv2.imread("E:\klon.jpg",0) # 0 değeri gray scale için
# # print(img)
cv2.namedWindow("image",cv2.WINDOW_NORMAL) #gösterilen image ölçeklenebilir olması için

cv2.imshow("image",img)
cv2.imwrite("E:\klon1.jpg",img)
cv2.waitKey(0) # image in kapatılana kadar gösterilmesini sağlar
cv2.destroyAllWindows()
