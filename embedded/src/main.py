import time
from motor_control import MotorController
from sensor_interface import SensorReader
from mqtt_client import MQTTClient
import config
from utils import log

def main():
    motor = MotorController()
    sensor = SensorReader()
    mqtt_client = MQTTClient(config.MQTT_BROKER, config.MQTT_PORT, config.TOPIC_COMMAND, motor)

    mqtt_client.connect()
    log("MQTT connected. Waiting for commands...")

    while True:
        position = sensor.read_position()
        telemetry = {"position": position}
        mqtt_client.publish(config.TOPIC_TELEMETRY, telemetry)
        log(f"Telemetry sent: {telemetry}")
        time.sleep(config.TELEMETRY_INTERVAL)

if __name__ == "__main__":
    main()
