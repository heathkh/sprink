#!/usr/bin/python
import driver
import gflags
import sys

FLAGS = gflags.FLAGS
gflags.DEFINE_integer('zone', None, 'ID of the zone')
gflags.DEFINE_bool('state', None, 'Desired state of the zone')

gflags.MarkFlagAsRequired('zone')
gflags.MarkFlagAsRequired('state')

def main():
    argv = sys.argv
    try:
        positional_args = gflags.FLAGS(argv)  # parse flags
    except gflags.FlagsError, e:
        print '%s\nUsage: %s ARGS\n%s' % (e, sys.argv[0], gflags.FLAGS.MainModuleHelp())
        sys.exit(1)
    
    sprink = driver.SprinklerDriver()
    sprink.set_zone(FLAGS.zone, FLAGS.state)
    print sprink.get_zone_states()
    return

    
if __name__ == "__main__":
    main()