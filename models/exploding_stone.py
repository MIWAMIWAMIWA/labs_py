"""
importing parent class
"""
from models.stone import Stone


class ExplodingStone(Stone):
    """
    for security purposes this class will be undocumented
    """

    def __init__(self, name, amount, color, price_per_amount):
        self.amount = amount
        self.price_per_amount = price_per_amount
        Stone.__init__(self, name, color)

    def get_total_price(self):
        """
        get full price of stone
        """
        return self.amount * self.price_per_amount

    def __str__(self):
        return self.name + " " + str(self.amount) + " " + self.color + " " \
            + " " + str(self.price_per_amount)
