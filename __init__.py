from __future__ import annotations
from abc import ABC, abstractmethod
from enum import IntEnum
from PIL.Image import Image


class Buttons(IntEnum):
    A = 5
    B = 6
    C = 16
    D = 24

class ButtonPressed:
    button: Buttons

class ButtonListener(ABC):
    @abstractmethod
    def listen(self) -> None:
        ...

class Display(ABC):
    @abstractmethod
    def show(self, image: Image) -> None:
        ...

