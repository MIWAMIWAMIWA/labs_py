from models.Stone import Stone


class PreciousStone(Stone):
    """
    child class of parent abstract class Stone
    """
    """
    static variable for instance of singleton object
    """
    __default_precious_stone = None
    """
    constructor with usage of parent constructor 
    """

    def __init__(self, name, carat, color, clarity, price_per_carat):
        self.carat = carat
        self.clarity = clarity
        self.price_per_carat = price_per_carat
        Stone.__init__(self, name, color)

    """
    override function of parent method that returns full price of this stone
    """

    def get_total_price(self):
        return self.carat * self.price_per_carat

    """
    function increases clarity by 1 for object
    """

    def increase_clarity(self):
        self.clarity += 1

    """
    function increases price_per_carat by amount% for object
    """

    def increase_price(self, amount):
        self.price_per_carat = self.price_per_carat * (1 + amount)

    """
    returns an instance of singleton object for this class
    """

    @classmethod
    def get_instance(cls):
        if cls.__default_precious_stone is None:
            cls.__default_precious_stone = PreciousStone(None, 0, None, 0, 0)
        return cls.__default_precious_stone

    """
    returns string representation of this object
    """

    def __str__(self):
        return self.name + " " + str(self.carat) + " " + self.color + " " \
            + str(self.clarity) + " " + str(
                self.price_per_carat)
