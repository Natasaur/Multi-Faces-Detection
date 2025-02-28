# Script para extraer rostros de un conjunto de imágenes
# En input_images
import cv2
import os

imagesPath = "C:/Users/jakeg/Desktop/multiple_face_recognition/images/input_images"

if not os.path.exists("faces"):
     os.makedirs("faces")
     print("Carpeta faces creada con éxito")

# Detector facial
# Haar Cascades
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

count = 0
for imageName in os.listdir(imagesPath):
     print(imageName)
     image = cv2.imread(imagesPath + "/" + imageName)
     # faces = faceClassif.detectMultiScale(image, 1.1, 5)
     faces = faceClassif.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))
     for (x, y, w, h) in faces:
          #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
          face = image[y:y + h, x:x + w]
          face = cv2.resize(face, (200, 200))
          cv2.imwrite("faces/" + str(count) + ".jpg", face)
          count += 1