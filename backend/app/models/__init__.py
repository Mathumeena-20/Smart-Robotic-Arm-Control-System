from .robotic_arm import RoboticArm
from .robot_state import RobotState  # if exists

"""
This module initializes the models package for the backend.
It ensures that all database models can be imported from this package.
"""

from flask_sqlalchemy import SQLAlchemy

# Global SQLAlchemy instance
db = SQLAlchemy()

# Import individual models here so they can be accessed directly from models package
from .robotic_arm import RoboticArm
from .sensor_data import SensorData
from .command import Command

__all__ = ["db", "RoboticArm", "SensorData", "Command"]
