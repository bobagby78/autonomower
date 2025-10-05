#rpi leds

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(29, GPIO.OUT)
while True:
	print('led on')
	GPIO.output(29, GPIO.HIGH)
	time.sleep(1)
	print('led off')
	GPIO.output(29, GPIO.LOW)
	time.sleep(1)

