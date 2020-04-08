#HAWK - MINI PROJECT MODEL 

from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import ctypes
import threading
import wmi
import brightness as b
import detect as d
import face_recognition
#calculates the face mapping

user2_image = face_recognition.load_image_file("users/user2.jpg")
user2_face_encoding = face_recognition.face_encodings(user2_image)[0]

user3_image = face_recognition.load_image_file("users/user3.jpg")
user3_face_encoding = face_recognition.face_encodings(user3_image)[0]

known_face_encodings = [user2_face_encoding, user3_face_encoding]
known_face_names = ["ALEX","KISHORE"]
#overide the inbuilt camera with a webcam connected to porrt 0 (DEFAULT)
ap = argparse.ArgumentParser()
ap.add_argument("-w", "--webcam", type=int, default=0,
help="index of webcam on system")
args = vars(ap.parse_args())

#Calculate Eye Aspect Ratio
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear
#Flag From GUI
CHECK_USER=1
CHECK_BLINK=0
CHECK_DROWSY=0

#Threshold Values based on Research
EYE_DROW_THRESH = 0.2
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3
EYE_DROW_CONSEC_FRAMES = 60
EYE_BLINK_THRESH = 10
B_COUNTER=0

#Counter values set for the individual events
COUNTER = 0
TOTAL = 0
DROWS_COUNT = 0
BLINK_COUNTER = 0
c=0

#Flags for System Operations
AUTOLOCK_FLAG = 0
TIME_FLAG=0
DROWS_FLAG = 0
l=0


#Loading the Face Landmark Algorithm
print("[HAWK] : Loading Facial Information")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#scan the individual eyes
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

print("[HAWK] : Starting Video Thread")
#vs = VideoStream(src=args["webcam"]).start()
time.sleep(1.0)

# Getting minute from which the user uses this feature
m1=time.localtime().tm_min
s1=time.localtime().tm_sec

video_capture = cv2.VideoCapture(0)
while True:
    ret,frame = video_capture.read()
    
    frame_detection=frame
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        
        #Locate the Eyes 
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        # Calculate the EAR for each eye
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        # Draw HULL for each eye
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        # DROWSINESS - LOCK 
        if ear < EYE_AR_THRESH:
            COUNTER+=1
            if ear < EYE_DROW_THRESH:
                print(DROWS_FLAG)
                if COUNTER >= EYE_DROW_CONSEC_FRAMES:
                    DROWS_COUNT+=1
                    cv2.putText(frame,"USER SLEEPY",(10,30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    if DROWS_COUNT==50:
                        DROWS_COUNT=0
                        DROWS_FLAG+=1
                        if DROWS_FLAG==3:
                            DROWS_FLAG=0
                            ctypes.windll.user32.LockWorkStation()
        else:
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                TOTAL+=1
                COUNTER=0

        if TOTAL >= EYE_BLINK_THRESH:
            wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(20, 0)
            TOTAL=0
            
        
        '''m2=time.localtime().tm_min
        s2=time.localtime().tm_sec

        if(abs(m1-m2)==1): #same minute
            m1=time.localtime().tm_min
            s1=time.localtime().tm_sec
            b.brightness_check(TOTAL,c)
            TOTAL=0'''

        cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    '''#f=video_capture.read()
    l+=d.detect_face(frame)
    s2.time.localtime().tm_sec
    if(abs(s2-s1)==10):
        if(l==0):
            ctypes.windll.user32.LockWorkStation()
                
       '''         
    
    if(CHECK_USER==1):
        s2=time.localtime().tm_sec #takes invocation time
        print(c)
        print(s1)
        print(s2)
        if(abs(s1-s2)==20): #works every 20 seconds
            while True:
                s2=time.localtime().tm_sec
                if(abs(s1-s2)!=30):
                    l=d.detect_face(frame_detection, known_face_encodings, known_face_names)
                    c=c+l       #dummy counter to check if faces have been identified
                    
            if(c==0):
                print("Locking  due to unauthenticated or no user...")
                ctypes.windll.user32.LockWorkStation()
                break
            else:
                c=0
                s1=time.localtime().tm_sec
                m1=time.localtime().tm_min
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
        
    if key == ord("q"):
        break
cv2.destroyAllWindows()
#vs.stop()








