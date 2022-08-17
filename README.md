# HAWK-The-smart-screen-application

What it is?
  Say, You dont have a windows feature like face unlock or secureness of PC or Laptop from peepers.
  We have the solution!
  
  HAWK provides a way to incorporate those features with your windows/linux OS as an application(currently not available for linux)
  
## Structure

GUI:
    Start with password_test.py
Libraries used:
os 
time
ctypes
tkinter
shutil
functools

GUI FILES: 
password_test.py --- For the Authentication
gui_pack.py --- For the control panel GUI
folder_gui.py --- For File selection using windows dialogue box
pass.txt --- Contains password(HAVE TO THINK ABOUT STORING IN DIFFERENT FORMAT)
flag.py --- Holds the setting options ON/OFF as flags
--------------------------------------------------------------------------
THE BACKEND:
    Start with p.py
Libraries used:
cv2
numpy
imutils
wmi
scipy
face_recognition

FILES:
p.py -- The service code that runs and monitors in the BG
detect.py --- The face detection code
shape_predictor_68_face_landmarks.dat --- The dlib uses this dat file for face mapping
