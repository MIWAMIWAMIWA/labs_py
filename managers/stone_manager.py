"""
importing child classes of stone to compare with
"""
from models.precious_stone import PreciousStone
from models.artificial_precious_stone import ArtificialPreciousStone


class StoneManager:
    """
    class manager for child classes of Stone
    """

    def __init__(self):
        self.stones = []

    def add_stone(self, stone):
        """
        adds Stone object to list
        """
        self.stones.append(stone)

    def find_all_legal(self):
        """
        returns a list of objects of PreciousStone class or ArtificialPreciousStone class
        """
        return list(filter(lambda stone: (stone.__class__ in (ArtificialPreciousStone,
                                                              PreciousStone)), self.stones))

    def find_all_lower(self, price):
        """
        returns a list of objects which have get_total_price() less than given price
        """
        return list(filter(lambda stone: (stone.get_total_price() <= price), self.stones))
