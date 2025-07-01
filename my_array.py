#In the name of ALLAH!
#Mahdi Salehi

class Array:
    def __init__(self, size : int) -> None:
        self.elements = [i for i in range(size)]
    
    def __getitem__(self, index):
        if isinstance(index,int):
            return self.elements[index]
        elif isinstance(index,slice):
            start, stop, step = index.indices(len(self))
            items = Array(int((stop - start)/step) + 1)
            for i in range(start, stop):
                items[i - start] = self.elements[i]
            return items
        else:
            raise TypeError
    
    def __setitem__(self, index, val):
        self.elements[index] = val

    def __contains__(self, val):
        for i in range(len(self.elements)):
            if self.elements[i] == val:
                return True
        return False
    
    def __iter__(self):
        return AIterator(self)
    
    def __len__(self):
        return len(self.elements)
    

class AIterator:
    """Iterator for Array."""
    def __init__(self, array) -> None:
        self.array = array
        self.len = len(array)
        self.index = 0
    
    def __next__(self):
        if self.len:
            val = self.array[self.index]
            self.len -= 1
            self.index += 1
            return val
        else:
            raise StopIteration
            