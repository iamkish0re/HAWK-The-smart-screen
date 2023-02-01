# HAWK - The smart screen application

What it is?
  Say, You dont have a windows feature like face unlock or secureness of PC or Laptop from peepers.
  We have the solution!
  
  HAWK provides a way to incorporate those features with your windows/linux OS as an application(currently not available for linux)
  
## Structure

  GUI:
    Start with password_test.py

  Libraries used:
  1. os 
  2. time
  3. ctypes
  4. tkinter
  5. shutil
  6. functools

  GUI FILES: 
  1. `password_test.py`: For the Authentication
  2. `gui_pack.py`: For the control panel GUI
  3. `folder_gui.py`: For File selection using windows dialogue box
  4. `pass.txt`: Contains password(HAVE TO THINK ABOUT STORING IN DIFFERENT FORMAT)
  5. `flag.py`: Holds the setting options ON/OFF as flags
  --------------------------------------------------------------------------
  THE BACKEND:
      Start with p.py
      
  Libraries used:
  1. cv2
  2. numpy
  3. imutils
  4. wmi
  5. scipy
  6. face_recognition

  BACKEND FILES:
  1. `p.py`: The service code that runs and monitors in the BG
  2. `detect.py`: The face detection code
  3. `shape_predictor_68_face_landmarks.dat`: The dlib uses this dat file for face mapping
