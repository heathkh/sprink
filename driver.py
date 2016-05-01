#!/usr/bin/python
import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


import atexit


def cleanup():
	# turn all channels "on" -> all relays off
    sprink = SprinklerDriver()
    sprink._all_off()
    return

atexit.register(cleanup)

 
class SprinklerDriver(object):
    def __init__(self):
        
        self._pin_pump = 11
        self._zone_to_pin = { 1 : 12,
                             2 : 13,
                             3 : 15 }
        
        # use board index scheme so mapping will work with different hardware versions
        GPIO.setmode(GPIO.BOARD)
        
        self._all_pins = self._zone_to_pin.values()
        self._all_pins.append(self._pin_pump)
        # relay board uses reversed logic (high = off)
        GPIO.setup(self._all_pins, GPIO.OUT, initial=1) 
        return
    
    def _all_off(self):
        GPIO.output(self._all_pins, 1)
        return

    
    def set_active_zone(self, zone_num):
        self._all_off()

        if zone_num is None:
            return

                
        pin = self._zone_to_pin[zone_num]
        GPIO.output(pin, 0)
        GPIO.output(self._pin_pump, 0)
        
        return
        
        
            
    