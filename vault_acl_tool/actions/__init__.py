import validate
import load
import connect
import diff
import apply

ORDER_CONNECT = 100
ORDER_LOAD = 200
ORDER_VALIDATE = 300
ORDER_DIFF = 400
ORDER_APPLY = 500
POLICY_TYPES = ["", "usersg-policies", "hostsg-policies"]


def add_argument(parser):
    parser.add_argument("--cont_on_fail", action="store_true", default=False)

    # submodules arguments
    validate.add_argument(parser)
    load.add_argument(parser)
    connect.add_argument(parser)
    apply.add_arguments(parser)


def validate_args(args):
    return load.validate_args(args) and validate.validate_args(args) and connect.validate_args(args) \
            and apply.validate_args(args)

