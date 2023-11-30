from dataclasses import dataclass
from enum import Enum


@dataclass
class ColorInformation:
    name: str
    mask: int


class Color(Enum):
    WHITE = ColorInformation(name="white", mask=1)
    BLACK = ColorInformation(name="black", mask=-1)
