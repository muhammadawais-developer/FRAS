# packagaes import
import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone

# webcam initialization
cap = cv2.VideoCapture(0)
cap.set(3, 640)  #width
cap.set(4, 480)  #height
imgBackground = cv2.imread("Resources/background.png")

# importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))


#load the encoding file for the webcam face recognition
print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encodings", studentIds)
print("Encode File Loaded !")

while True:
    success, img = cap.read()

    # resizing the img into 1/4th of the actual size of the img from webcam
    imgS = cv2.resize(img,(0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # locating the img and then compare the previous encoding with the new encodings
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    #webcam img refactoring
    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44+633, 808:808+414] = imgModeList[0]

    #face recognition
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print('matches', matches)
        print('faceDis', faceDis)

        matchIndex = np.argmin(faceDis)
        # print('matchIndex', matchIndex)

        if matches[matchIndex]:
            print("Known Face Detected !")
            print(studentIds[matchIndex])

            # webcam face detect corner rectangle
            y1,x2,y2,x1 = faceLoc
            # y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            bbox =  55 + x1 , 162 + y1 , x2-x1, y2-y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)

    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)

