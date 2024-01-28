# Import libraries
import RPi.GPIO as GPIO
import time
import ADC0834

ADC0834.setup()

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set pin 11 as an output, and define as servo1 as PWM pin
GPIO.setup(20,GPIO.OUT)
servo1 = GPIO.PWM(20,50) # pin 20 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)

# Loop to allow user to set servo angle. Try/finally allows exit
# with execution of servo.stop and GPIO cleanup :)
#float fact
try:
    while True:
        analogValPot=ADC0834.getResult(0)
        print('Value: ',analogValPot)
        pwmPercent=10/255*(analogValPot)+2
        print('pwmPercent =',pwmPercent)
        servo1.ChangeDutyCycle(pwmPercent)
        time.sleep(.1)


except KeyboardInterrupt:
    #Clean things up at the end
    servo1.stop()
    GPIO.cleanup()
    print("GPIO Cleanup Completed")
