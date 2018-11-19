import sys

class Color:
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"

HELP_MESSAGE = """{0}Avalibale Flags:
{1}-h     {3}Help.
{1}-si    {3}Run with command line interface (Shell Interface)""".format(Color.CYAN, Color.BLUE, Color.REVERSE, Color.RESET)

def get_flags_from_argv(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            try:
                opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
            except:
                opts[argv[0]] = None  # Add key and `None` to the dictionary.
        # Reduce the argument list by copying it starting from index 1.
        argv = argv[1:]
    return opts

if __name__ == '__main__':
    flags = get_flags_from_argv(sys.argv)
    if '-h' in flags:
        print(HELP_MESSAGE)
    else:
        if '-si' in flags:
            # yORn = raw_input("Do you sure to publishing version %s: (y/n)  " % (NEW_VERSION))
            print 'shell'