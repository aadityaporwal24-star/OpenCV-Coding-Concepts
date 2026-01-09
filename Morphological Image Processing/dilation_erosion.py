import cv2
import numpy as np 
image=cv2.imread("Morphological Image Processing/alphabet.png")
kernel=np.ones((10,10),np.uint8)

erosion=cv2.erode(image,kernel,iterations=1)
dilation=cv2.dilate(image,kernel,iterations=1)



cv2.imshow("ORIGINAL",image)
cv2.imshow("EROSION",erosion)
cv2.imshow("DILATION",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()