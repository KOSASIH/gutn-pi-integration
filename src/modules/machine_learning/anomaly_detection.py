import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    # Load the historical sensor readings
    df = pd.read_csv('sensor_data.csv')

    # Preprocess the data
    df = preprocess_data(df)

    # Train the anomaly detection model
    model = train_model(df)

    # Detect anomalies in the given data
    anomalies = model.predict(data.reshape(1, -1))

    return anomalies

def preprocess_data(df):
    # Preprocess the historical sensor readings
    # This step may include cleaning the data, handling missing values, and extracting features

    # Example: Extract the temperature and pressure from the sensor readings
    df['temperature'] = df['sensor_readings'].apply(lambda x: x['temperature'])
    df['pressure'] = df['sensor_readings'].apply(lambda x: x['pressure'])

    # Drop unnecessary columns
    df.drop(['sensor_readings'], axis=1, inplace=True)

    return df

def train_model(df):
    # Train the anomaly detection model
    # This step may include splitting the data into training and testing sets, selecting features, and training the model

    # Example: Use an isolation forest to detect anomalies
    X = df.drop(['anomaly'], axis=1)
    y = df['anomaly']

    model = IsolationForest(random_state=42)
    model.fit(X)

    return model
