import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from kafka import KafkaConsumer

def collect_data(sources):
    """
    Collect data from various sources and store it in a pandas dataframe.

    Parameters:
    sources (list): List of data sources (e.g. APIs, databases, files)

    Returns:
    pd.DataFrame: Collected data
    """
    data = []
    for source in sources:
        if source['type'] == 'api':
            response = requests.get(source['url'])
            data.append(pd.json_normalize(response.json()))
        elif source['type'] == 'database':
            conn = psycopg2.connect(**source['credentials'])
            cursor = conn.cursor()
            cursor.execute(source['query'])
            data.append(pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description]))
        elif source['type'] == 'file':
            data.append(pd.read_csv(source['path']))
        elif source['type'] == 'kafka':
            consumer = KafkaConsumer(source['topic'], bootstrap_servers=source['bootstrap_servers'])
            for message in consumer:
                data.append(pd.json_normalize(message.value))
    return pd.concat(data, ignore_index=True)

def collect_realtime_data(sources):
    """
    Collect real-time data from various sources and store it in a pandas dataframe.

    Parameters:
    sources (list): List of data sources (e.g. APIs, databases, files)

    Returns:
    pd.DataFrame: Collected real-time data
    """
    data = []
    for source in sources:
        if source['type'] == 'kafka':
            consumer = KafkaConsumer(source['topic'], bootstrap_servers=source['bootstrap_servers'])
            for message in consumer:
                data.append(pd.json_normalize(message.value))
    return pd.concat(data, ignore_index=True)
