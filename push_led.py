import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

while True:
    a = GPIO.input(25)
    if a:
        GPIO.output(18, False)
        print("Off")
    else:
        print("On")
        GPIO.output(18, True)
