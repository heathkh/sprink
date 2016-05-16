
import sys
import gflags
def init():
    """ Call this first thing in main to parse flags and configure logging. 
    
    If any required flags are missing, prints the help guide and exits.

    Python scripts can have a common user-friendly behavior without all the
    boilerplate code.
    
    Returns:
        argv with only positional arguments
    """
    argv = sys.argv
    try:
        positional_args = gflags.FLAGS(argv)  # parse flags
    except gflags.FlagsError, e:
        print '%s\nUsage: %s ARGS\n%s' % (e, sys.argv[0], gflags.FLAGS.MainModuleHelp())
        sys.exit(1)
    
    return positional_args