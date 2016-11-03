import ValidateUsersgPoliciesForYaml
import ValidateHostsgPoliciesForYaml


ORDER_VALIDATE_HOSTSGPOLICIES = 0
ORDER_VALIDATE_USERSGPOLICIES = 0


def add_argument(parser):
    parser.add_argument("--validate_ug", dest="actions", action="append", type=ValidateUsersgPoliciesForYaml)
    parser.add_argument("--validate_hg", dest="actions", action="append", type=ValidateHostsgPoliciesForYaml)


def validate_args(args):
    return True
