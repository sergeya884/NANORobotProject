from SimpleCV import Display, Image
from time import sleep

myDisplay = Display(resolution=(320,240))
rasIm = Image("ras.jpg")
rasIm.listHaarFeatures()

frame=Image("20.jpg")  
faces=frame.findHaarFeatures('tank.xml')
if faces:
    for face in faces:
        print "Face at: " + str(face.coordinates())
    faces.show(width=3)
else:
    print "NO faces detected."
    frame.save(myDisplay)
    
   
