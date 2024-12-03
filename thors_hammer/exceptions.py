class THError(Exception):
    """base class for exceptions in Thors Hammer."""

    def __str__(self) -> str:
        return "My hammer isn't working."
