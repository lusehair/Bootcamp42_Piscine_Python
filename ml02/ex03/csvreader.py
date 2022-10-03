import sys 
import csv 

# https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/3-further/2-context-managers/ 
# https://www.programiz.com/python-programming/csv

class CsvReader():
    
    filename = ""
    values = [] 
    f = ""
    header = False
    _skip_top = 0
    _skip_bottom = 0
    _sep = ','
    _error = None 
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
    
        if skip_bottom < 0 or skip_top < 0 :
            self._error = "Skiper cannot be a negative number" 
            return    
        if filename is None :
            self._error = "the filename is not specified"
            return 
        self.filename = filename
        self.header = header
        self._skip_bottom = skip_bottom 
        self._skip_top = skip_top 
        self._sep = sep 
    
    def __enter__(self):
        try:
            with open(self.filename, 'r') as file: 
                reader = csv.reader(file, delimiter = self._sep) 
                self.values = list(reader) 
                for row in self.values : 
                    for value in row :
                        if value == "" :
                            raise Exception("Error Data corrupted")
        except: 
            return None
        return self
        
    def __exit__(self, type, value, traceback): 
        if type is not None :
            print("here")
            return None 
        if self._error is not None :
            return self._error 
    
    def getdata(self):

        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        ret = [] 
        self._skip_bottom = len(self.values)  - (self._skip_bottom)
        for i, value in enumerate(self.values) : 
            if i > self._skip_top and i != self._skip_bottom and i != 0 :
                ret.append(value)
        return ret

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """    
        ret = None 
        if self.header is True :
            ret =  self.values[0]      
        return ret 

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