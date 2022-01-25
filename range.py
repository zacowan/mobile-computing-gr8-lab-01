import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG = 8
ECHO = 10

print("Distance Measurement")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting for Sensor to Settle")
time.sleep(2)

print("Starting measurement in 3 seconds")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Measuring")
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()

while GPIO.input(ECHO)==1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print("Distance:" + str(distance) + "cm")

GPIO.cleanup()