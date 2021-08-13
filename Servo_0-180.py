#Codigo Servomotor
#Uso y manejo de motores


import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

servo_Uno = 11

GPIO.setup(servo_UNo, GPIO.OUT)

pulso = GPIO.PWM(sevo_Uno, 50) #Se hace con PWM donde 50 es la frecuencia que se usa el motor(hz) 
pulso.start(2.5) #2.5 es la posicion inicial del motor 

try: 
		while True:  
				for i in range(0,180): # el motor se mueve de 180 grados
					   	  grados= 1.0/18.0*(i)+2.5 
						  pulso.ChangeDutyCycle(grados) 
except KeyboardInterrupt: 
		pulso.stop()
		GPIO.cleanup()

