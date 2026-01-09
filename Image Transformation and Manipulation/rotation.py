import cv2

image=cv2.imread("Image Transformation and Manipulation/snake.png")

if image is None:
    print("Not Loaded!!")
else:
    (h,w)=image.shape[:2]

    center=(w//2,h//2)
    M=cv2.getRotationMatrix2D(center,90,0.5)
    rotated=cv2.warpAffine(image,M,(w,h))

    cv2.imshow("Original",image)
    cv2.imshow("Rotated bro",rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()