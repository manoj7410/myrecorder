import numpy as np
import cv2
from time import sleep
file_count = 0
cap = cv2.VideoCapture(0)
while True:
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    frame_counter = 0
    out = cv2.VideoWriter('/home/manoj/recordingCode/output%d.avi' % file_count,fourcc, 25.0, (640,480))
    file_count += 1
    while frame_counter <= 3000:
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,1)
            frame_counter += 1
            # write the flipped frame
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
