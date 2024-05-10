import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class DataManager:
    def __init__(self, input_data_file, output_data_file, intermediate_data_file):
        self.input_data_file = input_data_file
        self.output_data_file = output_data_file
        self.intermediate_data_file = intermediate_data_file
        self.input_data = None
        self.output_data = None
        self.intermediate_data = None

    def load_data(self):
        self.input_data = pd.read_csv(self.input_data_file)
        self.output_data = pd.read_csv(self.output_data_file)
        self.intermediate_data = pd.read_csv(self.intermediate_data_file)

    def preprocess_data(self):
        # Handle missing values
        self.input_data.fillna(self.input_data.mean(), inplace=True)
        self.output_data.fillna(self.output_data.mean(), inplace=True)
        self.intermediate_data.fillna(self.intermediate_data.mean(), inplace=True)

        # Scale data using StandardScaler
        scaler = StandardScaler()
        self.input_data[['feature1', 'feature2', 'feature3']] = scaler.fit_transform(self.input_data[['feature1', 'feature2', 'feature3']])
        self.output_data[['target1', 'target2']] = scaler.fit_transform(self.output_data[['target1', 'target2']])
        self.intermediate_data[['intermediate_feature1', 'intermediate_feature2']] = scaler.fit_transform(self.intermediate_data[['intermediate_feature1', 'intermediate_feature2']])

        # Apply PCA for dimensionality reduction
        pca = PCA(n_components=0.95)
        self.input_data[['feature1', 'feature2', 'feature3']] = pca.fit_transform(self.input_data[['feature1', 'feature2', 'feature3']])
        self.intermediate_data[['intermediate_feature1', 'intermediate_feature2']] = pca.fit_transform(self.intermediate_data[['intermediate_feature1', 'intermediate_feature2']])

    def split_data(self, test_size=0.2, random_state=42):
        X_train, X_test, y_train, y_test = train_test_split(self.input_data, self.output_data, test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test

    def save_data(self):
        self.input_data.to_csv(self.input_data_file, index=False)
        self.output_data.to_csv(self.output_data_file, index=False)
        self.intermediate_data.to_csv(self.intermediate_data_file, index=False)
