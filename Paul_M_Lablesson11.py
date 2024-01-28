# Lab 11: Understanding and Using an RPG LED
# control colors with buttons

# for the input pins
#		=	1
#			Button is not pressed
#		=	0
#			Button is pressed
# for the output pin
#		= 	0
#			switch is open
#		=	1
#			switch is closed
# 
# want to capture event when button goes from 0 (pressed) to 1 (not pressed)
import RPi.GPIO as GPIO
import time

redButton=21
greenButton=20
blueButton=16

redOutput=26
greenOutput=19
blueOutput=13

GPIO.setmode(GPIO.BCM)

GPIO.setup(redButton, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(greenButton, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(blueButton, GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(redOutput, GPIO.OUT)
GPIO.setup(greenOutput, GPIO.OUT)
GPIO.setup(blueOutput, GPIO.OUT)

redButtonState=1
greenButtonState=1
blueButtonState=1

lastRedButtonState=1
lastGreenButtonState=1
lastBlueButtonState=1

redLEDState=1
greenLEDState=1
blueLEDState=1

try:
	while True:

#		Check red button state and toggle LED state as needed
		redButtonState=GPIO.input(redButton)

		if redButtonState==1 and lastRedButtonState==0:
			redLEDState = not redLEDState
			GPIO.output(redOutput,redLEDState)
		lastRedButtonState=redButtonState
		
#		Check green button state and toggle LED state as needed		
		greenButtonState=GPIO.input(greenButton)
		
		if greenButtonState==1 and lastGreenButtonState==0:
			greenLEDState = not greenLEDState
			GPIO.output(greenOutput,greenLEDState)			
		lastGreenButtonState=greenButtonState	
	
#		Check blue button state and toggle LED state as needed

		blueButtonState=GPIO.input(blueButton)
		
		if blueButtonState==1 and lastBlueButtonState==0:
			blueLEDState = not blueLEDState
			GPIO.output(blueOutput,blueLEDState)
		lastBlueButtonState=blueButtonState
		
		time.sleep(0.1)

			
except KeyboardInterrupt:

	GPIO.cleanup()
	print('GPIO Cleanup is Complete')