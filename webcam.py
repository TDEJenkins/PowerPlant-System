########################################
#    The Power Plant Capstone 2022     #
#   Code adapted from: GeeksforGeeks   # https://www.geeksforgeeks.org/detection-specific-colorblue-using-opencv-python/?ref=lbp
#           Mariah Armstorng           #
########################################

#C:\Users\maria\AppData\Local\Programs\Python\Python310\python

import cv2
import numpy as np 
  
#Webcam 
cam = cv2.VideoCapture(1) 

#Plant dying counter for automated system
deadCount = 0

while True:        
    #Captures the live stream frame-by-frame
    _, frame = cam.read() 

    #Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([25, 52, 72])
    upper_green = np.array([102, 255, 255])

    #Mask creation
    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #Showing the windows 
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    #Base colors detected within the res mask of green
    b = res[:, :, :1]
    g = res[:, :, 1:2]
    r = res[:, :, 2:]
  
    #Mean of the colors detected
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    #Break out! with Esc
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    #Determining if the plant is dead or aliveeee
    if (g_mean > r_mean and g_mean > b_mean):
        print("Alive")
    else:
        print("Dead")
        deadCount = deadCount + 1
        if deadCount == 50:
            #send email
            print('Sending Email: Plant Death Detected')
            break

   
cam.release()
cv2.destroyAllWindows()

