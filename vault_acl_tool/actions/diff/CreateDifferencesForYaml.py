import vault_acl_tool.actions.diff.ORDER_CREATEDIFFERENCES as ORDER_CREATEDIFFERENCES
import vault_acl_tool.actions.diff.
import Differences

class CreateDifferencesForYaml(ToolAction):
    def __init__(self):
        super(type(self), self).__init__()
        self._order += ORDER_CREATEDIFFERENCES
        self._diff = Differences()

    def _delete_types(self, config, srv_config):
        config_types = config.all_policies_types()
        srv_types = srv_config.all_policies_types()
        new_types = [t for t in config_types if t not in srv_types]
        for t in del_types:
            for p in srv_config.all_policies_for_type(t):
                self._diff.delete_policy(t, config.get_policy_name(p))

    def _new_types(self, config, srv_config):
        config_types = config.all_policies_types()
        srv_types = srv_config.all_policies_types()
        new_types = [t for t in config_types if t not in srv_types]
        for t in new_types:
            for p in config.all_policies_types(t):
                self._diff.update_policy_content(t, config.get_policy_type(p), config.get_policy_content(p))

    def _update(self, config, srv_config):
        config_types = config.policies_types()
        srv_types = srv_config.policies_types()
        update_types = [t for t in srv_types if t in config_types]
        for t in update_types:
            srv_names = srv_config.all_policy_names(t)
            config_names = config.all_policy_names(t)

            for n in srv_names:
                if not n in config_names:
                    self._diff.delete_policy(t, n)

            for n in config_names:
                if n in srv_names:
                    # check if content is changed
                    srv_content = srv_config.get_policy_content(t, n)
                    conf_content = config.get_policy_config(t, n)
                else:
                    self._diff.delete_policy(t, n)

    def diff(self, config, srv_config):
        self._delete_types(config, srv_config)
        self._new_types(config, srv_config)
        self._update(config,srv_config)
        return True
