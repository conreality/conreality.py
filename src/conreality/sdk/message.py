# This is free and unencumbered software released into the public domain.

class Message:
    """A message."""

    def __init__(self, id=None):
        self.id = id

    def __repr__(self):
        """Returns a human-readable string representation of this object."""
        return "message{{id={}}}".format(self.id)

    def __str__(self):
        """Returns a human-readable string representation of this object."""
        return self.__repr__()
