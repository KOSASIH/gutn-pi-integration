from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

class Algorithms:
    @staticmethod
    def k_means(X, k):
        return KMeans(n_clusters=k).fit(X)

    @staticmethod
    def pca(X, n_components):
        return PCA(n_components=n_components).fit(X)

    @staticmethod
    def random_forest(X, y, n_estimators=100, max_depth=None):
        return RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth).fit(X, y)

    @staticmethod
    def logistic_regression(X, y, penalty='l2', C=1.0):
        return LogisticRegression(penalty=penalty, C=C).fit(X, y)

    @staticmethod
    def k_nearest_neighbors(X, y, n_neighbors=5):
        return KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)

    @staticmethod
    def svm(X, y, kernel='linear', C=1.0):
        return SVC(kernel=kernel, C=C).fit(X, y)
