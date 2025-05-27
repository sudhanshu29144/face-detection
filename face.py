import cv2
import cv2.data
modelPath = cv2.data.haarcascades + "/haarcascade_frontalface_default.xml"
model = cv2.CascadeClassifier(modelPath)
cam = cv2.VideoCapture(0)
while True:

            status, image = cam.read()
            faces = model.detectMultiScale(image, 1.3, 5)
            for face in faces:
                        x = face[0]
                        y = face[1]
                        w = face[2]
                        h = face[3]
                        cv2.rectangle(image,(x,y),(x+w,y+h),(0, 0, 255),2)
            cv2.imshow("face",image)
            if cv2.waitKey(1)== ord("q"):
                        break
