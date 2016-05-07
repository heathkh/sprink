#!/usr/bin/python
import time
import driver
import time
import datetime


class ActiveInterval(object):
    def __init__(self, on_time, off_time):
        if off_time < on_time:
            raise RuntimeError('off time must be after on time')

        self.on_time = on_time
        self.off_time = off_time
        return
    
    def is_active(self):
        now = datetime.datetime.now().time()

        print now
        
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
        
        while True:
            print 'Checking...'
            for zone, intervals in self._zone_intervals.iteritems():
                is_active = False
                for interval in intervals:
                    if interval.is_active():
                        is_active = True
                        break
                self._driver.set_zone(zone, is_active)
            
            time.sleep(1)
            

def main():
    
    scheduler = SimpleScheduler()
    
    offset = datetime.datetime.now()
    for i in range(10):
        offset = offset + datetime.timedelta(seconds=10)
        start = offset
        end = start + datetime.timedelta(seconds=5)
        scheduler.add(1, start.time(), end.time())
    
    
    scheduler.run()
    return
            
if __name__ == '__main__':
    main()