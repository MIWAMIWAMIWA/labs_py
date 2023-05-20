from models.Stone import Stone


class ArtificialPreciousStone(Stone):
    """
    child class of parent abstract class Stone
    """
    """
    constructor with usage of parent constructor 
    """

    def __init__(self, name, gram, color, price_per_gram):
        self.gram = gram
        self.price_per_gram = price_per_gram
        Stone.__init__(self, name, color)

    """
    override function of parent method that returns full price of this stone
    """

    def get_total_price(self):
        return self.gram * self.price_per_gram / 2

    """
    returns string representation of this object
    """

    def __str__(self):
        return self.name + " " + str(self.gram) + " " + self.color + " " \
            + " " + str(self.price_per_gram)
