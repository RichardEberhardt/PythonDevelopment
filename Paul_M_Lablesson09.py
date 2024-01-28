# Lab 9
# Dims or Brightens an LED using Pulse Width Modulation (PWM)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)

fasterButton=6
slowerButton=5

dutyCycleIncrement=10
currentDutyCycle=0

GPIO.setup(fasterButton, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(slowerButton, GPIO.IN,pull_up_down=GPIO.PUD_UP)

LED=GPIO.PWM(26,500)
LED.start(0)

try:
	while(1):
		
		readFasterValue=GPIO.input(fasterButton)
		
		if readFasterValue==0:
			print('faster button pushed')
			currentDutyCycle=currentDutyCycle+dutyCycleIncrement
			if currentDutyCycle>99:
				currentDutyCycle=100
			print('current duty cycle: ',currentDutyCycle)
			LED.ChangeDutyCycle(currentDutyCycle)
			time.sleep(.1)
			
		readSlowerValue=GPIO.input(slowerButton)
		
		if readSlowerValue==0:
			print('slower button pushed')
			currentDutyCycle=currentDutyCycle-dutyCycleIncrement
			if currentDutyCycle<0:
				currentDutyCycle=0
			print('current duty cycle: ',currentDutyCycle)
			LED.ChangeDutyCycle(currentDutyCycle)
			time.sleep(.1)
				
except KeyboardInterrupt:

	GPIO.cleanup()
	print('GPIO Cleanup is Complete')
