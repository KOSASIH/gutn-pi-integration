# config/config.py
import json

class Config:
    def __init__(self, config_file: str):
        with open(config_file, 'r') as f:
            self.data = json.load(f)

    def get(self, key: str, default=None):
        return self.data.get(key, default)
