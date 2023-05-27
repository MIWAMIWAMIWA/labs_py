"""
importing parent class
"""

from models.stone import Stone


class MethStone(Stone):
    """
    child class of parent abstract class Stone
    """

    # pylint: disable = too-many-arguments
    def __init__(self, name, pound, color, clarity, price_per_pound,note1,note2):
        """
         using parent constructor
        :String  name:
        :int pound:
        :String color:
        :int  clarity:
        :int price_per_pound:
        """
        super().__init__(name, color, note1, note2)
        self.pound = pound
        self.clarity = clarity
        self.price_per_pound = price_per_pound

    def get_total_price(self):
        """
        override function of parent method that returns full price of this Stone
        """
        return self.pound * self.price_per_pound * self.clarity / 100

    def __str__(self):
        """
        string representation of object
        """
        return self.__class__.__name__ + " : " + self.name \
            + " " + str(self.pound) + " " + self.color + " " \
            + str(self.clarity) + " " + str(
                self.price_per_pound)+" " + str(self.notes)
