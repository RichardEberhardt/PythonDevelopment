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
# end of comments

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


try:

	while True:
		# Print the values to the serial port
		temperature_c = sensor.temperature
		temperature_f = temperature_c * (9 / 5) + 32
		humidity = sensor.humidity
		print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, 		temperature_f, humidity))
		
		sleep(2)
		
#		LCD1602.write(0,0,'Hello World')
#		LCD1602.write(0,1,'Welcome!')

except KeyboardInterrupt:

	LCD1602.clear()
	print("LCD 	Good to Go")
	
