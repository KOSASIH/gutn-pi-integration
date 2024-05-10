import os
import logging
import sys
import threading
import queue
import time
import signal
import traceback
import configparser
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
from core import app, sensors, actuators, machine_learning, exceptions

# Set up logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

# Set up configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Set up MQTT client
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(config.get('mqtt', 'broker'), int(config.get('mqtt', 'port')))
mqtt_client.loop_start()

# Set up message queue
message_queue = queue.Queue()

# Set up signal handler
def signal_handler(signal, frame):
    logging.info("Shutting down...")
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    sys.exit(0)

# Set up exception handler
def exception_handler(exception):
    logging.error(f"Unhandled exception: {str(exception)}")
    logging.error(traceback.format_exc())

# Set up main application loop
def main_loop():
    while True:
        try:
            # Get message from queue
            message = message_queue.get(block=True, timeout=1.0)

            # Parse message
            topic, payload = message
            logging.debug(f"Received message: {topic} {payload}")

            # Process message
            app.process_message(topic, payload)

            # Clean up resources
            message_queue.task_done()

        except queue.Empty:
            # Do nothing
            pass

        except exceptions.GUTNException as e:
            logging.error(str(e))

        except Exception as e:
            exception_handler(e)

# Set up sensor data collection loop
def sensor_data_collection_loop():
    while True:
        try:
            # Collect sensor data
            sensor_data = sensors.collect_data()

            # Publish sensor data
            publish.single(config.get('mqtt', 'sensor_data_topic'), sensor_data, qos=1)

        except exceptions.GUTNException as e:
            logging.error(str(e))

        except Exception as e:
            exception_handler(e)

        finally:
            # Sleep for a while
            time.sleep(config.getfloat('sensor_data_collection', 'interval'))

# Set up actuator control loop
def actuator_control_loop():
    while True:
        try:
            # Get actuator control message from queue
            message = actuators.get_control_message()

            # Control actuator
            actuators.control(message)

            # Publish actuator status
            publish.single(config.get('mqtt', 'actuator_status_topic'), "OK", qos=1)

        except exceptions.GUTNException as e:
            logging.error(str(e))

        except Exception as e:
            exception_handler(e)

        finally:
            # Sleep for a while
            time.sleep(config.getfloat('actuator_control', 'interval'))

# Set up machine learning loop
def machine_learning_loop():
    while True:
        try:
            # Get machine learning data from queue
            data = machine_learning.get_data()

            # Train machine learning model
            model = machine_learning.train(data)

            # Publish machine learning model
            publish.single(config.get('mqtt', 'machine_learning_model_topic'), model, qos=1)

        except exceptions.GUTNException as e:
            logging.error(str(e))

        except Exception as e:
            exception_handler(e)

# Set up MQTTmessage handler
def on_connect(client, userdata, flags, rc):
    logging.info(f"Connected to MQTT broker with result code {rc}")

    # Subscribe to topics
    subscribe.single(config.get('mqtt', 'command_topic'), 0, on_message)
    subscribe.single(config.get('mqtt', 'sensor_data_topic'), 0, on_message)
    subscribe.single(config.get('mqtt', 'actuator_status_topic'), 0, on_message)
    subscribe.single(config.get('mqtt', 'machine_learning_data_topic'), 0, on_message)

def on_message(client, userdata, message):
    logging.debug(f"Received MQTT message: {message.topic} {message.payload.decode()}")

    # Add message to queue
    message_queue.put((message.topic, message.payload.decode()))

# Set up signal handler
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Start main application loop
main_thread = threading.Thread(target=main_loop)
main_thread.start()

# Start sensor data collection loop
sensor_data_collection_thread = threading.Thread(target=sensor_data_collection_loop)
sensor_data_collection_thread.start()

# Start actuator control loop
actuator_control_thread = threading.Thread(target=actuator_control_loop)
actuator_control_thread.start()

# Start machine learning loop
machine_learning_thread = threading.Thread(target=machine_learning_loop)
machine_learning_thread.start()

# Wait for threads to finish
main_thread.join()
sensor_data_collection_thread.join()
actuator_control_thread.join()
machine_learning_thread.join()
