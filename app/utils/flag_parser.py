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
