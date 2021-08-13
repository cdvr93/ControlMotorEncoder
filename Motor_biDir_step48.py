#En este codigo se usa DRV8825 motor NEMA 23
#fuente https://www.rototron.info/raspberry-pi-stepper-motor-tutorial/
#https://www.youtube.com/watch?v=LUbhPKBL_IU

from time import sleep
import RPi.GPIO as GPIO

DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 48   # Steps per Revolution (360 / 7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)#sentido horario pin DIR(20) = 1

step_count = SPR
delay = .0208

try:
	while True:  #Bucle infinicto avance y retrocede motor

			for x in range(step_count):#cuenta los 48 pasos
			    GPIO.output(STEP, GPIO.HIGH)#pone en High pin STEP=21
			    sleep(delay)#envia pulsos cada 0.0208seg osea que para un giro tarda aprox 1 sg
			    GPIO.output(STEP, GPIO.LOW)#se alterna entre high y low el STEP cada 00.0208seg
			    sleep(delay)

			sleep(.5)#espera 0.5seg para iniciar en sentido anriohorario
			GPIO.output(DIR, CCW) #sentido Antihorario pin DIR(20) = 0
			for x in range(step_count):
			    GPIO.output(STEP, GPIO.HIGH)
			    sleep(delay)
			    GPIO.output(STEP, GPIO.LOW)
			    sleep(delay)
except KeyboardInterrupt:
GPIO.cleanup()