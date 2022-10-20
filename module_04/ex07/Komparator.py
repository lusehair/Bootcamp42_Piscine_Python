import matplotlib.pyplot as plt  
from FileLoader import FileLoader
import seaborn as sns
import warnings


class Komparator: 
    _df = None 

    def __init__(self, df): 
        self._df = df.dropna() 

    def compare_box(self, categorical_var, numerical_var) :
        self._df.boxplot(column=[numerical_var], by=categorical_var)
        plt.show()

    def density(self, categorical_var, numerical_var): 

        df = self._df.pivot(columns=categorical_var, values=numerical_var)
        sns.displot(df, kind="kde")
        plt.title(numerical_var+" per "+categorical_var)
        plt.show()
        


    def compare_histograms(self, categorical_var, numerical_var): 
        _cat = list(self._df[categorical_var].unique())
        fig, ax = plt.subplots(ncols=len(_cat))

        for i, item in enumerate(_cat):
            plot = self._df[categorical_var] == item 
            ax[i].set_title(item)
            ax[i].hist(self._df[plot][numerical_var].dropna())
            ax[i].grid()
        plt.show()




if __name__ == "__main__": 

    df = FileLoader()
    df = df.load("../athlete_events.csv")

    komp = Komparator(df)
    category = 'Medal'
    category1 = 'Sex'
    numerical = 'Age'
    numerical1 = 'Height'
    numerical2= 'Weight'

    komp.compare_box(category, numerical)
    komp.density(category, numerical2)
    komp.compare_histograms(category, numerical1)