# https://www.geeksforgeeks.org/select-row-with-maximum-and-minimum-value-in-pandas-dataframe/

import pandas as pd 
from FileLoader import FileLoader

def youngest_fellah(df, year) :
    if not isinstance(df, pd.DataFrame) or not isinstance(year, int) :
        return None 
    good_year = df[df['Year'] == year] 
    male = good_year[good_year['Sex'] == 'M']
    female = good_year[good_year['Sex'] == 'F']

    ret = dict() 
    ret['f'] = female.Age.min()
    ret['m'] = male.Age.min()
    return ret 


if __name__ == "__main__":

    f = FileLoader()
    data = f.load('../athlete_events.csv')
    # youngest_fellah(data,2002)
    print(youngest_fellah(data, 1992))
    # output is: "{'f': 12.0, 'm': 11.0}"

    print(youngest_fellah(data, 2004))
    # output is: "{'f': 13.0, 'm': 14.0}"

    print(youngest_fellah(data, 2010))
    # output is: "{'f': 15.0, 'm': 15.0}"

    print(youngest_fellah(data, 2003))
    # output is: "{'f': nan, 'm': nan}"