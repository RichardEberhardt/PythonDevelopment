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
# 	1.	Retrieve and test the temperature/humidity sensor with LCD 	- CPT
# 	2.	Make sure this is still working								- CPT
# 	3.	Board changes
# 			Migrate the buzzer set up to the board					- CPT
# 			Add button for changing modes (may not use)				- CPT
#			Add potentiometer for setting trigger temperature		- CPT
#			Add ADC chip to the bread board							- CPT
#
#	4. Code Changes
# 			Read and process potentiometer							- CPT
#			Accommodate the buzzer									- CPT
# 			Code mode changer										- CPT
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
import ADC0834


LCD1602.init(0x27, 1)

# pin for reading the temp/humidity sensor
dht11Pin=26
# pin for changing the modes
modeButtonPin=20
# pin for buzzer
# buzzPin=17 had to change this since the library needs pin 17
buzzPin=22

potentiometerAnalogValue=0

potentiometerDigitalValue=0

GPIO.setmode(GPIO.BCM)

GPIO.setup(dht11Pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(modeButtonPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(buzzPin,GPIO.OUT)

currentTemperatureType = 'F'
currentTemperature=100

lastModeButtonState=-1
currentModeButtonState=-1

# ON_OFF==True means that we are in normal mode
# ON_OFF==False means that we are in trigger set mode
ON_OFF=True

sensor = adafruit_dht.DHT11(board.D26)

# buzz=GPIO.PWM(buzzPin,400)
buzz=GPIO.PWM(buzzPin,1)

buzz.start(50)

triggerValueDisp=0

ADC0834.setup()

while True:

	try:
	
		potentiometerAnalogValue=ADC0834.getResult(0)
		
		potentiometerDigitalValue=(100/255)*potentiometerAnalogValue
		
		print("Digital value is: ", potentiometerDigitalValue)
		
		currentModeButtonState=GPIO.input(modeButtonPin)
		
#		Detects changes to the state of the pushbutton
		
		if currentModeButtonState!=lastModeButtonState: #button state changed
			if currentModeButtonState==GPIO.LOW: 		#button was just pressed
				ON_OFF=not ON_OFF

			else:	
				if currentModeButtonState==GPIO.HIGH:	#button was just released
					ON_OFF=not ON_OFF
					lastModeButtonState=currentModeButtonState
					
		print("ON_OFF Value =", ON_OFF)	
		


		#	This part of the code handles trigger set mode	
			
		if ON_OFF==False:
		
			triggerValueDisp=("Trigger={0:0.1f}".format(potentiometerDigitalValue))
			
			setupModeDisplay="SetUp Mode"
			
			GPIO.output(buzzPin,GPIO.HIGH)

			LCD1602.clear()
			LCD1602.write(0,0,setupModeDisplay)		
			LCD1602.write(0,1,triggerValueDisp)
			
		else:
			# This part of the code handles normal mode (shows temperature)
									
			temperature_c 			= sensor.temperature
			
			temperature_f = temperature_c * (9 / 5) + 32
			
			currentTemperature=temperature_f
			
			selectedTemperatureFormatted="Temp={0:0.1f}F".format(temperature_f)
			
			print(selectedTemperatureFormatted)
			
			currentTemperature=temperature_f
			
			triggerValueDisp=("Trigger={0:0.1f}".format(potentiometerDigitalValue))
			
			normalModeDisplay="Normal Mode"
			
			LCD1602.clear()
			
			LCD1602.write(0,0,normalModeDisplay)
			LCD1602.write(0,1,selectedTemperatureFormatted)
						
		time.sleep(2)
		
		print(currentTemperature,potentiometerDigitalValue)
		
		if not currentTemperature>=potentiometerDigitalValue:
			print('Found one')
			for i in range(150,2000):
				buzz.ChangeFrequency(i)
				time.sleep(.0001)
				
			for i in range(2000,150,-1):
				buzz.ChangeFrequency(i)
				time.sleep(.0001)
				
		GPIO.output(buzzPin,1)

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
#		dhtDevice.exit()
		raise error
