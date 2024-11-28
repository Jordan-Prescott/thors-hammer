from typing import Any, Dict


class BroadworksCommand:
    """
    Base class for all BroadWorks commands.

    Attributes:
        command (str): The name of the BroadWorks command.
        params (Dict[str, Any]): Parameters for the command.
    """

    def __init__(self, command: str, **kwargs: Any) -> None:
        """
        Initialize the command with a name and parameters.

        Args:
            command (str): The name of the BroadWorks command.
            **kwargs: Arbitrary keyword arguments representing command parameters.
        """
        self.command: str = command
        self.params: Dict[str, Any] = kwargs

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the command into a dictionary format.

        Returns:
            Dict[str, Any]: A dictionary containing the command and its parameters.
        """
        return {
            "command": self.command,
            "params": {k: v for k, v in self.params.items() if v is not None},
        }
