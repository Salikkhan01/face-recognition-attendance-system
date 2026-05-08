import cv2
import face_recognition
import pickle
import os

# Importing student images
folderPath = 'images'
pathList = os.listdir(folderPath)

print(pathList)

imgList = []
studentIds = []

for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))
    imgList.append(img)

    studentIds.append(os.path.splitext(path)[0])

    print(path)
    print(os.path.splitext(path)[0])

print(studentIds)


def findEncodings(imagesList):
    encodeList = []

    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encodings = face_recognition.face_encodings(img)

        if len(encodings) > 0:
            encodeList.append(encodings[0])

    return encodeList


print("Encoding Started ...")

encodeListKnown = findEncodings(imgList)

encodeListKnownWithIds = [encodeListKnown, studentIds]

print("Encoding Complete")

file = open("EncodeFile.p", 'wb')

pickle.dump(encodeListKnownWithIds, file)

file.close()

print("File Saved")