import sys
from app import shell
from app.utils import Color, get_flags_from_argv


HELP_MESSAGE = """{0}Avalibale Flags:
{1}-h     {3}Help.
{1}-yes   {3}Answer yes to all yes or no questions
{1}-si    {3}Run with command line interface {2}(Shell Interface){3}""".format(Color.CYAN, Color.BLUE, Color.REVERSE, Color.RESET)


if __name__ == '__main__':
    flags = get_flags_from_argv(sys.argv)
    yes_to_all = False
    if '-h' in flags:
        # print(HELP_MESSAGE)
        pass
    else:
        if '-si' in flags:
            pass  # add graohical then use this flag
        if '-yes' in flags:
            yes_to_all = True
    shell(yes_to_all)
