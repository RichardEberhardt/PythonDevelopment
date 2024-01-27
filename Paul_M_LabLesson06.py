# used in lab6 on GPIO pins and Pull Up and Pull Down reistors
# added a  comment
# added another
import RPi.GPIO as GPIO

import time
GPIO.setmode(GPIO.BCM)
inPin=21
GPIO.setup(inPin,GPIO.IN)
try:
		while True:
			readVal=GPIO.input(inPin)
			print(readVal)
			time.sleep(1)
except KeyboardInterrupt:
		GPIO.cleanup()
