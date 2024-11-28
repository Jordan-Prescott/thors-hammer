class BroadworksCommand:
    """
    Base class for all BroadWorks commands.
    """

    def __init__(self, command: str, **kwargs):
        """
        Initialize the command with a name and parameters.

        Args:
            command (str): The name of the BroadWorks command.
            **kwargs: Parameters for the command.
        """
        self.command = command
        self.params = kwargs

    def to_dict(self):
        """
        Convert the command into a dictionary format.

        Returns:
            dict: Command and parameters.
        """
        return {
            "command": self.command,
            "params": {k: v for k, v in self.params.items() if v is not None},
        }
