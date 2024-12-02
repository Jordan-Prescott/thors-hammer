from pydantic import BaseModel, Field
from typing import Any, Dict


class BroadworksCommand(BaseModel):
    """
    Base class for all BroadWorks commands.

    Attributes:
        command (str): The name of the BroadWorks command.
        params (Dict[str, Any]): Parameters for the command.
    """

    command: str = Field(..., exclude=True)
    params: Dict[str, Any] = Field(default_factory=dict, exclude=True)

    def to_dict(
        self,
    ) -> Dict[
        str, Any
    ]:  # TODO: This may not be needed as pydantic has inbuilt dict method
        """
        Convert the command into a dictionary format.

        Returns:
            Dict[str, Any]: A dictionary containing the command and its parameters.
        """
        return {
            "command": self.command,
            "params": self.dict(exclude_unset=True, exclude={"command", "params"}),
        }
