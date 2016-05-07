#!/usr/bin/python
import time
import atexit



try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
    raise
except ImportError:
    print 'Only mock driver is available'
    GPIO = None

if GPIO:
    def cleanup():
    	# turn all channels "on" -> all relays off
        sprink = SprinklerDriver()
        sprink._all_off()
        print 'CLEANUP CALLED!'
        return
    

     
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
    

        def set_zone(self, zone_num, zone_state):
            pin = self._zone_to_pin[zone_num]
            GPIO.output(pin, not zone_state) # note pin on -> zone off 
            
            # need pump on if any zones are on
            need_pump = False
            for pin in self._zone_to_pin.itervalues():
                if GPIO.input(pin) == 0: # pin off -> zone on
                    need_pump = True
                    break
            
            
            GPIO.output(self._pin_pump, not need_pump)
            
            return

class MockSprinklerDriver(object):
    def __init__(self):
        return
    
    def set_zone(self, zone_num, zone_state):
        print 'Setting zone %s to state %s' % (zone_num, zone_state)
        return

def mock_cleanup():
        print 'CLEANUP CALLED!'
        return
   

def get_driver():
    if GPIO:
        atexit.register(cleanup)
        return SprinklerDriver()
    else:
        atexit.register(mock_cleanup)
        return MockSprinklerDriver()
            
        
            
    