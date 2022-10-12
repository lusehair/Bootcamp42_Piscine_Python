import numpy as np 
from collections.abc import Iterable

# https://numpy.org/doc/stable/reference/generated/numpy.full.html

class NumPyCreator :
    
    def from_list(self, lst) :
        if not isinstance(lst, list) :
            return None 
        return np.asarray(lst) 
    def from_tuple(self, tpl) :
        if type(tpl) is not tuple:
            return None
        return np.array(tpl)
    def from_iterable(self, itr) :
        if isinstance(itr, Iterable):
            return np.array(itr) 
        return None
    def from_shape(self, shape, value = 0): 
        if not isinstance(shape, tuple) :
            return None 
        if shape[0] <= 0 or shape[1] <= 0 :
            return None
        return(np.full((shape),value))
    def random(self, shape) :
        if not isinstance(shape, tuple): 
            return None 
        return np.random.random(shape)
    def identity(self, n) : 
        if n <= 1 :
            return None
        return np.identity(n) 
    

if __name__ == "__main__":

    npc = NumPyCreator()
    print(npc.from_list([[],[]])) 
    print(npc.from_list([[1,2,3],[6,3,4],[8,5,6]]))
    print(npc.from_tuple(("a","b","c")))
    print(npc.from_iterable(range(5)))
    print(npc.from_shape((0, 0)))
    print(npc.from_shape((3, 5)))
    print(npc.random((3, 5)))
    print(npc.identity(4))
    print("ERROR MANAGEMENT")
    
    print(npc.from_list("toto"))
    print(npc.from_tuple(3.2))
    print(npc.from_shape((-1, -1)))
    print(npc.identity(-1))