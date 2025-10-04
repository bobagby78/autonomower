import RPi.GPIO as GPIO
import time
from evdev import InputDevice, categorize, ecodes


#use GPIO physical pin layout
GPIO.setmode(GPIO.BOARD)

# Physical Pin Numbering (BOARD mode)
# -----------------------------------
# Pin 1  (3V3)                  -----           Pin 2 (5V)
# Pin 3  **left forward**       -----           Pin 4 (5V)
# Pin 5  **left reverse**       -----           Pin 6 (GND)
# Pin 7  (GPIO 4/GPCLK0)        -----           Pin 8  **right forward**
# Pin 9  (GND)                  -----           Pin 10 **right reverse**
# Pin 11 **lftFwdBtn**          -----           Pin 12 **rtFwdBtn**
# Pin 13 **lftRevBtn**          -----           Pin 14 (GND)
# Pin 15 (GPIO 22)              -----           Pin 16 **rtRevBtn**
# Pin 17 (3V3)                  -----           Pin 18 (GPIO 24)
# Pin 19 (GPIO 10/MOSI)         -----           Pin 20 (GND)
# Pin 21 (GPIO 9/MISO)          -----           Pin 22 (GPIO 25)
# Pin 23 (GPIO 11/SCLK)         -----           Pin 24 (GPIO 8/CE0)
# Pin 25 (GND)                  -----           Pin 26 (GPIO 7/CE1)
# Pin 27 (ID_SD/EEPROM)         -----           Pin 28 (ID_SC/EEPROM)
# Pin 29 (GPIO 5)               -----           Pin 30 (GND)
# Pin 31 (GPIO 6)               -----           Pin 32 (GPIO 12/PWM0)
# Pin 33 (GPIO 13/PWM1)         -----           Pin 34 (GND)
# Pin 35 (GPIO 19/MISO)         -----           Pin 36 (GPIO 16/CE2)
# Pin 37 (GPIO 26)              -----           Pin 38 (GPIO 20/MOSI)
# Pin 39 (GND)                  -----           Pin 40 (GPIO 21/SCLK)

#Suppress warnings
GPIO.setwarnings(False)

#assign some pins for the motors
ltFwdMtr = 3
ltRevMtr = 5
rtFwdMtr = 8
rtRevMtr = 10
motorPins = [ltFwdMtr, ltRevMtr, rtFwdMtr, rtRevMtr]

# set pins as output pins
for pin in motorPins:
    GPIO.setup(pin, GPIO.OUT)
    
#set up controller
controller = InputDevice('/dev/input/event12')
print (controller)

def runMotors():
	print('Running Motors')
	#set all pins to off position
	for pin in motorPins:
		pin = GPIO.LOW
	
	for event in controller.read_loop():
		if event.type == ecodes.EV_KEY:
			print(str(event.code) + ' : ' + str(event.value))
			
			if event.code == 310:
				if event.value == 1: 
					ltFwdMtr = GPIO.HIGH
					print('ltFwdMtr on')
				if event.value == 0: 
					ltFwdMtr = GPIO.LOW
					print('ltFwdMtr off')

			if event.code == 312:
				if event.value == 1:
					ltRevMtr = GPIO.HIGH
					print('ltRevMtr on')
				if event.value == 0:
					ltRevMtr = GPIO.LOW
					print('ltFwdMtr off')
					
			if event.code == 311:
				if event.value == 1: 
					ltFwdMtr = GPIO.HIGH
					print('rtFwdMtr on')
				if event.value == 0: 
					ltFwdMtr = GPIO.LOW
					print('ltFwdMtr off')

			if event.code == 313:
				if event.value == 1:
					ltRevMtr = GPIO.HIGH
					print('ltRevMtr on')
				if event.value == 0:
					ltRevMtr = GPIO.LOW
					print('ltFwdMtr off')
	
runMotors()

