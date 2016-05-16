#!/usr/bin/python
import driver
import gflags
import cli

FLAGS = gflags.FLAGS
gflags.DEFINE_integer('zone', None, 'ID of the zone')
gflags.DEFINE_boolean('on', True, 'Desired state of the zone')


def main():
    cli.init()
    driver.set_zone(FLAGS.zone, FLAGS.on)
    
    print driver.get_zone_states()
    
    return

    
if __file__ == "__main__":
    main()