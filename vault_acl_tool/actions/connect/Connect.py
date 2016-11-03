import vault_acl_tool.actions.ToolAction
import vault_acl_tool.actions.CONNECT_ORDER
import vault_acl_tool.config.YamlConfig as YamlConfig


class Connect(vault_acl_tool.actions.ToolAction):
    def __init__(self):
        super(type(self), self).__init__()
        self._name = "Connect"
        self._order = vault_acl_tool.actions.CONNECT_ORDER
        self._client = None
        self._srv_config = YamlConfig()

    def connect(self):
        pass

    @staticmethod
    def get_policy_type_name(policy_name):
        if '/' not in policy_name:
            return "", policy_name
        else:
            index = policy_name.index('/')
            return policy_name[:index], policy_name[index+1:]

    def load_single_policy(self, full_pol_name):
        policy_type, pol_name = Connect.get_policy_type_name(full_pol_name)
        pol_content = self._client.get_policy(pol_name)
        if pol_content is None:
            # TODO raise exception
            return False
        self._srv_config.add_policy(policy_type, pol_name, pol_content)

    def load_policies(self):
        pol_list = self._client.list_policies()
        if pol_list is None:
            # TODO: raise exception
            return False
        for full_pol_name in pol_list:
            if not self.load_single_policy(full_pol_name):
                return False
        return True

    def execute(self, context):
        if not self.connect():
            # TODO process error here
            context.terminate()
            return False
        else:
            context.set_client(self._client)

        if not self.load_policies(self):
            context.terminate()
            return False
        else:
            context.set_srv_config(self._srv_config)
