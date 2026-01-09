import cv2

image=cv2.imread("Read Display Save/output_snake.png")

if image is not None :
    success=cv2.imwrite("output_snake.png",image)
    if success:
        print("Image saved !!")
        print(success)
    else:
        print("NOT SAVED")
else :
    print("NOT LOADED !!")