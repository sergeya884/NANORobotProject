Обучение каскада.
Для детектора объектов необходимо обучить систему технического зрения. Для этого было сделано 1500 фотографий, переконвертированных в черно-белый формат разрешением 320x240. 500 - содержат объект, 1000 –не содержат . На основе этих фотографий и происходило обучение.

«Хорошие» и «плохие» фотографии

!["хорошее" фото](https://github.com/sergeya884/NANORobotProject/blob/main/common/Haara_cascad/photo/good.png) !["плохое" фото](https://github.com/sergeya884/NANORobotProject/blob/main/common/Haara_cascad/photo/bad.png)

Примеры работы детектора

![](https://github.com/sergeya884/NANORobotProject/blob/main/common/Haara_cascad/photo/examp1.png) ![](https://github.com/sergeya884/NANORobotProject/blob/main/common/Haara_cascad/photo/examp2.png)

Использование примерa python test_tank.py [-h] -i IMAGE [-c CASCADE]

Детектор получился не очень точный, бывают ложные срабатывания, однако для первых шагов вполне неплохо. Недавно собрал себе мощный компьютер, возможно в будущем обучу нормальную нейросеть, а то время обучения на ноутбуке даже такого простого каскада 5-6 часов.
