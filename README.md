# HAWK - The smart screen application

What it is?
  Say, You dont have a windows feature like face unlock or secureness of PC or Laptop from peepers.
  We have the solution!
  
  HAWK provides a way to incorporate those features with your windows/linux OS as an application(currently not available for linux)
  
## Structure
HAWK/
├── db/
│   ├── hawk.db
│   └── haarcascade_frontalface_default.xml
│   └── db.py
├── gui/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── face_detection/
│   ├── __init__.py
│   └── detect_faces.py
├── speech_assistant/
│   ├── __init__.py
│   ├── speech_recognition.py
│   └── text_to_speech.py
├── requirements.txt
└── main.py

  GUI:
    Start with password_test.py

  Libraries used:
  1. os 
  TODO: add recent changes with explanation  --------------------------------------------------------------------------
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
