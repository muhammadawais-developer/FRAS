#import dependencies
import cv2
import os
import face_recognition
import pickle

# importing the student images into a list
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []

# getting the students pictures with ids
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
print(studentIds)

# opencv uses bgr
# face_recognition uses rgb
# so we are converting our images into rgb , its basically for encoding purposes
def findEncodings(imagesList):
    # storing the encoded images
    encodeList = []
    for img in imagesList:
        # we convert from bgr to rgb
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Completed !")

# pickle file creation and storing the data for the webcam recognition
file = open("EncodeFile.p","wb")
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Saved !")

