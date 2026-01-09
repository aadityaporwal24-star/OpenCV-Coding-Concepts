import cv2

image=cv2.imread("Read Display Save/output_snake.png")

if image is not None :
    h,w,c=image.shape
    print(f"Image loaded:\nheight:{h}\nwidth:{w}\nchannel:{c}")
else:
    print("Not Loaded")