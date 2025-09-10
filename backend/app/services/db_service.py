"""
Database Service Layer
Provides helper functions to interact with the database.
"""

from app.models import db, RobotState
from sqlalchemy.exc import SQLAlchemyError


def add_robot_state(data):
    """
    Add a new RobotState record to the database.

    :param data: dict containing robot state info
    :return: RobotState instance or None
    """
    try:
        state = RobotState(
            joint1_angle=data.get("joint1_angle"),
            joint2_angle=data.get("joint2_angle"),
            joint3_angle=data.get("joint3_angle"),
            joint4_angle=data.get("joint4_angle"),
            joint5_angle=data.get("joint5_angle"),
            joint6_angle=data.get("joint6_angle"),
            gripper_open=data.get("gripper_open", True),
            mode=data.get("mode", "MANUAL"),
            health_status=data.get("health_status", "OK")
        )
        db.session.add(state)
        db.session.commit()
        return state
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"[DB ERROR] Failed to add RobotState: {e}")
        return None


def get_latest_robot_state():
    """
    Fetch the latest robot state from the database.

    :return: RobotState instance or None
    """
    try:
        return RobotState.query.order_by(RobotState.timestamp.desc()).first()
    except SQLAlchemyError as e:
        print(f"[DB ERROR] Failed to fetch latest RobotState: {e}")
        return None


def get_all_robot_states():
    """
    Fetch all robot states.

    :return: List of RobotState instances
    """
    try:
        return RobotState.query.order_by(RobotState.timestamp.desc()).all()
    except SQLAlchemyError as e:
        print(f"[DB ERROR] Failed to fetch all RobotStates: {e}")
        return []


def delete_robot_state(state_id):
    """
    Delete a RobotState by ID.

    :param state_id: int
    :return: True if deleted, False otherwise
    """
    try:
        state = RobotState.query.get(state_id)
        if not state:
            return False
        db.session.delete(state)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"[DB ERROR] Failed to delete RobotState: {e}")
        return False
