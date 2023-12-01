from dataclasses import dataclass
from typing import Any


@dataclass
class ConstantInformation:
    name: str
    description: str
    value: Any


class Constants:
    board_area = ConstantInformation(
        name="board_area",
        description="This is the area of the board",
        value=64
    )

    number_of_files = ConstantInformation(
        name="number_of_files",
        description="This is the number of files (x-axis) on the board",
        value=8
    )

    number_of_ranks = ConstantInformation(
        name="number_of_ranks",
        description="This is the number of ranks (y-axis) on the board",
        value=8
    )
