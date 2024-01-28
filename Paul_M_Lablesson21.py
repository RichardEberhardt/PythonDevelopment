# lesson 21: Using and HC SR04 Ultrasonic sensor for Echolocation
# calculate the distance between the sensor and an object
# Distance=Rate*time
# Rate = the speed of sound
# Time = measured difference between trigger and response 
# speed of sound to inches per second calculator
# http://conversion.org/speed/speed-of-sound/inches-per-second
# conversion factor=13488.332620092
# then half the value (otherwise includes outbound and inbound timings)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
trigPin=23
echoPin=24
GPIO.setup(trigPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN)

try:
	while True:
		GPIO.output(trigPin,0)
		time.sleep(2E-6)
		GPIO.output(trigPin,1)
		time.sleep(10E-6)
		GPIO.output(trigPin,0)
		while GPIO.input(echoPin)==0:
			pass
		echoStartTime=time.time()
		while GPIO.input(echoPin)==1:
			pass
		echoStopTime=time.time()
		elapsed=echoStopTime-echoStartTime
		conversionFactor=13488.332620092 
		distance=elapsed*conversionFactor
		distance= distance/2
		print('Distance from sensor: ',distance)
		time.sleep(.2)
		
except KeyboardInterrupt:
	GPIO.cleanup()
	print('GPIO cleanup completed')
