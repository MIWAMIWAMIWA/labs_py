"""
importing packages for abstract class
"""

from abc import ABC, abstractmethod


class Stone(ABC):
    """
    abstract parent  class for Stone classes
    """

    # pylint: disable=too-few-public-methods
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def get_total_price(self):
        """
        abstract method for child classes
        """
