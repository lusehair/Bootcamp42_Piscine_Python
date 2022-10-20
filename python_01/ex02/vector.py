import copy 

class Vector:
    shape = ()
    values = []
    
    def __init__(self, _raw_data , _raw_data1 = None) :
    
        # if args :
        #     print("here")
        #     self.values.append([_raw_data])
        #     self.values.append([_raw_data1]) 
        #     for el in args :
        #         self.values.append(float([el])) 
       # print(type(_raw_data))
        print(_raw_data, _raw_data1)

        if type(_raw_data) == list :
            print("here")
            #self.values.append(_raw_data)
            self.values = _raw_data
            column = 0
            for el in _raw_data : 
                column = column + 1
          #  self.shape = column, len(self.values[0]) 
            if column > 1 : 
                self.shape = column, 1 
            else : self.shape = column, len(self.values[0]) 

            # print(column) 
            # print(len(self.values))


            
        elif type(_raw_data) == int and _raw_data < 1 :
            print("inputError: insert a int more than 1")
            exit()                


        elif type(_raw_data) is int and _raw_data > 0  :
            print("here no1")
            for i in range(_raw_data) :
                self.values.append([float(i)])
            self.shape = len(self.values), 1

        # Case Vector(3,6)

        elif type(_raw_data) is tuple :
            print("this case")
            if _raw_data[0] < _raw_data[1]  and (type(_raw_data[0]) is int and type(_raw_data[1]) is int)  :
                for i in range(_raw_data[0], _raw_data[1]) :
                    self.values.append([float(i)])
            else :
                print("inputError: the range is incorrect")
                exit()
            self.shape = len(self.values), 1

        
        # elif _raw_data[1] != None and type(_raw_data[0]) != list: 
        #     _raw_data = list(_raw_data)

        #     print("here no")
        #     if type(_raw_data[0]) == int and type(_raw_data[1]) == int : 
        #         i = 0
        #         if _raw_data[0] < _raw_data[1] :
        #             print("this case")
        #             while _raw_data[0] < _raw_data[1] : 
        #                 self.values.append([_raw_data[0]])
        #                 _raw_data[0] = _raw_data[0] + 1 

        #         elif _raw_data[0] > _raw_data[1] : 
        #             print("this caseTOO")
        #             i = 0
        #             while _raw_data[0] > _raw_data[1] : 
        #                 self.values.append([_raw_data[0]])
        #                 _raw_data[0] = _raw_data[0] - 1 
        else :
            print("Error: In this case you should input only int")
            exit()
        #self.shape = len(self.values),  len(self.values[0]) 
        # print(self.shape[1])    




    def __mul__(self, multi) : 
        if type(multi) == int or type(multi) == float : 
            if len(self.values) > 1 :
                ret = []
                for value in self.values : 
                    for el in value :
                        ret.append([el * multi])
                return Vector(ret)
            else :
                ret = copy.deepcopy(self)
                i = 0 
                print(multi)

                while i < len(self.values[0]) :
                   ret.values[0][i] = ret.values[0][i] * multi 
                   print(ret.values[0][i])
                   i = i + 1
                print(ret.values[0])
                # ret = self.values
                # for value in ret[0] :
                #     #for el in value : 
                #     value = value * multi
                # print(ret)
                        #ret.append([el * multi])  
                return ret
        else : 

            print('error: the multiplicator should be a int or a float')
            exit()
       

            


    def __rmul__(self, multi) :
        return self.__mul__(multi)



    def __add__(self, v2) : 
        ret = []
        
        if type(v2) != Vector :
            print("errorType: An addition between two differents type is impossible")
            exit()
        if self.shape == v2.shape :
            for value, value2 in zip(self.values, v2.values) :
                for el, el2 in zip(value, value2) :
                    ret.append([el + el2]) 
            return Vector(ret) 
            
        else : 
            print('error: vectors don\'t have the same shape')
            exit()
    
    def __radd__(self, v2) :
        return self.__add__(v2)  
    


    def __sub__(self, v2) : 
        ret = []
        
        if type(v2) != Vector :
            print("errorType: An addition between two differents type is impossible")
            exit()
        if self.shape == v2.shape :
            for value, value2 in zip(self.values, v2.values) :
                for el, el2 in zip(value, value2) :
                    ret.append([el - el2]) 
            return Vector(ret) 
            
        else : 
            print('error: vectors don\'t have the same shape')
            exit()
    
    def __rsub__(self, v2) :
        return self.__add__(v2)  
    
                 

    def __truediv__(self, multi) :
        if multi == 0 : 
            print("ZeroDivisionError: division by zero.")
            exit()
        ret = []
        if type(multi) == int or type(multi) == float : 
            for value in self.values : 
                for el in value :
                    ret.append([el / multi])
        else : 
            print('error: the multiplicator should be a int or a float')
            exit()
        return Vector(ret)

    
    def __str__(self) :
        return str(self.values)

            


    def __rtruediv__(self, multi) :
        print('NotImplementedError: Division of a scalar by a Vector is not defined here.')
        exit()
    


    def T(self) :
         
        ret = []
        if self.shape[0] > 1 :
            ret.append([item for sublist in self.values for item in sublist])
        else : 
            print(len(self.values[0]))
            for el in self.values :
                for val in el :
                    ret.append([val])
        return Vector(ret)

    
    def dot(self, v2) :
        ret = 0
        if self.shape == v2.shape : 
            for value, value2 in zip(self.values, v2.values) :
                for el, el2 in zip(value, value2) :
                    ret = ret + (el * el2) 
            return ret
        else : 
            print("The vectors d\'ont have the same shape")
            exit()

    def __repr__(self) :
        return str(self.values)






    

       

    

        
            


                 

