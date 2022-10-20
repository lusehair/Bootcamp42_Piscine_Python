# https://datatofish.com/first-n-rows-pandas-dataframe/ 


import pandas as pd 

class   FileLoader :


    def load(self, path) : 
        try :
            df = pd.read_csv(path)
        except :
            return None 
        print(df.shape)
        return df

    def display(self, df, n) :
        if not isinstance(n, int) or not isinstance(df, pd.DataFrame): 
            return None 
        if n > 0 :
            try :
                return df.head(n) 
            except :
                return None 
        elif n < 0 :
            try :
                return df.tail(abs(n)) 
            except :
                return None 

if __name__ == "__main__":

    f = FileLoader()
    df = f.load('../athlete_events.csv')
    print("# TEST 1")
    print(f.display(df, 3))
    print("# TEST 2")
    print(f.display(df, -3))
    print("# TEST 3")
    print(f.display(df, 0))
    print("# TEST 4")
    print(f.display(df, "lol"))


