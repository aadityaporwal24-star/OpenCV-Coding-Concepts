import cv2 

image=cv2.imread("Image Transformation and Manipulation/snake.png")

if image is None :
    print("Image not Loaded")
else:
    print("Image Loaded")

    resized=cv2.resize(image,(300,300))

    cv2.imshow("Original",image)
    cv2.imshow("RESIZED BRO",resized)

    cv2.imwrite("resized_output.png",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()