from abc import ABC, abstractmethod


class Stone(ABC):
    """
    abstract class for stone classes
    """
    """
    parent constructor for children classes
    """

    def __init__(self, name, color):
        self.name = name
        self.color = color

    """
    abstract method for getting full price for children classes
    """

    @abstractmethod
    def get_total_price(self):
        pass
