import matplotlib.pyplot as plt  
import pandas as pd 
from FileLoader import FileLoader


class MyPlotLib: 

    def histogram(self, data, features):
        data[features].hist()
        plt.show()
    
    def density(self,data, features) : 
      data[features].plot.density()
      plt.show()
    
    def pair_plot(self,df, features) :
        pd.plotting.scatter_matrix(df[features])
        plt.show()
    
    def box_plot(self,df, features):
      fig, ax = plt.subplots()
      ax.boxplot(df[features].dropna(), labels=features)
      plt.show()

if __name__ == "__main__":

    loader = FileLoader()
    mpl = MyPlotLib()

    data = loader.load("../athlete_events.csv")
    x = ["Height", "Weight"]
    y = ["Weight", "Height"]
    mpl.histogram(data, x)
    mpl.density(data, y)
    mpl.pair_plot(data, y)
    mpl.box_plot(data, y)