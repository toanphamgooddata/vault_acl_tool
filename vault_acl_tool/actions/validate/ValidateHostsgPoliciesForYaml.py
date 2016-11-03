import vault_acl_tool.actions.validate.ORDER_VALIDATE_HOSTSGPOLICIES as ORDER_VALIDATE_HOSTSGPOLICIES
import Validate


class ValidateHostsgPoliciesForYaml(Validate):
    def __init__(self):
        super(type(self), self).__init__()
        self._name = "ValidateHostgPolicies"
        self._order += ORDER_VALIDATE_HOSTSGPOLICIES
        self._schema = {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "content": {
                    "type": "object",
                    "patternProperties": {
                        "^[^*/]+(/[^*/]+)*/?\*?$": {
                            "type": "object",
                            "oneOf": [
                                {
                                    "properties": {
                                        "capabilities": {
                                            "type": "array",
                                            "enum": ["deny", "read"]
                                        }
                                    }
                                },
                                {
                                    "properties": {
                                        "policy": {
                                            "type": "array",
                                            "enum": ["read", "deny"]
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    "additionalProperties": False
                }
            }
        }

    def extract_policies_for_validate(self, context):
        return context.config().get_policies_type("hostsg-policies")
