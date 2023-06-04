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
    stone_manager.add_stone(MethStone("start", 100, "blue", 90, 100, 11, 12))
    stone_manager.add_stone(PreciousStone("ruby", 1000, "red", 100, 10, 21, 22))
    stone_manager.add_stone(ExplodingStone("glycerine", 50, "gray", 1000, 31, 32))
    stone_manager.add_stone(ArtificialPreciousStone("plastic Stone", 10, "white", 15, 41, 42))
    stone_manager.add_stone(PreciousStone("emerald", 1000, "green", 100, 100, 51, "end"))
    print(stone_manager[1])
    print(stone_manager.get_lower_any_all(100))
    print(list(stone_manager.enumerating()))
    print(list(stone_manager.zipping()))
    print(list(stone_manager.find_all_lower(1000)))
    iter1 = SetManager(stone_manager)
    for i in range(33):
        print(iter1[i])
    iter1 = SetManager(stone_manager)
    for item in iter1:
        print(item)
    iter1 = SetManager(stone_manager)
    print(len(iter1))
    print(next(iter1))
