import cv2      #библиотека для видеотрансляции pip install opvencv-python

cap = cv2.VideoCapture(0)

while True:     #считывание изображения
    ret, img = cap.read()
    cv2.imshow('camera', img)
    if cv2.waitKey(10) == 27:   #услови прекращения трансляции нажатием клавиши с кодом 27 "esc"
        break                   #10милисекунд это частота картинки

cap.release()   #освобаждение прекращение видеотрансляции
cv2.destroyAllWindows()     #закрываем окно