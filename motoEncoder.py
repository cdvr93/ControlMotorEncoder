from time import sleep
import RPi.GPIO as GPIO


pin_A = 17
pin_B = 18
DIR = 20
STEP = 11
SPR = 3200
ONOFF = 5

Encoder_Count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup (pin_A, GPIO.IN)
GPIO.setup (pin_B, GPIO.IN)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP,GPIO.OUT)
GPIO.setup(ONOFF,GPIO.OUT)
GPIO.output(DIR,1)
GPIO.output(ONOFF,0)



step_count = SPR
step_count1 = 3200
delay = .000001
#delay1 = .01

A_Pos = 0
A_Last = "00"
STATE = {"0001":1,"0010":-1,"0100":-1,"0111":1,"1000":1,"1011":-1, "1101":-1, "1110":1}

def Encoder1(channel1):
    global Encoder_Count,A_Pos,A_Last,STATE
    now = str(GPIO.input(17)) + str(GPIO.input(18))
    key =A_Last + now
    
     
    if key in STATE:
            direction = STATE[key]
            A_Last = now
            A_Pos +=direction 
            
            

      

GPIO.add_event_detect (pin_A, GPIO.BOTH, callback=Encoder1)  
GPIO.add_event_detect (pin_B, GPIO.BOTH, callback=Encoder1)

try:

      while True :


            
            GPIO.output(DIR,1)
            for x in range(step_count):
                  GPIO.output(STEP, GPIO.HIGH)
                  sleep(delay)
                  GPIO.output(STEP, GPIO.LOW)
                  sleep(delay)
                  
            sleep(.3)
            GPIO.output(DIR, 0)
            for x in range(step_count):
                  GPIO.output(STEP, GPIO.HIGH)
                  sleep(delay)
                  GPIO.output(STEP, GPIO.LOW)
                  sleep(delay)
                        
            sleep(1)   
            
            
            
            GPIO.output(ONOFF,1)          
except KeyboardInterrupt:
      pulso.stop()
      GPIO.cleanup()