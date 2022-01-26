import RPi.GPIO as GPIO
import time

#####################################################
# Lab 1 - Mobile Computing - Group 8 
# Shaun Fidler, Zachary Cowan, Sydney McLaughlin
#####################################################

def InitializeGPIO():
    # Configure Ultrasonic Sensor Pins
    global TRIG
    TRIG = 8
    global ECHO
    ECHO = 10

    # Configure LED Pins
    global RED
    RED = 11
    global GREEN
    GREEN = 15
    global BLUE
    BLUE = 13

    # Correspond Board Pin Numbers
    GPIO.setmode(GPIO.BOARD)

    # Ignore Channel Warnings
    GPIO.setwarnings(False)

    # Init Pins to Correct In/Out Modes
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(BLUE, GPIO.OUT)

def GetDistance():
    # GPIO.output(TRIG, False)
    # print("Pausing for Reading")
    # time.sleep(0.5)

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

    return distance

def BlinkLED(LED):
    GPIO.output(LED, GPIO.HIGH) # Turn on
    time.sleep(0.2) # Sleep for 0.2 second
    GPIO.output(LED, GPIO.LOW) # Turn off
    time.sleep(0.2) # Sleep for 0.2 second

def DistanceBasedLED():
    distance = GetDistance()
    print("Distance --> " + str(distance))
    if(distance > 100):
        BlinkLED(GREEN)
    elif(distance > 50):
        BlinkLED(BLUE)
    elif(distance < 50):
        BlinkLED(RED)

if __name__ == '__main__':
    InitializeGPIO()
    while(True):
        DistanceBasedLED()
        time.sleep(0.1)

    GPIO.cleanup()