# Created By: Brendan (@AtlasDisease)
# Copyright: 2023
# Description: Albums, Record, Playlists, etc

# --- Imports --- #

from typing import Self
from dataclasses import dataclass, field

try:
    from .genres import Genre
except:
    from genres import Genre

try:
    from .artists import Artist
except:
    from artists import Artist

try:
    from .songs import Song
except:
    from songs import Song

__all__ = ("Album", "Playlist", "Record",)


# --- Album Class --- #

@dataclass(slots = True)
class Album:
    name: str
    artist: Artist
    genre: Genre = field(default = Genre.OTHER)
    songs: list[Song] = field(default_factory = list)

    def __str__(self):
        return self.name

    def __format__(self, format_spec = ""):
        if "desc" in format_spec or "d" in format_spec:
            return f"{self.name} - {self.artist}"
        return str(self)

    def __iter__(self):
        return iter(self.songs)


# --- Record Class --- #

@dataclass(slots = True)
class Record(Album):
    pass


# --- Playlist Class --- #

@dataclass(slots = True)
class Playlist(Album):
    desc: str = ""

    def __format__(self, format_spec = ""):
        if "desc" in format_spec or "d" in format_spec:
            return f"{self.name} - {self.artist}:\r\n\r\n{self.desc}"
        return str(self)
