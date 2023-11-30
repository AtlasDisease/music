# Created By: Brendan (@AtlasDisease)
# Copyright: 2023
# Description: Artist

# --- Imports --- #

from typing import Self
from dataclasses import dataclass, field

try:
    from .genres import Genre
except:
    from genres import Genre

__all__ = ("Artist",)


# --- Artist Class --- #

@dataclass(slots = True)
class Artist:
    name: str
    genre: Genre = field(default = Genre.OTHER)
    bio: str = ""

    def __str__(self):
        return self.name

    def __format__(self, format_spec = ""):
        if "desc" in format_spec or "d" in format_spec:
            return f"{self.name}:\r\n\r\n{self.bio}"
        return str(self)
