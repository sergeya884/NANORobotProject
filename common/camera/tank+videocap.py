import cv2
# все каскады в открытом доступе лежа в https://github.com/opencv/opencv/tree/4.x/data


face_cascade_db = cv2.CascadeClassifier("tank.xml") 
cap = cv2.VideoCapture(0) #камеры   подключенные к пк нумируются с 0

while True:
    #img = cv2.imread('b.webp',)   #загружаем картинку лица фронтальную или трансляцию
    success, img = cap.read()
 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #меняем ее на черно-белую для распознования
    #img_gray = cv2.resize(img_gray, (320, 240))
        #к переменной face_cascade_db применяет распознование и сохроняет соотв. координаты
                                                   # параметры
    faces = face_cascade_db.detectMultiScale(img_gray)

    for (x, y, w, h) in faces:        #теперь пройдемся по всем координатам и зададим квадрат с параметрами
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
                                             #цвет    толщина
    cv2.imshow('name of window', img)  #заускаем окно 
    
    if cv2.waitKey(1) & 0xff == ord('q'):  #иачепредыдущая команда сразу завершается
        break
cap.release() #освобаждаем камеру
cv2.destroyAllWindows() #и закрывать все окошки

