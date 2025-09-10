import random

class SensorReader:
    def __init__(self):
        print("SensorReader initialized")

    def read_position(self):
        # Simulate sensor position
        return random.randint(0, 180)
