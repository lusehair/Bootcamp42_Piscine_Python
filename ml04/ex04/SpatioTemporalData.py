##Find unique occurence
# https://stackoverflow.com/questions/68590094/unique-values-in-pandas 
##  Tricky but can be a red flag: COnvert np.array to list 
# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html 
from FileLoader import FileLoader 

class SpatioTemporalData :
    _df = None 

    def __init__(self, df) :
        self._df = df 
    
    def when(self, location) :
        ret = []
        good_year =  self._df[self._df['City'] == location]
        ret = good_year.Year.unique()
        ret = ret.tolist()
        return ret 

         

    def where(self, date) : 
        ret = []
        good_location =  self._df[self._df['Year'] == date]
        ret = good_location.City.unique()
        ret = ret.tolist()
        (ret)
        return ret 
         


if __name__ == "__main__":
    f = FileLoader()
    df = f.load('../athlete_events.csv')
    sp = SpatioTemporalData(df)
    print(sp.where(2000))
    print(sp.where(1980))
    print(sp.when('London'))

