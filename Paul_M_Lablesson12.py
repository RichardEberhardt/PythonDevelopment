# Lab 12: Set Color of RPG LED with Push Buttons
# uses Pulse Width Modulation to ge full range of colors

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
from vpython import *

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

dutyCycleIncrement=10

redCurrentDutyCycle=0.99
greenCurrentDutyCycle=0.99
blueCurrentDutyCycle=0.99

redLED=GPIO.PWM(redOutput,100)
redLED.start(int(redCurrentDutyCycle))

greenLED=GPIO.PWM(greenOutput,100)
greenLED.start(int(greenCurrentDutyCycle))

blueLED=GPIO.PWM(blueOutput,100)
blueLED.start(int(blueCurrentDutyCycle))

mySphere=sphere(color=color.white,radius=1,pos=vector(0,2.5,0))
myCyl=cylinder(color=color.white,radius=1,length=2.5,axis=vector(0,1,0))
myBase=cylinder(color=color.white,radius=1.2,length=0.25,axis=vector(0,1,0))
myLeg1=box(pos=vector(-.75,-3,0),size=vector(.1,6,.1),color=vector(.2,.2,.2))

myLeg2=box(pos=vector(.75,-3,0),size=vector(.1,6,.1),color=vector(.2,.2,.2))


try:
	while True:
		rate(20)
#		Check red button state and toggle LED state as needed
		redButtonState=GPIO.input(redButton)
		
		if redButtonState==1 and lastRedButtonState==0:
			redCurrentDutyCycle=redCurrentDutyCycle*1.58
#			redCurrentDutyCycle=redCurrentDutyCycle+dutyCycleIncrement
			if redCurrentDutyCycle>99:
				redCurrentDutyCycle=0.99
			redLED.ChangeDutyCycle(int(redCurrentDutyCycle))
		lastRedButtonState=redButtonState

#		Check green button state and toggle LED state as needed
		greenButtonState=GPIO.input(greenButton)
		
		if greenButtonState==1 and lastGreenButtonState==0:
			greenCurrentDutyCycle=greenCurrentDutyCycle*1.58
#			greenCurrentDutyCycle=greenCurrentDutyCycle+dutyCycleIncrement
			if greenCurrentDutyCycle>99:
				greenCurrentDutyCycle=0.99
			greenLED.ChangeDutyCycle(int(greenCurrentDutyCycle))
		lastGreenButtonState=greenButtonState

#		Check blue button state and toggle LED state as needed
		blueButtonState=GPIO.input(blueButton)
		
		if blueButtonState==1 and lastBlueButtonState==0:
			blueCurrentDutyCycle=blueCurrentDutyCycle*1.58
#			blueCurrentDutyCycle=blueCurrentDutyCycle+dutyCycleIncrement
			if blueCurrentDutyCycle>99:
				blueCurrentDutyCycle=0.99
			blueLED.ChangeDutyCycle(int(blueCurrentDutyCycle))
		lastBlueButtonState=blueButtonState
		
		mySphere.color=vector(redCurrentDutyCycle/25,greenCurrentDutyCycle/25,blueCurrentDutyCycle/25)
		myCyl.color=vector(redCurrentDutyCycle/25,greenCurrentDutyCycle/25,blueCurrentDutyCycle/25)
		myBase.color=vector(redCurrentDutyCycle/25,greenCurrentDutyCycle/25,blueCurrentDutyCycle/25)
		time.sleep(0.1)
#		print('Red Button State: ',redButtonState)
#		print('Last Red Button State: ',lastRedButtonState)	
except KeyboardInterrupt:

	GPIO.cleanup()
	print('GPIO Cleanup is Complete')
