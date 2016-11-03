import hvac.Client

import vault_acl_tool.actions.connect.ORDER_CONNECT_USERPASSWD as ORDER_CONNECT_USERPASSWD
import Connect


class ConnectUserPasswd(Connect):
    def __init__(self, args):
        super(type(self), self).__init__()
        self._order += ORDER_CONNECT_USERPASSWD
        self._name = "ConnectUserPasswd"
        self._username = args[1]
        self._password = args[2]
        self._url = args[0]

    def connect(self):
        try:
            self._client = hvac.Client(self._url)
            self._client.auth_userpass(username=self._username, password=self._password, user_token=True)
        except Exception as e:
            # TODO process error
            return False
        return True
