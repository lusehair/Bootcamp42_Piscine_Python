class Vector:
    _m = 0
    _n = 0 
    _data = {} 
    
    def __init__(self, _raw_data) : 
    
        # case if input is n el like Vector(3) 
        if type(_raw_data) == int :
            self._n = int(_raw_data)
            self._m = 1
            for x in range(self._n) :
                self._data[x] = float(x)


        # case if input is like Vector(10,16)
        elif type(_raw_data) == tuple :
            for x in range(_raw_data[1] - _raw_data[0]) :
                self._data = float(_raw_data[0] + x)

        else:
        # Case if input is like Vector([[0.0, 1.0, 2.0, 3.0]])
        # or like Vector([[0.0], [1.0], [2.0], [3.0]])
            self._m = len(_raw_data)
            # Case if m == 1, need to split the str into a list and remove dirty character 
            if self._m  == 1: 
                self._n = str(_raw_data).count('.')
                _raw_data = str(_raw_data) 
                _raw_data = _raw_data.split(',')
                _raw_data[0] = _raw_data[0].replace('[', "")
                _raw_data[self._n - 1] = _raw_data[self._n - 1].replace(']', "")
            # convert str el into float in the _data list         
            for x in range(self._n) :
                self._data[x] = float(_raw_data) 
        

    def values(self) :

       # return(self._data)
       print(self._data)
    

    




