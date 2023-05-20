from models.Stone import Stone


class ExplodingStone(Stone):
    """
    for security purposes this class will be undocumented
    """
    """
    constructor with usage of parent constructor 
    """

    def __init__(self, name, amount, color, price_per_amount):
        self.amount = amount
        self.price_per_amount = price_per_amount
        Stone.__init__(self, name, color)

    """
    override function of parent method that returns full price of this stone
    """

    def get_total_price(self):
        return self.amount * self.price_per_amount

    """
    returns string representation of this object
    """

    def __str__(self):
        return self.name + " " + str(self.amount) + " " + self.color + " " \
            + " " + str(self.price_per_amount)
