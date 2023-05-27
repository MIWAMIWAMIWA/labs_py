"""
importing child classes of stone to compare with
"""
from managers.decorators import logging_exception
from managers.decorators import logging_arguments
from models.precious_stone import PreciousStone
from models.artificial_precious_stone import ArtificialPreciousStone


class StoneManager:
    """
    class manager for child classes of Stone
    """

    # зробити декоратори вар 7 і 8
    def __init__(self):
        """
        initialization of list to save stone objects
        """
        self.stones = []
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = self.stones[self.current]
        self.current += 1
        return res

    def __len__(self):
        return len(self.stones)

    @logging_arguments
    @logging_exception
    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError
        if item < 0 or item >= len(self.stones):
            raise IndexError
        return self.stones[item]

    @logging_arguments
    @logging_exception
    def add_stone(self, stone):
        """
        adds Stone object to list
        """
        if stone is None:
            raise TypeError
        self.stones.append(stone)

    def find_all_legal(self):
        """
        returns a list of objects of PreciousStone class or ArtificialPreciousStone class
        """
        return filter(lambda stone: (stone.__class__ in (ArtificialPreciousStone,
                                                         PreciousStone)), self.stones)

    @logging_arguments
    @logging_exception
    def find_all_lower(self, price):
        """
        returns a list of objects which have get_total_price() less than given price
        """
        if price <= 0:
            raise ValueError
        return filter(lambda stone: (stone.get_total_price() <= price), self.stones)

    def get_all_prices(self):
        """
        returns all prices of stones in manager
        """
        return [item.get_total_price() for item in self.stones]

    def enumerating(self):
        """
        returns tuples of index of object in manager and string representation of this object
        """
        return enumerate([str(item) for item in self.stones])

    def zipping(self):
        """
        returns tuples of string representation of object and value of get_total_price() from
        this object
        """
        return zip([str(item) for item in self.stones], self.get_all_prices())

    def get_lower_any_all(self, asked_price):
        """
        returns dictionary which tells is all or any stone could be bought
        for asked price
        """
        if not isinstance(asked_price, int):
            raise TypeError
        if asked_price <= 0:
            raise ValueError
        affordable = [asked_price >= current for current in self.get_all_prices()]
        return {"all": all(affordable), "any": any(affordable)}
