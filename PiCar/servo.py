import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7,100)

p.start(5)

p.ChangeDutyCycle(2.5)
time.sleep(1)
p.ChangeDutyCycle(5)
time.sleep(1)

time.sleep(2)
GPIO.cleanup()
