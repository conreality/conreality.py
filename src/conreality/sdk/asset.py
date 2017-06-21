# This is free and unencumbered software released into the public domain.

from .object import Object

class Asset(Object):
    """An asset."""

    def __init__(self, uuid=None):
        super().__init__(uuid=uuid)

    def __repr__(self):
        """Returns a human-readable string representation of this object."""
        return "asset{{uuid={}}}".format(self.uuid)

    def __str__(self):
        """Returns a human-readable string representation of this object."""
        return self.__repr__()
