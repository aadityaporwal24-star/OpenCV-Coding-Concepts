import cv2

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read() # ret->True/Flase frame->image
    if not ret:
        print("Could not read")
        break

    cv2.imshow("WEBCAM BRO",frame)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        print("Quitting..")
        break

cap.release()
cv2.destroyAllWindows() 
