import json_schema


class YamlConfig(Config):
    # format { pol_type: [{pol_name: pol_content}] }
    def __init__(self):
        self._config = {}

    def set_config(self, config):
        if YamlConfig.validate_config(config):
            self._config = config
            return True
        return False

    @staticmethod
    def validate_config(config):
        schema = {
            "type": "object",
            "properties": {
                "usersg-policies": {
                    "type": "object",
                    "patternProperties": {
                        '[^/]+': {
                            "type": "object",
                        }
                    }
                },
                "hostsg-policies": {
                    "type": "object",
                    "patternProperties": {
                        '[^/]+': {
                            "type": "object",
                        }
                    }
                }
            }
        }
        try:
            json_schema.validate(config, schema)
        except Exception as e:
            # TODO process error
            return False
        return True

    def add_policy(self, pol_type, pol_name, pol_content):
        if not self._config.has_key(self, pol_type):
            self._config[pol_type] = {}
        self._config[pol_type][pol_name] = pol_content

    def all_policies_types(self):
        return self._config.keys()

    def all_policy_names(self, pol_type):
        if self._config.has_key(pol_type):
            return self._config[pol_type]
        else:
            return []

    def get_policy_content(self, pol_type, pol_name):
        if self._config.has_key(pol_type) and self._config[pol_type].has_key(pol_name):
            return self._config[pol_type][pol_name]
        else:
            return None
