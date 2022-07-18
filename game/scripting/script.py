class Script:
    """
    A collection of actions.

    The responsibility of Script is to keep track of a collection of actions.
    It has methods for adding, removing and getting them by a group name.

    Attributes:
        _actions (dict): A dictionary of actions { key: group_name, value: a list of actions }
    """
    def __init__(self):
        """
        Constructs a new Action.
        """
        self._actions = {}

    def add_action(self, group, action):
        """
        Adds an action to the given group.

        Args:
            group (string): The name of the group.
            action (Action): The action to add.
        """
        if not group in self._actions.keys():
            self._actions[group] = []