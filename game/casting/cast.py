class Cast:
    """
    A collection of actors.

    The responsibility of a cast is to keep track of a collection of actors.
    It has methods for adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """
    def __init__(self):
        """
        Constructs a new actor.
        """
        self._actors = {}

    def add_actors(self, group, actor):
        """
        Adds an actor to the given group.

        Args:
            group: (string): The name of the group.
            actor: (Actor): The actor to add.
        """
        if not group in self._actors.keys():
            self._actors[group] = []

        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        """
        Gets the actors in the given group.

        Args:
            group (string): The name of the group.

        Returns:
            List: The actors in the group.
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()