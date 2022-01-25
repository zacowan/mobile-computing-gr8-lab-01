import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

pin_num = 12

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(pin_num, GPIO.OUT, initial=GPIO.LOW) # Set pin 12 to be an output pin and set initial value to low (off)

for i in range(20):
    print("ON")
    GPIO.output(pin_num, GPIO.HIGH) # Turn on
    sleep(0.2) # Sleep for 0.2 second
    print("OFF")
    GPIO.output(pin_num, GPIO.LOW) # Turn off
    sleep(0.2) # Sleep for 0.2 second

GPIO.cleanup()