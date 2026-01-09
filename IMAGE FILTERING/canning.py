import cv2

image=cv2.imread("IMAGE FILTERING/pink_flower.png",cv2.IMREAD_GRAYSCALE)

canned=cv2.Canny(image,50,150)

cv2.imshow("ORIGINAL",image)
cv2.imshow("CANNED",canned)

cv2.waitKey(0)
cv2.destroyAllWindows()