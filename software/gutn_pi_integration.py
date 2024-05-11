import logging
from typing import List

logging.basicConfig(level=logging.INFO)

def main() -> None:
    # Initialize sensors
    sensors: List[Sensor] = [BME680(), SGP30()]

    # Read sensor data
    data: List[SensorData] = []
    for sensor in sensors:
        data.extend(sensor.read_data())

    # Process and store data
    process_data(data)

if __name__ == "__main__":
    main()
