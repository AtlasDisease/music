# Created By: Brendan (@AtlasDisease)
# Copyright: 2023
# Description: Song

# --- Imports --- #

from typing import Self
from dataclasses import dataclass, field, KW_ONLY

try:
    from .genres import Genre
except:
    from genres import Genre

try:
    from .artists import Artist
except:
    from artists import Artist

__all__ = ("Song",)


# --- Song Class --- #

@dataclass(frozen = True)
class Song:
    name: str
    artist: Artist
    genre: Genre = field(default = Genre.OTHER)
    _: KW_ONLY
    contributors: list[Artist] | None = field(default = None)

    def __str__(self):
        return self.name

    def __format__(self, format_spec = ""):
        if "desc" in format_spec or "d" in format_spec:
            return f"{self.name} - {self.artist}"
        return str(self)
