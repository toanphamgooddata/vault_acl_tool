class ToolAction(object):
    def __init__(self):
        self._name = "ToolAction"
        self._order = 0

    def name(self):
        return self._name

    def order(self):
        return self._order

    def dependencies(self):
        # returns the type of itself mean that it doesn't require any action
        return [type(self)]

    def create_dependencies(self):
        pass

    def check_required_actions(self, actions):
        deps = self.dependencies()
        for a in actions:
            for t in deps:
                if isinstance(a, t):
                    deps.remove(t)
        return len(deps) == 0

    def execute(self, context):
        pass

    @staticmethod
    def get_order(action):
        return action.order()
