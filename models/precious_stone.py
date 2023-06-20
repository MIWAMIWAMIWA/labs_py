"""
importing parent class
"""
from models.stone import Stone


class NegativeCarat(Exception):
    """
    this exception should be raised only when object
    of class PreciousStone have negative carat
    """


class PreciousStone(Stone):
    """
    child class of parent abstract class Stone
    """

    # pylint: disable = too-many-arguments
    def __init__(self, name, carat, color, clarity, price_per_carat, note1, note2):
        """
        using parent constructor
        :String name:
        :int carat:
        :String color:
        :int clarity:
        :int price_per_carat:
        """
        super().__init__(name, color, note1, note2)
        self.carat = carat
        self.clarity = clarity
        self.price_per_carat = price_per_carat

    def get_total_price(self):
        """
        override function of parent method that returns full price of this Stone
        """
        if self.carat < 0:
            raise NegativeCarat("IT CAN`T BE NEGATIVE - IS IT NOT OBVIOUS FOR YOU")
        return self.carat * self.price_per_carat

    def increase_clarity(self):
        """
        function increases clarity by 1 for object
        """
        self.clarity += 1

    def increase_price(self, amount):
        """
        function increases price_per_carat by amount% for object
        """
        self.price_per_carat = self.price_per_carat * (1 + amount)

    def __str__(self):
        """
        string representation of object
        :return:
        """
        return self.__class__.__name__ + " : " + self.name + " " \
            + str(self.carat) + " " + self.color + " " \
            + str(self.clarity) + " " + str(
                self.price_per_carat) + " " + str(self.notes)
