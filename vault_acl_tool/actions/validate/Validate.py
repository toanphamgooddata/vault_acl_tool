import json_schema

import vault_acl_tool.actions.load.LoadConfig as LoadConfig
import vault_acl_tool.actions.ORDER_VALIDATE as ORDER_VALIDATE
import vault_acl_tool.actions.ToolAction as ToolAction


class Validate(ToolAction):
    def __init__(self):
        super(type(self), self).__init__()
        self._name = "Validate"
        self._order = ORDER_VALIDATE
        self._schema = {"type": "object"}

    def validate_with_schema(self, cont_on_fail=False, policies=[]):
        for p in policies:
            try:
                json_schema.validate(self._schema, p)
            except Exception as e:
                # TODO process error here
                if not cont_on_fail:
                    return False
        return True
    
    def extract_policies_for_validate(self, context):
        return []
    
    def execute(self, context):
        policies = self.extract_policies_for_validate(context)
        return self.validate_with_schema(context.cont_on_fail(), policies)

    def dependencies(self):
        return [LoadConfig]
