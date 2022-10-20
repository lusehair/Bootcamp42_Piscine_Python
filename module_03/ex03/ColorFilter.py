import numpy as np
from ImageProcessor import ImageProcessor
class ColorFilter :

## Iter in each el of 2d array 
# https://www.w3schools.com/python/numpy/numpy_array_iterating.asp

## Invert 
# https://medium.com/analytics-vidhya/inverting-an-image-using-numpys-broadcasting-method-1f5beb7f9fa5

    
## to_[RGB]
# https://stackoverflow.com/questions/29718877/how-to-extract-green-channel-from-rgb-image-in-python-using-scikit-image-library 


## Celluloid 
# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html 


## GreyScale 
# https://www.adamsmith.haus/python/answers/how-to-convert-an-image-from-rgb-to-grayscale-in-python 
# https://muthu.co/converting-color-images-to-grayscale-using-numpy-and-some-mathematics/


    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.nd\python\answers\how-to-convert-an-image-from-rgb-to-grayscale-in-pythonarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        ret = array[:,:,:3]

        return 1 - ret



    
    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        ret = array.copy()
        ret[:,:,0] = 0
        ret[:,:,1] = 0
        return ret

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """

        ret = array.copy()
        ret[:,:,0] = 0
        ret[:,:,2] = 0
        return ret

        
    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        ret = array.copy()
        ret[:,:,1] = 0
        ret[:,:,2] = 0
        return ret

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        ret = array.copy() 
        for el in np.linspace(0.0, 1.0, num= 50) :
            pix = array <= el
            ret[pix] = el
        return ret



    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """  
        weight = kwargs.get('weights')
        if filter == 'weight' or filter == 'w' :
            return np.dot(array[..., :3], weight)
        elif filter == 'mean' or filter == 'm' :
            mean = np.sum(array, axis=-1) / 3 
            return np.broadcast_to(mean[..., None], array.shape) 
        else : return None 

    

if __name__ == "__main__":

    imp = ImageProcessor()
    arr = imp.load("elon_canaGAN.png")


    imp.display(arr)
    cf = ColorFilter()
    imp.display(cf.invert(arr))
    imp.display(cf.to_green(arr))
    imp.display(cf.to_red(arr))
    imp.display(cf.to_blue(arr))

    imp.display(cf.to_grayscale(arr, 'm'))
    imp.display(cf.to_grayscale(arr, 'weight', weights = [0.2, 0.3, 0.5]))