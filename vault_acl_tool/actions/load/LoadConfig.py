import os.path
import vault_acl_tool.actions.ORDER_LOAD as ORDER_LOAD


class LoadConfig(ToolAction):
    def __init__(self, path):
        super(type(self), self).__init__()
        self._order = ORDER_LOAD
        self._path = path
        self._config = None

    # for sub class overwrite
    def load(self):
        pass

    def execute(self, context):
        if not os.path.isfile(self._path):
            # TODO process error here
            context.terminate()
            return False
        if not self.load():
            # TODO process error here
            context.terminate()
            return False
        else:
            context.set_config(self._config)
            return True
