import numpy as np 
from collections.abc import Iterable

# https://numpy.org/doc/stable/reference/generated/numpy.full.html

class NumPyCreator :
    
    def from_list(self, lst) :
        if type(lst) is not list :
            return None 
        return np.array(lst) 
    def from_tuple(self, tpl) :
        if type(tpl) is not tuple:
            return None
        return np.array(tpl)
    def from_iterable(self, itr) :
        if itr <= 1 :
            return None
        return np.arange(itr) 
    def from_shape(self, shape, value = 0): 
        if shape <=1 and value <= 1 : 
            return None 
        return(np.full((shape),value))
    def from_random(self, shape) :
        if shape < 0: 
            return None 
        return np.random.rand(shape)
    def identity(self, n) :
        
    
        
    
        
    

        







if __name__ == "__main__":

    npc = NumPyCreator()
    print(npc.from_list([[],[]]))