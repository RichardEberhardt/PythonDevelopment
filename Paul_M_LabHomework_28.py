# Paul McWhorter Raspberry pi Tutorials
# Raspberry Pi LESSON 28: temperature Monitor and alarm
# Lab 28 
# Homework
# 
# 	Making a temperature sensor
# 	LCD display
# 	buzzer alarm based on temperature (over or under heated)	
# 	Trigger point set via Potentiometer
# 	Two Modes
# 		Set Up mode
# 		Monitor Mode		
# 
# It looks like the temperature/humidity sensor with LCD output would be the best starting point
# 
# Tasks
# 
# 	1.	Retrieve and test the temperature/humidity sensor with LCD 
# 	2.	Make sure this is still working
# 	3.	changes
# 			Migrate the buzzer set up to the board
# 			Add button for changing modes?
# 			Change code
# 				Accommodate the buzzer
# 				Code mode changer
# 
# 
# 	Components
# 		LCD
# 		Add temperature and humidity sensor DHT11
# 		Push button
#		Add Buzzer
# 
# 	Functionality
# 		Display the temperature and humidity on the LCD
# 		toggle button to swap between centigrade or fahrenheit
#

import RPi.GPIO as GPIO
import LCD1602
import adafruit_dht
import time
import board

LCD1602.init(0x27, 1)

# pin for reading the sensor
dht11Pin=26
# pin for the switch
inButtonPin=20

GPIO.setmode(GPIO.BCM)

GPIO.setup(dht11Pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(inButtonPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

currentTemperatureType = 'F'

lastInButtonState=-1
currentInButtonState=-1

ON_OFF=True

sensor = adafruit_dht.DHT11(board.D26)

while True:

	try:
	
	
		currentInButtonState=GPIO.input(inButtonPin)
		
		print('current button state is… ',currentInButtonState)
		
		if currentInButtonState!=lastInButtonState: #button state changed
			if currentInButtonState==GPIO.LOW: 		#button was just pressed
				ON_OFF=not ON_OFF
				if currentTemperatureType == "F":	#adjust temperature type
					currentTemperatureType="C"
				else:
					currentTemperatureType = 'F'
			else:	
				if currentInButtonState==GPIO.HIGH:	#button was just released
					lastInButtonState=currentInButtonState
		print('Current Temperature Type: ', currentTemperatureType)		
					
		# Print the values to the serial port
		temperature_c 			= sensor.temperature

		temperature_c_disp		="Temp={0:0.1f}C".format(temperature_c)
		
		temperature_f = temperature_c * (9 / 5) + 32
		temperature_f_disp		= "Temp={0:0.1f}F".format(temperature_f)
		
		if currentTemperatureType=='F':
			selectedTemperatureFormatted="Temp={0:0.1f}F".format(temperature_f)
	
		else:
			selectedTemperatureFormatted="Temp={0:0.1f}C".format(temperature_c)

		humidity = sensor.humidity
		humidity_disp = "Humidity={0:0.1f}".format(humidity)
		
		print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, 		temperature_f, humidity))
		
		LCD1602.write(0,0,selectedTemperatureFormatted)
		LCD1602.write(0,1,humidity_disp)
		
		time.sleep(2)
		
		
		
		

	except KeyboardInterrupt:	
		LCD1602.clear()
		GPIO.cleanup()
		print("LCD 	Good to Go")
		exit()		
			
	except RuntimeError as error:
		# Errors happen fairly often, DHT's are hard to read, just keep going
		print(error.args[0])
		time.sleep(2.0)
		continue
		
	except Exception as error:
		dhtDevice.exit()
		raise error