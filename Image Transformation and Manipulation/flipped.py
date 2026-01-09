import cv2

image=cv2.imread("Image Transformation and Manipulation/snake.png")

if image is None:
    print("Not Loaded!!")
else:
    flipped_horizontal=cv2.flip(image,1)
    flipped_vertical=cv2.flip(image,0)
    flipped_both=cv2.flip(image,-1)


    cv2.imshow("Original",image)
    cv2.imshow("horizontal",flipped_horizontal)
    cv2.imshow("Vertical",flipped_vertical)
    cv2.imshow("BOTH",flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()