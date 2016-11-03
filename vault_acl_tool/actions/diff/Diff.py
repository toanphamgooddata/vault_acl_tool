import vault_acl_tool.actions.ToolAction as ToolAction
import vault_acl_tool.actions.load.LoadConfig as LoadConfig
import vault_acl_tool.actions.connect.Connect as Connect
import vault_acl_tool.actions.ORDER_DIFF as ORDER_DIFF


class Diff(ToolAction):
    def __init__(self):
        super(type(self), self).__init__()
        self._order += ORDER_DIFF
        self._differences = None

    def dependencies(self):
        # returns the type of itself mean that it doesn't require any action
        return [LoadConfig, Connect]

    def diff(self, config, srv_config):
        pass

    def execute(self, context):
        if not self.diff(context.config(), context.srv_config()):
            return False
        context.set_diff(self._differences)
        return True
