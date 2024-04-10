import cv2
 
capture = cv2.VideoCapture("http:192.168.1.30")
 
while (capture.isOpened()):
    ret, frame = capture.read()
    cv2.imshow('webCam',frame)
    if (cv2.waitKey(1) == ord('s')):
        break
 
capture.release()
cv2.destroyAllWindows()