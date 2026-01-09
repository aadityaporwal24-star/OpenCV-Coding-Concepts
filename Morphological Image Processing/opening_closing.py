import cv2
import numpy as np 
image=cv2.imread("Morphological Image Processing/alphabet.png")
kernel=np.ones((10,10),np.uint8)

opening=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)


cv2.imshow("ORIGINAL",image)
cv2.imshow("OPENING",opening)
cv2.imshow("CLOSING",closing)
cv2.waitKey(0)
cv2.destroyAllWindows()