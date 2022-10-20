import pandas as pd 
from FileLoader import FileLoader 


def proportion_by_sport(df, year, sport, sex) :
        if not isinstance(df, pd.DataFrame) or not isinstance(year, int) :
            return None 
        good_year = df[df['Year'] == year] 
        denominator = good_year[good_year['Sex'] == sex]
        numerator = denominator[denominator['Sport'] == sport]
        return (numerator.shape[0] / denominator.shape[0]) 



if __name__ == "__main__" :

    f = FileLoader()
    data = f.load('../athlete_events.csv')

print("")


print(proportion_by_sport(data, 2004, 'Tennis', 'F'))
# output is "0.02307"

print(proportion_by_sport(data, 2008, 'Hockey', 'F'), end = "\n\n")
# output is  "0.03284"

print(proportion_by_sport(data, 1964, 'Biathlon', 'M'), end = "\n\n")
# output is "0.00659"

        
