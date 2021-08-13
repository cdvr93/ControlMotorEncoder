GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(ONOFF,GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.output(ONOFF,1)
GPIO.output(DIR,0)   
        
p = GPIO.PWM(PUL, 100)  # channel=18 frequency=50Hz
p.start(0)
    
try:
    inicio = default_timer()
    while 1:
        
        for dc in range(0,200):
            p.ChangeDutyCycle(50)
            time.sleep(0.1)
        #time.sleep(.05)    
        GPIO.output(DIR,0)
        for dc in range(0,200):
            p.ChangeDutyCycle(50)
            time.sleep(0.1)
        #time.sleep(.05)
        break
    GPIO.output(ONOFF,1)
    fin = default_timer()
    print (fin - inicio)
        
    
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()