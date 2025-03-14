from broadworks_ocip import BroadworksAPI


class API:
    """
    Wrapper around BroadworksAPI to enhance usability and provide additional features.
    """

    def __init__(self, host, username, password, port=2209, logger=None, **kwargs):
        """
        Initialize the wrapper with the required connection details.

        Args:
            host (str): The hostname or IP address of the OCI-P server.
            username (str): The username to authenticate with.
            password (str): The password to authenticate with.
            port (int, optional): The port to connect to. Defaults to 2208.
            logger (Logger, optional): A custom logger instance.
            **kwargs: Additional parameters to pass to the BroadworksAPI.
        """
        self.api = BroadworksAPI(
            host=host,
            username=username,
            password=password,
            port=port,
            logger=logger,
            **kwargs,
        )
        self.logger = logger

    def authenticate(self):
        """
        Authenticate with the OCI-P server.

        Returns:
            Response: The response object from the server.
        """
        return self.api.authenticate()

    def close(self):
        """
        Close the connection to the OCI-P server.
        """
        self.api.close()

    def command(self, command_instance):
        """
        Send a command to the OCI-P server using a command class instance.

        Args:
            command_instance (object): An instance of a command class with a `command` and `params` attribute.

        Returns:
            Response: The response object from the server.
        """
        if not hasattr(command_instance, "command") or not hasattr(
            command_instance, "params"
        ):
            raise ValueError(
                "Command instance must have `command` and `params` attributes."
            )

        return self.api.command(command_instance.command, **command_instance.params)

    def is_authenticated(self):
        """
        Check if the connection is authenticated.

        Returns:
            bool: True if authenticated, False otherwise.
        """
        return self.api.authenticated

    def connect(self):
        """
        Open a connection to the OCI-P server.
        """
        self.api.connect()

    def send_command(self, command, **kwargs):
        """
        Build and send XML for a command and its parameters.

        Args:
            command (str): The command name.
            **kwargs: The parameters for the command.

        Returns:
            None
        """
        self.api.send_command(command, **kwargs)
