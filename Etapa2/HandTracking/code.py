import numpy as np
import cv2

img = cv2.imread("entrada.jpg")

# (x,y,color,thickness)
# x = largura x altura
# rec = cv.rectangle(img,(50,300),(250,500),(0,255,0),2)


# pts = np.array([[50,150],[20,15],[50,20],[23,23]],np.int32)
# cv.fillPoly(img,[pts],(0,255,0))



pts = np.array([[170,50],[240, 40],[240, 150], [210, 100], [130, 130]], np.int32)
cv2.fillPoly(img, [pts], (255,150,255))

cv2.imshow("asd",pts)
cv2.waitKey(0)
