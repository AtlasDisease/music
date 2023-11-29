# Created By: Brendan (@AtlasDisease)
# Copyright: 2023
# Description: Genre

# --- Imports --- #

from enum import StrEnum, auto

_all__ = ("Genre",)


# --- Genre Enum --- #

class Genre(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
    
    OTHER = auto() #General use
    ROCK = auto()
    POP = auto()
    COUNTRY = auto()
    JAZZ = auto()
    HIP_HOP = auto()
    RAP = auto()
    R_AND_B = auto()
    ELECTRONIC = auto()
    PUNK = auto()
    RAGTIME = auto()
