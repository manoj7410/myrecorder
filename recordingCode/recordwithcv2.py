import numpy as np
import cv2
from time import sleep
import datetime
import os
import os.path
#cwd = os.getcwd()
cwd="/home/manoj/recordingCode"
print "CurrentDirectory = %s"%cwd
cap = cv2.VideoCapture(0)
break_flag = 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
while True:
    if break_flag == 1:
        print "Exiting main loop"
        break
    # Define the codec and create VideoWriter object
    currentTime = datetime.datetime.now()
    #Concat CWD and Timestamp to make it generic
    fileName = "{0}/output{1}.avi".format(cwd,currentTime) 
    fileName = fileName.replace(" ","") #Remove Spaces from Timestamp
    fileName = fileName.replace(":","") #Remove : from Timestamp
    print "FILENAME=%s"%fileName
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
            break_flag = 1
            break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
