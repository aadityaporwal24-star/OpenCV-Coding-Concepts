import cv2
import numpy as np

img1=np.zeros((300,300),dtype="uint8")
img2=np.zeros((300,300),dtype="uint8")

cv2.circle(img1,(150,150),100,255,-1)
cv2.rectangle(img2,(100,100),(250,250),255,-1)

b_and=cv2.bitwise_and(img1,img2)
b_or=cv2.bitwise_or(img1,img2)
b_not=cv2.bitwise_not(img1)

cv2.imshow("IMAGE 1 ORIGINAL",img1)
cv2.imshow("IMAGE 2 ORIGINAL",img2)
cv2.imshow("AND IMAGE",b_and)
cv2.imshow("OR IMAGE",b_or)
cv2.imshow("NOT IMAGE",b_not)

cv2.waitKey(0)
cv2.destroyAllWindows()



