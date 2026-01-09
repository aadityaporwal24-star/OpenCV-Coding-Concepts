import cv2

image=cv2.imread("Read Display Save/output_snake.png")

if image is not None :
    cv2.imshow("OUR IMAGE",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image Not loaded ")

print("Hello")


  