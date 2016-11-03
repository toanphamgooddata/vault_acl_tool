import Context
import ToolAction


class ActionChain:
    def __init__(self, actions, args):
        # allocate a context for actions
        # it is a storage for global data: hvac client, config, differences
        self._context = Context(args.cont_on_fail)
        cont = True
        self._actions = actions
        while cont:
            new_actions = []
            for a in self._actions:
                if not a.check_required_actions(self._actions + new_actions):
                    new_actions.append(a.create_dependencies())
            cont = len(new_actions) == 0
            self._actions = actions + new_actions
        self._actions.sort(key=ToolAction.get_order)

    def execute(self):
        for a in self._actions:
            print("Execute Action %s" % a.name())
            if (not a.execute(self._context) and not self._context.cont_on_fail()) \
               or self._context.is_terminated():
                print("Terminate")
                break
