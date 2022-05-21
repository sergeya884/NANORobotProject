camera папка с кодом для работы с камерой и распознования мишени

Gauss папка с описанием разработки пушки

Haara_cascad папка про обучение каскада

lidar папка про настройку и тестирование лидара

motors папка про управление моторами

-------------------------------------------------------------------------------

Последовательность действий для запуска всего этого добра:

ДОСТУП К РАБОЧЕМУ СТОЛУ

1)Можно узнать ip бота с помощью команды: nmap -sn 192.168.0.0/24

2)Открыть putty: pytty

3)Bвести ip

4)Ввести логин nanobot и пароль

5)Запустить доступ к удаленному рабочему столу: ~/openvino 

6)Запустить программу VNC Viewer, ввести ip

УПРАВЛЕНИЕ

1)Из командной строки запустить: python3 ride.py

КАМЕРА

1)Из нового терминала: gst-launch-1.0 nvarguscamerasrc sensor_mode=0 ! 'video/x-raw(memory:NVMM),width=320, height=240, framerate=21/1, format=NV12' ! nvvidconv flip-method=0 ! 'video/x-raw,width=320, height=240' ! nvvidconv ! nvegltransform ! nveglglessink -e

ЛИДАР 

1)Из нового терминала: sudo chmod 777 /dev/ttyUSB0

roslaunch rplidar_ros rplidar.launch

2)Из нового терминала: roslaunch hector_slam_launch tutorial.launch


