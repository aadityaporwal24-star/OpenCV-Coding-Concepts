import cv2
image=cv2.imread("Image Transformation and Manipulation/snake.png")

if image is None:
    print("NOT LOADED!!")
else:
    print("Loaded")

    

    cv2.line(image,(50,100),(300,100),(0,0,255),4)
    cv2.rectangle(image,(350,200),(250,350),(0,255,0),-1)
    cv2.rectangle(image,(450,250),(360,450),(0,95,0),5)
    cv2.circle(image,(290,150),50,(245,0,0),5)
    cv2.putText(image,"SNAKE --PYTHON",(50,300),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,255,255),2)


    cv2.imshow("LINE MADE",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
