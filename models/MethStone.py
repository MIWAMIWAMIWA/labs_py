from models.Stone import Stone


class MethStone(Stone):
    """
    child class of parent abstract class Stone
    """
    """
    constructor with usage of parent constructor 
    """

    def __init__(self, name, pound, color, clarity, price_per_pound):
        Stone.__init__(self, name, color)
        self.pound = pound
        self.clarity = clarity
        self.price_per_pound = price_per_pound

    """
    override function of parent method that returns full price of this stone
    """

    def get_total_price(self):
        return self.pound * self.price_per_pound * self.clarity / 100

    """
    returns string representation of this object
    """

    def __str__(self):
        return self.name + " " + str(self.pound) + " " + self.color + " " \
            + str(self.clarity) + " " + str(
                self.price_per_pound)
