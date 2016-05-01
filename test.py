#!/usr/bin/python
import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


def cleanup():
	# turn all channels "on" -> all relays off
	return

 
class SprinkerDriver(object):
    def __init__(self):
        
        self._channel_pump = 11
        self._channel_valve_1 = 12
        self._channel_valve_2 = 13
        self._channel_valve_3 = 15
        
        
        
        return
    
    




# use board index scheme so mapping will work with different hardware versions
GPIO.setmode(GPIO.BOARD)


channel_list = [ 11, 12, 13, 15]
# channel_list = [  15]
GPIO.setup(channel_list, GPIO.OUT, initial=GPIO.HIGH) 


while True:
	for channel in channel_list:
		time.sleep(1)
		print 'on'
		GPIO.output(channel, 0)
		time.sleep(1)
		print 'off'
		GPIO.output(channel, 1)
