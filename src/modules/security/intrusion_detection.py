import numpy as np
import pandas as pd
from scipy.cluster.vq import whiten, kmeans

def detect_intrusions(data):
    """
    Detect intrusions in the data using k-means clustering.

    Parameters:
    data (pd.DataFrame): Data to be analyzed

    Returns:
    pd.DataFrame: Data with intrusion labels
    """
    data = whiten(data.values)
    centroids, _ = kmeans(data, 2)
    labels = np.zeros(len(data))
    for i in range(len(data)):
        if np.linalg.norm(data[i] - centroids[1]) < np.linalg.norm(data[i] - centroids[0]):
            labels[i] = 1
    data['intrusion'] = labels
    return data
