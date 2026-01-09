import cv2

image=cv2.imread("IMAGE FILTERING/tree.png")

blurred=cv2.GaussianBlur(image,(7,7),3)

cv2.imshow("ORIGINAL",image)
cv2.imshow("Blurred!!",blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()