import cv2

image=cv2.imread("Image Transformation and Manipulation/snake.png")

if image is None:
    print("Not Loaded")
else:
    print("LOADED!!")

    cropped=image[100:200,50:150]

    cv2.imshow("ORIGINAL BRO",image)
    cv2.imshow("CROPPED BRO",cropped)

    cv2.imwrite("cropped_image.png",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
