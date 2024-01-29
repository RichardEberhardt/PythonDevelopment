# Lab 16: Set Color of RPG LED with Potentiometers

# uses Pulse Width Modulation to ge full range of colors
# comment
# another comment
# new comment

import RPi.GPIO as GPIO
import ADC0834
from time import sleep


GPIO.setmode(GPIO.BCM)

# redPotentiometer=21
# greenPotentiometer=20
# bluePotentiometer=16

redOutput=26
greenOutput=19
blueOutput=13

redCurrentDutyCycle=0
greenCurrentDutyCycle=0
blueCurrentDutyCycle=0

GPIO.setup(redOutput, GPIO.OUT)
GPIO.setup(greenOutput, GPIO.OUT)
GPIO.setup(blueOutput, GPIO.OUT)

redLED=GPIO.PWM(redOutput,2000)
redLED.start(int(redCurrentDutyCycle))

greenLED=GPIO.PWM(greenOutput,2000)
greenLED.start(int(greenCurrentDutyCycle))

blueLED=GPIO.PWM(blueOutput,2000)
blueLED.start(int(blueCurrentDutyCycle))



ADC0834.setup()

try:
    while True:
        redAnalogVal=ADC0834.getResult(0)
        greenAnalogVal=ADC0834.getResult(1)
        blueAnalogVal=ADC0834.getResult(2)
        
        
        print('Red Analog Value:  ',redAnalogVal)
        
        redCurrentDutyCycle=(100/255)*redAnalogVal
          
        if redCurrentDutyCycle>99:
        	redCurrentDutyCycle=99
        	
        print('Red Duty Cycle: ',redCurrentDutyCycle)
        	
        redLED.ChangeDutyCycle(redCurrentDutyCycle)
        
        
        print('GreenAnalog Value: ',greenAnalogVal) 
        greenCurrentDutyCycle=(100/255)*greenAnalogVal
          
        if greenCurrentDutyCycle>99:
        	greenCurrentDutyCycle=99
        	
        print('Green Duty Cycle: ',greenCurrentDutyCycle)
        	
        greenLED.ChangeDutyCycle(greenCurrentDutyCycle)
      
      
      
        print('blueAnalog Value: ',blueAnalogVal)         
        
        blueCurrentDutyCycle=(100/255)*blueAnalogVal
          
        if blueCurrentDutyCycle>99:
        	blueCurrentDutyCycle=99
        	
        print('blue Duty Cycle: ',blueCurrentDutyCycle)
        	
        blueLED.ChangeDutyCycle(blueCurrentDutyCycle)
        
        
#         greenLED.ChangeDutyCycle(greenAnalogVal*100/255)
#         blueLED.ChangeDutyCycle(blueAnalogVal*100/255)
        


        print('Blue Analog Value: ',blueAnalogVal)
        sleep(2)
        
except KeyboardInterrupt:
	redLED.stop()
	greenLED.stop()
	redLED.stop()
	GPIO.cleanup()
	print('GPIO cleanup is complete')
