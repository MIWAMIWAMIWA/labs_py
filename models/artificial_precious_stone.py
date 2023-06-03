"""
importing parent class
"""
from models.stone import Stone


class ArtificialPreciousStone(Stone):
    """
    child class of parent abstract class Stone
    """

    # pylint: disable = too-many-arguments
    def __init__(self, name, gram, color, price_per_gram,note1,note2):
        """
        using parent constructor
        :String name:
        :int gram:
        :String color:
        :int price_per_gram:
        """
        super().__init__(name, color, note1, note2)
        self.gram = gram
        self.price_per_gram = price_per_gram

    def get_total_price(self):
        """
        override function of parent method that returns full price of this Stone
        """
        return self.gram * self.price_per_gram / 2

    def __str__(self):
        """
        string representation of object
        """
        return self.__class__.__name__ + " : " + self.name + " " \
            + str(self.gram) + " " + self.color + " " \
            + " " + str(self.price_per_gram)+" " + str(self.notes)
