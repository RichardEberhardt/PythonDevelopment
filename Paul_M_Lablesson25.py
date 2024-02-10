# Paul McWhorter Raspberry pi Tutorials
# Raspberry Pi LESSON 25: Using an LCD1602 LCD Display with I2C
# Lab 25 
# Homework
# 	Components
# 		LCD
# 		Add temperature and humidity sensor DHT11
# 		Push button
# 
# 	Functionality
# 		Display the temperature and humidity on the LCD
# 		toggle button to swap between centigrade or fahrenheit

import RPi.GPIO as GPIO
import LCD1602
import adafruit_dht
import time
import board

LCD1602.init(0x27, 1)

dht11Pin=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(dht11Pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

sensor = adafruit_dht.DHT11(board.D26)

while True:

	try:

		# Print the values to the serial port
		temperature_c 			= sensor.temperature

		temperature_c_disp		="Temp={0:0.1f}C".format(temperature_c)
		
		temperature_f = temperature_c * (9 / 5) + 32
		temperature_f_disp		= "Temp={0:0.1f}F".format(temperature_f)

		humidity = sensor.humidity
		humidity_disp = "Humidity={0:0.1f}".format(humidity)
		
		print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, 		temperature_f, humidity))
		
		LCD1602.write(0,0,temperature_f_disp)
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

