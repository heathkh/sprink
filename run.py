#!/usr/bin/python
"""

TODO: add reporting to cloudwatch so we can monitor and alert on missed watering
"""

import time
import driver
import time
import datetime
import signal
import time
import sys

class SignalHandler:
  exit_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)
    return

  def exit_gracefully(self,signum, frame):
    self.exit_now = True
    return


class ActiveInterval(object):
    def __init__(self, on_time, off_time):
        if off_time < on_time:
            raise RuntimeError('off time must be after on time')
        self.on_time = on_time
        self.off_time = off_time
        return
    
    def is_active(self):
        now = datetime.datetime.now().time()
        is_active = False
        if now > self.on_time and now <  self.off_time:
            is_active = True
        return is_active
        
        
class SimpleScheduler(object):
    def __init__(self):
        self._driver = driver.get_driver()
        self._zone_intervals = {}
        return
    
    def add(self, zone, on_time, off_time):
        if zone not in [1,2,3,None]:
            raise RuntimeError('Invalid zone')
        interval = ActiveInterval(on_time, off_time)
        if zone not in self._zone_intervals:
            self._zone_intervals[zone] = []
        self._zone_intervals[zone].append(interval)
        return
    
    def run(self):
        signals = SignalHandler()
        while True:
            print '%s : Updating' % (datetime.datetime.now())
            if signals.exit_now:
                print 'Exiting from signal...'
                break
            for zone, intervals in self._zone_intervals.iteritems():
                is_active = False
                for interval in intervals:
                    if interval.is_active():
                        is_active = True
                        break
                self._driver.set_zone(zone, is_active)
            time.sleep(60)
        return
    
    
            

def schedule_cycle(scheduler, start_time, duration, zones = [1,2,3]):
    # Need to convert from time to datetime so we can do arthmetic with timedelta, then convert back to time object
    phase_start_time = datetime.datetime.combine(datetime.date.today(), start_time)
    for zone in zones:
        phase_end_time = phase_start_time + duration
        scheduler.add(zone, phase_start_time.time(), phase_end_time.time())
        phase_start_time += duration
    return
        
    
    

def main():
    scheduler = SimpleScheduler()
    
    schedule_cycle(scheduler, datetime.time(8,00), datetime.timedelta(minutes=5))
    schedule_cycle(scheduler, datetime.time(13,00), datetime.timedelta(minutes=5))
    
    scheduler.run()
    return
            
if __name__ == '__main__':
    main()