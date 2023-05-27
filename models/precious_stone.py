"""
importing parent class
"""
from models.stone import Stone


class PreciousStone(Stone):
    """
    child class of parent abstract class Stone
    """
    __default_precious_stone = None

    # pylint: disable = too-many-arguments
    def __init__(self, name, carat, color, clarity, price_per_carat):
        self.carat = carat
        self.clarity = clarity
        self.price_per_carat = price_per_carat
        Stone.__init__(self, name, color)

    def get_total_price(self):
        """
        override function of parent method that returns full price of this Stone
        """
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

    @classmethod
    def get_instance(cls):
        """
        returns an instance of singleton object for this class
        """
        if cls.__default_precious_stone is None:
            cls.__default_precious_stone = PreciousStone(None, 0, None, 0, 0)
        return cls.__default_precious_stone

    def __str__(self):
        return self.name + " " + str(self.carat) + " " + self.color + " " \
            + str(self.clarity) + " " + str(
                self.price_per_carat)
