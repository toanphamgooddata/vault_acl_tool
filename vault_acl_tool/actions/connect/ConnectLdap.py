import hvac.Client

import vault_acl_tool.actions.connect.ORDER_CONNECT_LDAP as ORDER_CONNECT_LDAP
import Connect


class ConnectLdap(Connect):
    def __init__(self, args):
        super(type(self), self).__init__()
        self._order += ORDER_CONNECT_LDAP
        self._name = "ConnectLdap"
        self._username = args[1]
        self._password = args[2]
        self._url = args[0]

    def connect(self):
        try:
            self._client = hvac.Client(self._url)
            self._cilent.auth_ldap(username=self._username, password=self._password, user_token=True)
        except Exception as e:
            # TODO process error
            return False
        return True
