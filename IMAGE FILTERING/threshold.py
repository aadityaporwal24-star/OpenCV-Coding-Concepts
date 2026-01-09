import cv2

image=cv2.imread("IMAGE FILTERING/man.png",cv2.IMREAD_GRAYSCALE)

ret,thresh_img=cv2.threshold(image,120,255,cv2.THRESH_BINARY)

cv2.imshow("ORIGINAL",image)
cv2.imshow("THRESHOLD",thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
