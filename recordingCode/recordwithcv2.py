import numpy as np
import cv2
from time import sleep
import datetime
import os
cwd = os.getcwd()
cap = cv2.VideoCapture(0)
while True:
    if cap==True:
        print "Camera is connected"
    else:
        print "Camera is not connected. Exiting!!"
        break
    # Define the codec and create VideoWriter object
    currentTime = datetime.datetime.now()
    #Concat CWD and Timestamp to make it generic
    fileName = "{0}/output{1}.avi".format(cwd,currentTime) 
    fileName = fileName.replace(" ","") #Remove Spaces from Timestamp
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    frame_counter = 0
    out = cv2.VideoWriter(fileName,fourcc, 25.0, (640,480))
    while frame_counter <= 3000:
        ret, frame = cap.read()
        if ret==True:
            # frame = cv2.flip(frame,2)
            frame_counter += 1
            # write the frame
            out.write(frame)
            # cv2.imshow('frame',frame)
            if frame_counter == 3000:
                out.release()
        else:
            break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
