import config

def test_mqtt_config():
    assert isinstance(config.MQTT_BROKER, str)
    assert isinstance(config.MQTT_PORT, int)
    assert config.MQTT_PORT == 1883

def test_topics():
    assert config.TOPIC_COMMAND.startswith("robotic_arm")
    assert config.TOPIC_TELEMETRY.startswith("robotic_arm")

def test_motor_defaults():
    assert config.DEFAULT_SPEED == 50
