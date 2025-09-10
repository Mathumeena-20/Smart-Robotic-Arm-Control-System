"""
MQTT Service Layer
Handles MQTT connection, publishing, and subscription for the robotic system.
"""

import json
import threading
import paho.mqtt.client as mqtt
from flask import current_app

# MQTT configuration will be loaded from Flask app config
mqtt_client = None


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[MQTT] Connected successfully")
        # Subscribe to required topics after connection
        client.subscribe("robotic_arm/sensor")
        client.subscribe("robotic_arm/status")
    else:
        print(f"[MQTT] Connection failed with code {rc}")


def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode('utf-8')
        data = json.loads(payload)
        print(f"[MQTT] Message received on {msg.topic}: {data}")

        # Process incoming data based on topic
        if msg.topic == "robotic_arm/sensor":
            handle_sensor_data(data)
        elif msg.topic == "robotic_arm/status":
            handle_status_update(data)
    except Exception as e:
        print(f"[MQTT ERROR] Failed to process message: {e}")


def handle_sensor_data(data):
    """
    Handle incoming sensor data from the robot.
    """
    print(f"[SENSOR DATA] {data}")
    # TODO: Store in database if needed


def handle_status_update(data):
    """
    Handle status update messages from the robot.
    """
    print(f"[STATUS UPDATE] {data}")
    # TODO: Update RobotState in DB if required


def connect_mqtt(app):
    """
    Initialize and connect the MQTT client using Flask app config.
    """
    global mqtt_client
    mqtt_client = mqtt.Client()

    # Set event handlers
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    # Load credentials from app config
    mqtt_broker = app.config.get("MQTT_BROKER", "localhost")
    mqtt_port = app.config.get("MQTT_PORT", 1883)
    mqtt_user = app.config.get("MQTT_USER", None)
    mqtt_password = app.config.get("MQTT_PASSWORD", None)

    if mqtt_user and mqtt_password:
        mqtt_client.username_pw_set(mqtt_user, mqtt_password)

    # Connect to the broker
    mqtt_client.connect(mqtt_broker, mqtt_port, keepalive=60)

    # Run MQTT loop in a background thread
    thread = threading.Thread(target=mqtt_client.loop_forever)
    thread.daemon = True
    thread.start()
    print("[MQTT] Client started")


def publish_command(command):
    """
    Publish a command to the robot via MQTT.

    :param command: dict with command details
    """
    if mqtt_client:
        topic = "robotic_arm/command"
        payload = json.dumps(command)
        mqtt_client.publish(topic, payload)
        print(f"[MQTT] Command published: {payload}")
    else:
        print("[MQTT ERROR] Client not initialized")
