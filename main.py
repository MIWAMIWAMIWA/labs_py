class PreciousStone:
    __default_precious_stone = None

    def __init__(self, name, carat, color, clarity, price_per_carat):
        self.__name = name
        self.__carat = carat
        self.__color = color
        self.__clarity = clarity
        self.__price_per_carat = price_per_carat

    def get_total_price(self):
        return self.__carat * self.__price_per_carat

    def increase_clarity(self):
        self.__clarity += 1

    def increase_price(self, amount):
        self.__price_per_carat = self.__price_per_carat * (1 + amount)

    @staticmethod
    def get_instance(self):
        if self.__default_precious_stone is None:
            self.__default_precious_stone = PreciousStone(None, 0, None, 0, 0)
        return self.__default_precious_stone

    def set_name(self, name):
        self.__name = name

    def set_carat(self, carat):
        self.__carat = carat

    def set_color(self, color):
        self.__color = color

    def set_clarity(self, clarity):
        self.__clarity = clarity

    def set_price_per_carat(self, price_per_carat):
        self.__price_per_carat = price_per_carat

    def to_string(self):
        return self.__name + " " + str(self.__carat) + " " + self.__color + " " \
            + str(self.__clarity) + " " + str(
                self.__price_per_carat)


if __name__ == "__main__":
    stone1 = PreciousStone.get_instance(PreciousStone)
    stone1.set_name("singleton")
    stone1.set_clarity(100)
    stone1.set_color("None")
    stone1.set_carat(100)
    stone1.set_price_per_carat(100)
    stone2 = PreciousStone.get_instance(PreciousStone)
    stone3 = PreciousStone("ruby", 3, "red", 3, 3)
    stone4 = PreciousStone("lapis", 4, "blue", 4, 4)
    stone5 = PreciousStone("ruby", 5, "red", 5, 5)
    arr = stone1, stone2, stone3, stone4, stone5
    for item in arr:
        print(item.to_string())
