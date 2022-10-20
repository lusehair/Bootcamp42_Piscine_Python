from logging import exception
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# https://www.geeksforgeeks.org/how-to-convert-images-to-numpy-array/
# https://pillow.readthedocs.io/en/stable/reference/ImageTk.html#module-PIL.ImageTk
# https://ensip.gitlab.io/pages-info/ressources/transverse/tuto_images.html

class ImageProcessor() :

    imgObj = ""

    def __init__(self) :
        self.imgObj = None

    def load(self,path) :
        try :
            self.imgObj = Image.open(path) 
        
        except Exception as e: 
            print(e)
            return None 
        print("Loading image of dimensions " + str(self.imgObj.height) + ' x ' + str(self.imgObj.width))
        return np.array(self.imgObj)
         
    def display(self, array) :
        try :
            plt.imshow(array)    
            plt.show()
        except Exception as e: 
            print(e)
            return None 



if __name__ == "__main__":

    imp = ImageProcessor()
    # Error Management 
    arr = imp.load("non_existing_file.png")
    print(arr)
    arr = imp.load("empty_file.png")
    print(arr)

    # From IMG 
    arr = imp.load("42AI.png")
    print(arr)

    # From Array 
    imp.display(arr)






