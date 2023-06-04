"""
importing parent class
"""
from models.stone import Stone
from managers.decorators import logged


class NegativeAmount(Exception):
    """
    this exception should be raised only when object
    of class ExplodingStone have negative amount
    """



class ExplodingStone(Stone):
    """
    for security purposes this class will be undocumented
    """

    # pylint: disable = too-many-arguments
    def __init__(self, name, amount, color, price_per_amount, note1, note2):
        """
        using parent constructor
        :String name:
        :int amount:
        :String  color:
        :int price_per_amount:
        """
        super().__init__(name, color, note1, note2)
        self.amount = amount
        self.price_per_amount = price_per_amount

    @logged(Exception, mode="file")
    def get_total_price(self):
        """
        get full price of stone
        """
        if self.amount < 0:
            raise NegativeAmount("IT CAN`T BE NEGATIVE - IS IT NOT OBVIOUS FOR YOU")
        return self.amount * self.price_per_amount

    def __str__(self):
        """
        string representation of object
        """
        return self.__class__.__name__ + " : " + self.name + " " \
            + str(self.amount) + " " + self.color + " " \
            + " " + str(self.price_per_amount) + " " + str(self.notes)
