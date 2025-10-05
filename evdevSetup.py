#import evdev necessary components
from evdev import InputDevice, categorize, ecodes
#configure controller
controller = InputDevice('/dev/input/event12')

#get controller info
print(controller)


#check inputs
for event in controller.read_loop():
	if event.type == ecodes.EV_KEY:
		print(str(event.code) + ' : ' + str(event.value))

#BTN_TL, EVENT CODE 310= LEFT SHOULDER
#BTN_TL2, EVENT CODE 312 = LEFT TRIGGER
#BTN_TR, EVENT CODE 311 = RIGHT SHOULDER
#BTN_TR2, EVENT CODE 313 = RIGHT TRIGGER
