from managers.StoneManager import StoneManager
from models.MethStone import MethStone
from models.PreciousStone import PreciousStone
from models.ExplodingStone import ExplodingStone
from models.ArtificialPreciousStone import ArtificialPreciousStone

"""
main method for demonstration of work of all classes
"""
if __name__ == "__main__":
    stone_manager = StoneManager()
    stone_manager.add_stone(MethStone("meth", 100, "blue", 90, 100))
    stone_manager.add_stone(PreciousStone("ruby", 1000, "red", 100, 10))
    stone_manager.add_stone(ExplodingStone("glycerine", 50, "gray", 1000))
    stone_manager.add_stone(ArtificialPreciousStone("plastic stone", 10, "white", 10))
    stone_manager.add_stone(PreciousStone("emerald", 1000, "green", 100, 100))
    for item in stone_manager.find_all_lower(10000):
        print(str(item))
    print("#" * 100)
    for item in stone_manager.find_all_legal():
        print(str(item))
