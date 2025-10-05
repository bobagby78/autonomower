#rpi leds

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT)
while True:
	print('led on')
	GPIO.output(8, GPIO.HIGH)
	time.sleep(1)
	print('led off')
	GPIO.output(8, GPIO.LOW)
	time.sleep(1)

