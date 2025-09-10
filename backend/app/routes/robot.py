import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/robotdb")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MQTT_BROKER = os.getenv("MQTT_BROKER", "mqtt")
    MQTT_PORT = 1883
