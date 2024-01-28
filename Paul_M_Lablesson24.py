# homework assignment for Lesson 24
# Have the PIR sensor work with other components
# 
# Connect PIR to RGB	
# 	Green:			Monitor is on
# 	Red: 			Motion Detected now
# 	Yellow:			Warning at least one motion detected 

# this program was updated to use sound a passive buzzer when motion is detected

import RPi.GPIO as GPIO
import time
from datetime import datetime

motionPin=18

buzzerPin=25

redLEDPin=16
yellowLEDPin=20
greenLEDPin=21

GPIO.setmode(GPIO.BCM)

GPIO.setup(motionPin,GPIO.IN)

GPIO.setup(buzzerPin,GPIO.OUT)

GPIO.setup(redLEDPin,GPIO.OUT)
GPIO.setup(yellowLEDPin,GPIO.OUT)
GPIO.setup(greenLEDPin,GPIO.OUT)

GPIO.output(redLEDPin,0)
GPIO.output(greenLEDPin,0)
GPIO.output(yellowLEDPin,0)

lastMotion=0

buzzer=GPIO.PWM(buzzerPin,1000)

intruderLog=open("intruderLog.txt","a")

#	Code to do the countdown to start
def countdown_timer(seconds):
    while seconds > 0:
        print(f"Starting Monitoring - Please wait: {seconds} seconds")
        time.sleep(1)  # Delay for 1 second
        seconds -= 1

    print("Monitoring Active!")

try:
	countdown_timer(10)
	
	while True:
		motion=GPIO.input(motionPin)
		GPIO.output(greenLEDPin,1)
		
		if motion==1:			# Motion has been detected
			buzzer.start(10)
			

			if lastMotion==0:	# Motion detected is a new motion
#				build timestamp
				now=datetime.now()
				dateString=now.isoformat()
				intruderDateWrite="Motion Detected"+"\t"+dateString+"\n"
				intruderDatePrint="Motion Detected"+"\t"+dateString
				intruderLog.write(intruderDateWrite)
				print(intruderDatePrint)
				GPIO.output(redLEDPin,1)
				GPIO.output(yellowLEDPin,1)
				
		else:
			GPIO.output(redLEDPin,0)
			lastMotion=0			# No motion detected
			buzzer.stop()	
				
#		print(motion)
		time.sleep(0.1)

except KeyboardInterrupt:

	GPIO.output(redLEDPin,0)
	GPIO.output(greenLEDPin,0)
	GPIO.output(yellowLEDPin,0)
	GPIO.cleanup()
	print('GPIO Cleanup Completed')
