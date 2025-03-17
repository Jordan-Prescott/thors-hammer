from typing import Dict, Any

from . import scripts
from .api import API


class Scripter:
    """This object acts as the gateway to all pre-written scripts in /scripts/.


    Each api object created creates its own associated Scripter object on api creation.
    Additionally, this object can be created solely and passed an api, however, this
    will result in two exact Scripter objects.

    Intended use: odin_api.scripter.{script function}

    :param api: api object in package odin_api, this is used in the scripts to achieve objective.
    """

    __instance = None

    @staticmethod
    def get_instance(api: API = None) -> "Scripter":
        """
        Singleton implementation for Scripter object.

        Args:
            api (API): API object to be used in the scripts.
        """
        if Scripter.__instance is None:
            Scripter(api)
        return Scripter.__instance

    def __init__(
        self,
        api: API,
    ) -> None:
        if Scripter.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.api = api

    def _run_script(self, script_name: str, *args, **kwargs) -> Dict[str, Any]:
        """Dynamically runs the specified script."""
        self.api.logger.debug(
            f"Script {script_name} executed, args: {[args]}, kwargs: {kwargs}"
        )
        try:
            script_function = getattr(scripts, script_name)
            self.api.logger.info(f"Script {script_name} executed")
        except AttributeError:
            self.api.logger.error(
                f"Script failed to execute, error: Script '{script_name}' not found."
            )
            raise AttributeError(
                f"Script '{script_name}' not found in 'scripts' module."
            )
        return script_function(self.api, *args, **kwargs)

    def find_alias(
        self, *, service_provider_id: str, group_id: str, alias: int
    ) -> Dict[str, any]:
        """Locates alias if assigned to broadworks entity.

        Args:
            service_provider_id (str): Service Prodiver where group is hosted.
            group_id (str): Group where alias is located.
            alias (int): Alias number to identify e.g. 0

        Raises:
            THAliasNotFound: If alias not found THAliasNotFound error raised

        Returns:
            Dict: Returns type and name/ userId of entity where alias located.

        """
        return self._run_script("find_alias", service_provider_id, group_id, alias)
