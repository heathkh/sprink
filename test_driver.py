#!/usr/bin/python
import time
import driver

def main():
    sprink = driver.SprinklerDriver()
    
    while True:
        for i in [1,2,3]:
            sprink.set_active_zone(i)
            time.sleep(1)
            
if __name__ == '__main__':
    main()