import numpy as np

class ScrapBooker() :

    ## CROP 
    # https://www.geeksforgeeks.org/how-to-crop-an-image-using-the-numpy-module/ 
    # https://stackoverflow.com/questions/39424052/how-to-set-coordinates-when-cropping-an-image-with-pil

    ## THIN 
        # https://numpy.org/doc/stable/reference/generated/numpy.delete.html 
        # https://note.nkmk.me/en/python-numpy-delete/ 

    ## JUXTAPOSITION 
        # https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html

    ## Mosaic 
        # https://numpy.org/doc/stable/reference/generated/numpy.tile.html
        # 

    ## Error Management 
     # https://stackoverflow.com/questions/12569452/how-to-identify-numpy-types-in-python

    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        """ 
        if (type(array).__module__ == np.__name__) is False :
            return None

        if dim[0] > array.shape[0] or dim[1] > array.shape[1] :
            return None 
        if dim[0] < 0 or dim[1] < 0 or position[0] < 0 or position[1] < 0 : 
            return None 
        if position[0] > array.shape[0] or position[1] > array.shape[1] : 
            return None 
        return array[position[0]:dim[0] + position[0] , position[1]:dim[1] + position[1]]

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """   
        if  (type(array).__module__ == np.__name__) is False:
            return None
        if n <= 0 or axis == 1 and n > array.shape[1] or axis == 0 and n > array.shape[0] :
            return None 
        for i in range(array.shape[axis]) :
            if i % n == 0 :
               np.delete(array, i, axis)
        return array 
            
    
    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        ret = None
        if  (type(array).__module__ == np.__name__) is False:
            return ret
        elif n > 0 and (axis == 0 or axis == 1) :
            ret = array
            i = 1
            while i < n :
                ret = np.concatenate((ret, array), axis = axis)
                i += 1
        return ret 
        
        
        pass
    def mosaic(self, array, dim):
        
        if  (type(array).__module__ == np.__name__)  is False:
            return None
       
        if dim[0] < array.shape[0] or dim[1] < array.shape[1] :
                return None
        else :
            return np.tile(array,dim) 

        
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This  function should not raise any Exception.
        """
        
        
        pass 


if __name__ == "__main__":

    spb = ScrapBooker()
    arr1 = np.arange(0,25).reshape(5,5)
    print(spb.crop(arr1, (3,1),(1,0)))

    #Output :
    # array([[ 5],
    # [10],
    # [15]])


    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
    print(spb.thin(arr2,3,0))

    #Output :
    # array([[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
    # [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
    # [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
    # [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
    # [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
    # [’A’, ’B’, ’D’, ’E’, ’G’, ’H’]], dtype=’<U1’)

    arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    print(spb.juxtapose(arr3, 3, 1))

    #     #Output :
    # array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
    # [1, 2, 3, 1, 2, 3, 1, 2, 3],
    # [1, 2, 3, 1, 2, 3, 1, 2, 3]])

    arr4 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    print(spb.juxtapose(arr4, 2, 0)) 

    # Output 

    # array([[1, 2, 3],
    #   [4, 5, 6],
    #   [7, 8, 9],
    #   [1, 2, 3],
    #   [4, 5, 6],
    #   [7, 8, 9]])

    # Error Management 

    not_numpy_arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print(spb.crop(not_numpy_arr, (1,2)))
    print(spb.juxtapose(arr4, -2, 0))
    print(spb.mosaic(arr4, (1, 2, 3))) 

    # Should all return None (no error exception)







                    
