import hvac.Client

import Connect
import vault_acl_tool.actions.connect.ORDER_CONNECT_CERKEY as ORDER_CONNECT_CERKEY


class ConnectCertKey(Connect):
    def __init__(self, args):
        super(type(self), self).__init__()
        self._name = "ConnectCertKey"
        self._order += ORDER_CONNECT_CERKEY
        self._cert = args[2]
        self._key = args[1]
        self._url = args[0]

    def connect(self):
        try:
            self._client = hvac.Client(self._url, cert=(self._cert, self._key))
            self._client.auth_tls(use_token=True)
        except Exception as e:
            # TODO process error
            return False
        return True
