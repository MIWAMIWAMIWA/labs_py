"""
importing all classes
"""

from managers.stone_manager import StoneManager
from managers.set_manager import SetManager
from models.meth_stone import MethStone
from models.precious_stone import PreciousStone
from models.exploding_stone import ExplodingStone
from models.artificial_precious_stone import ArtificialPreciousStone

if __name__ == "__main__":
    stone_manager = StoneManager()
    stone_manager.add_stone(MethStone("meth", 100, "blue", 90, 100, 1, 1))
    stone_manager.add_stone(PreciousStone("ruby", 1000, "red", 100, 10, 2, 2))
    stone_manager.add_stone(ExplodingStone("glycerine", 50, "gray", 1000, 3, 3))
    stone_manager.add_stone(ArtificialPreciousStone("plastic Stone", 10, "white", 15, 4, 4))
    stone_manager.add_stone(PreciousStone("emerald", 1000, "green", 100, 100, 5, 5))

    miwa = SetManager(stone_manager)
    print(miwa.values)
    for item in miwa:
        print(item)
    print(len(miwa))
