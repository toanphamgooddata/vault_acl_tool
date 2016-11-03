import LoadYamlConfig


ORDER_LOADYAMLCONFIG = 0


def add_argument(parser):
    parser.add_argument("--yaml", dest="actions", action="append",
                        type=LoadYamlConfig, nargs=1, required=True)


def validate_args(args):
    return True
