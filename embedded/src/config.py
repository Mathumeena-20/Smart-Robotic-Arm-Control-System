# Configuration file for Embedded Robotic Arm

MQTT_BROKER = "mqtt"        # MQTT service name in docker-compose
MQTT_PORT = 1883
TOPIC_COMMAND = "robotic_arm/commands"
TOPIC_TELEMETRY = "robotic_arm/telemetry"

TELEMETRY_INTERVAL = 1  # seconds between telemetry updates

# Motor settings
DEFAULT_SPEED = 50
