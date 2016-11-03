import PrintDiff
import Apply

ORDER_PRINTDIFF = 0
ORDER_APPLY = 1

def add_argument(parser):
    parser.add_argument("--diff", dest="actions", action="append", type=PrintDiff)
    parser.add_argument("--apply", dest"actions", action="append", type=Apply)


def validate_args(args):
    return True
