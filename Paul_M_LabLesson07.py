# Lesson 7 - GPIO Inputs from Button Switch
#	Using the Raspberry Pi pull up function
# for the input pin
#	readPinState
#		=	1
#			Button is not pressed
#		=	0
#			Button in pressed
# for the output pin
#		= 	0
#			switch is open
#		=	1
#			switch is closed
# comment
# another comment
import RPi.GPIO as GPIO
from time import sleep
delay=.1
inPin=21
outPin=20
lastPinState=-1
readPinState=-1
change = False
ON_OFF = False


GPIO.setmode(GPIO.BCM)
GPIO.setup(outPin,GPIO.OUT)
GPIO.setup(inPin, GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
		while True:
				readPinState=GPIO.input(inPin)
				print('readPinState: ',readPinState)

				# check to see f the input pin status has changed
						
				if readPinState!=lastPinState:
					# print('Not the same')
					ON_OFF=not ON_OFF
					CPIO.output(outPin, ON_OFF)
					
# 					if GPIO.input(outPin)==1:
# 						print('Skipping change')
# 						breakpoint()
# 					else:
# 						if readPinState==1:
# 							GPIO.output(outPin,0)
# 						
# 						if readPinState==0:
# 							GPIO.output(outPin,1)
# 						# change = not change
# 						# GPIO.output(outPin,change)
					
						lastPinState=readPinState
						print('outpin status in if clause ',GPIO.input(outPin))
						breakpoint()
					
					
				else:
					# print('Did not change')
					# print('outpin status in else clause ',GPIO.input(outPin))
			
					# breakpoint()
		
				sleep(1)
				
except KeyboardInterrupt:
	GPIO.cleanup()
	print("GPIO Cleanup is Complete")

