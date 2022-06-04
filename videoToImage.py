import numpy as np
import cv2 as cv
filename='1out_detected'
cap = cv.VideoCapture(filename+'.avi')
counter=0
while(cap.isOpened()):
    ret, frame = cap.read()
    cv.imwrite("./JPEGImages3/"+filename+"Image"+str(counter)+".jpg", frame)
    counter+=1
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
