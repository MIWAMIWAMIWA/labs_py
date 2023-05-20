from models.PreciousStone import PreciousStone
from models.ArtificialPreciousStone import ArtificialPreciousStone


class StoneManager:
    """
    class manager for child classes of stone
    """

    def __init__(self):
        self.stones = []

    """
    adds stone object to list
    """

    def add_stone(self, stone):
        self.stones.append(stone)

    """
    returns a list of objects of PreciousStone class or ArtificialPreciousStone class
    """

    def find_all_legal(self):
        legal = list(filter(lambda stone: (stone.__class__
                                           == PreciousStone or stone.__class__
                                           == ArtificialPreciousStone), self.stones))
        return legal

    """
    returns a list of objects which have get_total_price() less than given price
    """

    def find_all_lower(self, price):
        affordable = list(filter(lambda stone: (stone.get_total_price() <= price), self.stones))
        return affordable
