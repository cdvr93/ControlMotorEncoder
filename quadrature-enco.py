
import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(True)

pin_A = 17
pin_B = 18

Encoder_Count = 0

GPIO.setup (pin_A, GPIO.IN)
GPIO.setup (pin_B, GPIO.IN)
A_Pos = 0
A_Last = "00"
STATE = {"0001":1,"0010":-1,"0100":-1,"0111":1,"1000":1,"1011":-1, "1101":-1, "1110":1} 



def Encoder1(channel1):
    global Encoder_Count,A_Pos,A_Last,STATE
    now = str(GPIO.input(17)) + str(GPIO.input(18))
    key = A_Last + now
    if key in STATE:
            direction = STATE[key]
            A_Last = now
            A_Pos +=direction


GPIO.add_event_detect (pin_A, GPIO.BOTH, callback=Encoder1)  
GPIO.add_event_detect (pin_B, GPIO.BOTH, callback=Encoder1)

while(1):

    print (A_Pos)
    time.sleep(0.1)

GPIO.cleanup()