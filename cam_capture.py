import cv2

#Abrindo Video da Webcam Com Open-Cv
webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("MyCam", frame)
        key = cv2.waitKey(5)
        if key == 27: # Se a Tecla ESC For Apertada :
            break
    cv2.imwrite("MyCapture.png", frame)

webcam.release()
cv2.destroyAllWindows()