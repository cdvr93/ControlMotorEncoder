import RPi.GPIO as GPIO
import time
from timeit import default_timer

DIR = 20
PUL = 18
ONOFF = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL,GPIO.OUT)
GPIO.setup(DIR,GPIO.OUT)
GPIO.setup(ONOFF,GPIO.OUT)

p=GPIO.PWM(PUL,70000)
p.start(0)
GPIO.output(ONOFF,0)
inicio = default_timer()
print (type(p))


while True:
    GPIO.output(ONOFF,0)
    GPIO.output(DIR,1)
    iniDir1 = default_timer()
    p.ChangeDutyCycle(50)
    finDir1 = default_timer()
    time.sleep(1)
    GPIO.output(DIR,0)
    iniDir0 = default_timer()
    p.ChangeDutyCycle(50) #Motor will run at High speed
    finDir0 = default_timer ()
    time.sleep(1)
    GPIO.output(ONOFF,1)
    p.stop()
    print ("Fin DIR 1: "+str(finDir1 - iniDir1))
    print("Dir0 time: " + str (finDir0 - iniDir0))
    break
    
fin = default_timer()
print ("Tiempo total : " + str (fin - inicio))
