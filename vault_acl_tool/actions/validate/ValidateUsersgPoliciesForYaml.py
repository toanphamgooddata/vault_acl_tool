import Validate
import vault_acl_tool.actions.validate.ORDER_VALIDATE_HOSTSGPOLICIES as ORDER_VALIDATE_HOSTSGPOLICIES


class ValidateUsersgPoliciesForYaml(Validate):
    def __init__(self):
        super(type(self), self).__init__()
        self._name = "ValidateUsersgPoliciesForYaml"
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
                                            "enum": ["deny", "write", "read"]
                                        }
                                    }
                                },
                                {
                                    "properties": {
                                        "policy": {
                                            "type": "array",
                                            "enum": [
                                                "create", "read", "update",
                                                "delete", "list", "deny"
                                            ]
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
        return context.config().get_policies_type("usersg-policies")
