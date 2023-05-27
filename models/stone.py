"""
importing packages for abstract class
"""

from abc import ABC, abstractmethod


class Stone(ABC):
    """
    abstract parent  class for Stone classes
    """

    # pylint: disable=too-few-public-methods
    def __init__(self, name, color,note1,note2):
        """
        parent constructor of parent class
        :String name:
        :String color:
        :(String note1,String note2):
        """
        self.name = name
        self.color = color
        self.notes= (note1,note2)
    @abstractmethod
    def get_total_price(self):
        """
        abstract method for child classes
        """
