import json_schema
import os.path
import yaml

import vault_acl_tool.actions.load.ORDER_LOADYAMLCONFIG as ORDER_LOADYAMLCONFIG
import vault_acl_tool.config.YamlConfig as YamlConfig
import LoadConfig


class LoadYamlConfig(LoadConfig):
    def __init__(self, path):
        super(type(self), self).__init__(path)
        self._order += ORDER_LOADYAMLCONFIG
        self._name = "LoadYamlConfig"
        self._config = YamlConfig()
        yaml.add_contruction("!include", self._yaml_include)

    def _yaml_include(self, loader, node):
        """
        Include another yaml file from main file
        This is usually done by registering !include tag
        """
        file_path = os.path.join(os.path.dirname(self._path), node.value)
        try:
            with open(file_path, 'r') as input_file:
                return yaml.load(input_file)
        except Exception as e:
            # TODO: process error
            raise

    def load(self):
        try:
            with open(self._path) as fh:
                config = yaml.load(fh)
        except Exception as e:
            # TODO: process error
            return False
        return self._config.set_config(config)
