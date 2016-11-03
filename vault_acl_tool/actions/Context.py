class Context:
    def __init__(self, cont_on_fail=False):
        self._config = None
        self._client = None
        self._cont_on_fail = cont_on_fail
        self._terminated = False
        self._differences = None
        self._srv_config = None

    def set_srv_config(self, config):
        self._srv_config = config

    def srv_config(self):
        return self._srv_config

    def set_config(self, config):
        self._config = config

    def config(self):
        return self._config

    def set_client(self, client):
        self._client = client

    def client(self):
        return self._client

    def set_diff(self, differences):
        self._differences = differences

    def differences(self):
        return self._differences

    def cont_on_fail(self):
        return self._cont_on_fail

    def terminate(self):
        self._terminated = True

    def is_terminated(self):
        return self._terminated
