import face_recognition
import cv2
import numpy as np
import os

def detect_face(frame, known_face_encodings, known_face_names):
    flag = 0
    '''
    user1_image = face_recognition.load_image_file("users/user1.jpg")
    user1_face_encoding = face_recognition.face_encodings(user1_image)[0]

    user2_image = face_recognition.load_image_file("users/user2.jpg")
    user2_face_encoding = face_recognition.face_encodings(user2_image)[0]

    user3_image = face_recognition.load_image_file("users/user3.jpg")
    user3_face_encoding = face_recognition.face_encodings(user3_image)[0]'''

    # Try to get the user names and append it into the list 
    #store the known face as encoded values
    '''known_face_encodings = [user1_face_encoding , user2_face_encoding, user3_face_encoding]
    known_face_names = ["AKASH" , "ALEX","KISHORE"]'''

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    #Face_recognition uses RGB
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "USER"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                if(name):
                    flag=1
                else:
                    flag=0


    return flag
