import numpy as np 
import sys 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



# https://www.lovelyanalytics.com/2016/09/06/k-means-comment-ca-marche/ 
# https://stackoverflow.com/questions/3518778/how-do-i-read-csv-data-into-a-record-array-in-numpy
# https://stackoverflow.com/questions/39390418/python-how-can-i-enable-use-of-kwargs-when-calling-from-command-line-perhaps



class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
        self.array = None 

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """

        # centroids = X.copy() 
        # np.random.shuffle(centroids)
        # self.centroids = centroids[:self.ncentroid]
        # plt.scatter(X[:,0], X[:,1])
        # plt.scatter(self.centroids[:,0], self.centroids[:,1], c='r', s=100)
        # distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2)) 
        # deminor = np.argmin(distances, axis=0) 

        # INIT VISUALIZATION 
        self.centroids = np.random.randn(self.ncentroid, X.shape[1]) * np.std(X, axis=0) + np.mean(X, axis=0)
        graph = plt.figure()
        dotcolor = 10*["g", "c", "k", "r", "b"]
        draw = Axes3D(graph) 
        for el in range(X.shape[0]) :
            dot = dotcolor[4] 
            draw.scatter(X[el][0], X[el][1], color = dot)
        for i, el in enumerate(self.centroids) :
            dot = dotcolor[i] 
            draw.scatter(el[0], el[1], el[2], color = dot, marker= "x")
        plt.show() 
        
        dist = np.zeros(X.shape[0], self.ncentroid)
        self.clustering = np.zeros(X.shape[0])
        
        # Getting the mean 
        for i in range(self.max_iter) :
            for i in range(self.ncentroid) :
                self.dist[:,i] = np.linalg.norm(X - self.centroids[i], axis=1)
            self.clustering = np.argmin(dist, axis = 1) 

            # Affinage 
            for i in range(self.ncentroid): 
                self.centroids[i] = np.mean(X[self.clustering == i], axis = 0)
        self.table = np.zeros(X.shape[0], X.shape[1] + 1) # + 1 not needed ?
        self.table[:,:-1] = X
        self.table[:,3] = self.clustering 

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        y = [self.table[self.table[:,3]==k] for k in np.unique(self.table[:,3])]
        moy = np.zeros((self.ncentroid, X.shape[1] + 1))
        for i, el in enumerate(y) :
            moy[i] = el.mean(axis=0) 
        moy = moy[moy[:, 0].argsort()]
        ret = np.chararray(shape=(X.shape[0], 1))
        for el in range(X.shape[0]):
            if self.table[i][3] == moy[0][3]:
                ret[i] = "The flying cities of Venus,"
            elif self.table[i][3] == moy[1][3]:
                ret[i] = "United Nations of Earth"
            elif self.table[i][3] == moy[2][3] :
                ret[i] = "Mars Republic,"
            elif self.table[i][3] == moy[3][3] :
                ret[i] = "Asteroids' Belt colonies."
        return ret

    def drawing(self) :

        dotcolors = 10*["g", "c", "k", "r", "b"]
        graph = plt.figure()
        draw = Axes3D(graph)

        for el in range(self.table.shape[0]):
            dot = dotcolors[int(self.table[el][3])] 
            draw.scatter(self.table[el][0], self.table[el][1], self.table[el][2], color = dot)
        
        for i, value in enumerate(self.centroids) :
            dot = dotcolors[i] 
            draw.scatter(value[0], value[1], value[2], s = 130, color = dot, marker= "x")
        plt.show()
            
    






def main(**kwargs) : 
    ret = KmeansClustering()
    for key, value in kwargs.items() :
        setattr(ret, key, value) 
    return ret  



if __name__ == "__main__":

    cluster = main(**dict(arg.split('=') for arg in sys.argv[1:])) 
    array = np.genfromtxt(cluster.filepath,delimiter=',')


