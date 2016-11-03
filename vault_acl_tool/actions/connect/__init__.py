import vault_acl_tool.actions.connect.ConnectCertKey
import vault_acl_tool.actions.connect.ConnectLdap
import vault_acl_tool.actions.connect.ConnectUserPasswd
import vault_acl_tool.actions.ORDER_CONNECT as ORDER_CONNECT


ORDER_CONNECT_CERKEY = 0
ORDER_CONNECT_LDAP = 0
ORDER_CONNECT_USERPASS = 0


def add_argument(parser):
    # --connect_ldap server username password
    parser.add_argument("--connect_ldap", nargs=3, action="append", dest="actions", type=ConnectLdap)
    # --connect_userpasswd server username password
    parser.add_argument("--connect_userpasswd", nargs=3, action="append", dest="actions", type=ConnectUserPasswd)
    # --connect_cert server key cert
    parser.add_argument("--connect_certkey", nargs=3, action="append", dest="actions", type=ConnectCertKey)


def validate_args(args):
    no_connect_act = 0
    for a in args.actions:
        if a.order() == ORDER_CONNECT:
            no_connect_act += 1
    if no_connect_act != 1:
        return False
    return True
