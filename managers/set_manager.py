"""
no modules needed to be imported
"""


class SetManager:
    """
    SetManager in fact is custom iterator to iterate through list of values of objects
    """

    def __init__(self, prev_manager):
        self.values = []
        for item in prev_manager.stones:
            current_values = list(item.__dict__.values())
            self.values += current_values
        self.current = 0
        self.current_if_tuple = 0

    def __iter__(self):
        return self

    def __len__(self):
        length = 0
        for item in self.values:
            if isinstance(item, tuple):
                length += len(item)
            else:
                length += 1
        return length

    def __next__(self):
        if self.current >= len(self.values):
            raise StopIteration
        if isinstance(self.values[self.current], tuple):
            if self.current_if_tuple >= len(self.values[self.current]):
                self.current += 1
                self.current_if_tuple = 0
                return self.__next__()

            result = self.values[self.current][self.current_if_tuple]
            self.current_if_tuple += 1
            return result

        result = self.values[self.current]
        self.current += 1
        return result

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError
        if item < 0 or item >= self.__len__():
            raise IndexError
        current = 0
        actual_position = -1
        while 1:
            if isinstance(self.values[current], tuple):
                if len(self.values[current]) + actual_position >= item:
                    return self.values[current][item - actual_position-1]
                actual_position += len(self.values[current])
                current += 1
            else:
                if item == actual_position + 1:
                    return self.values[current]
                actual_position += 1
                current += 1
