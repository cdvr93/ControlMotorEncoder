#Servomotor se mueve con potenciometro
#fuente https://www.youtube.com/watch?v=gnyLlFw7Twk
#Este potenciometro no controla vel , solo posicionamiento del servo

import spidev #comunicacion spi analogica
from numpy import interp #numpy calcculo cientifico
from time import sleep 
import RPi.GPIO as GPIO 

spi = spidev.SpiDev() 
spi.open(0,0) 

servo_Uno = 11 #pin fisico GPIO
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(servo_Uno, GPIO.OUT)

pwm = GPIO.PWM(servo_Uno, 50) #50 hz frecuencia con la que trabaja servomotor
pwm.start(2.5) #2.5 posicion de inicio servo de acuerdo a especificaciones del fabricante

def analogRead(canal):
	spi.max_speed_hz = 1350000  #maxima lectura, (potenciometro) 
 	adc = spi.xfer2([1,(8+canal)<<4,0])   #especificaciones del conversor AD MCP3008
  	data = ((adc[1]&3) << 8) + adc[2]  
  	return data

try:
		while True:
	      	output = analogRead(0) #potenciometro en canal 0
	      	output = interp(output, [0, 1023], [0, 180]) #mapea las posiciones 
	      	grados = 1.0/18.0*(output)+2.5  #formula para mover servomotor
		    pwm.ChangeDutyCycle(grados)
except KeyboardInterrupt:
    pwm.stop() 
    GPIO.cleanup()



