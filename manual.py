#!/usr/bin/python
import driver
import gflags
import cli

FLAGS = gflags.FLAGS
gflags.DEFINE_integer('zone', None, 'ID of the zone')
gflags.DEFINE_boolean('on', True, 'Desired state of the zone')

gflags.MarkFlagAsRequired('zone')

def main():
    cli.init()
    sprink = driver.SprinklerDriver()
    sprink.set_zone(FLAGS.zone, FLAGS.on)
    print sprink.get_zone_states()
    return

    
if __name__ == "__main__":
    main()