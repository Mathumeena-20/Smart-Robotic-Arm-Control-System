import json
import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker, port, topic_command, motor_controller):
        self.broker = broker
        self.port = port
        self.topic_command = topic_command
        self.motor_controller = motor_controller
        self.client = mqtt.Client()

    def connect(self):
        self.client.on_message = self.on_message
        self.client.connect(self.broker, self.port, 60)
        self.client.subscribe(self.topic_command)
        self.client.loop_start()

    def on_message(self, client, userdata, msg):
        command = json.loads(msg.payload.decode())
        direction = command.get("direction")
        speed = command.get("speed", 50)
        self.motor_controller.move(direction, speed)

    def publish(self, topic, message):
        self.client.publish(topic, json.dumps(message))
