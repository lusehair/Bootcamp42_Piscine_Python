import sys 
import csv 

# https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/3-further/2-context-managers/ 


class CsvReader():
    
    filename = ""
    values = [] 
    f = ""
    header = False
    _skip_top = 0
    _skip_bottom = 0
    _sep = ','
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.header = header
        self._skip_bottom = skip_bottom 
        self._skip_top = skip_top 
        self._sep = sep 
        pass
        # ... Your code here ...
    
    def __enter__(self):
        with open(self.filename, 'r') as file: 
            values = csv.reader(file) 

        # ... Your code here ...
        pass 
    
        #f.close()
    
    
    def __exit__(self, type, value, traceback): 
        pass 
    # ... Your code here ...
    def getdata(self):

        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """

    # ... Your code here ...

    
    
    def getheader(self):
        if self.header is True :
            return self.values[0] 
        else : 
            return None 
        

        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """


# ... Your code here ...



if __name__ == "__main__":
    filename = sys.argv[1]
    with CsvReader(filename, skip_top=18, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end = "\n")
            print(reader.getdata(), end = "\n\n")

    with CsvReader(filename, header = True, skip_top=17, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end = "\n")
            print(reader.getdata(), end = "\n\n")