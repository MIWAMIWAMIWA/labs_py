"""
importing parent class
"""
from models.stone import Stone


class ArtificialPreciousStone(Stone):
    """
    child class of parent abstract class Stone
    """

    def __init__(self, name, gram, color, price_per_gram):
        self.gram = gram
        self.price_per_gram = price_per_gram
        Stone.__init__(self, name, color)

    def get_total_price(self):
        """
        override function of parent method that returns full price of this Stone
        """
        return self.gram * self.price_per_gram / 2

    def __str__(self):
        return self.name + " " + str(self.gram) + " " + self.color + " " \
            + " " + str(self.price_per_gram)
