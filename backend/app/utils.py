"""
Utility functions for Smart Robotic Arm backend.
Includes helper methods for JSON responses, validation, logging, and data formatting.
"""

import json
import datetime
from flask import jsonify


def json_response(data=None, message="", status=200):
    """
    Create a standardized JSON response.

    :param data: Dictionary or list to include in the response
    :param message: Message string
    :param status: HTTP status code
    :return: Flask Response object
    """
    response = {
        "status": status,
        "message": message,
        "data": data
    }
    return jsonify(response), status


def validate_payload(payload, required_fields):
    """
    Validate that required fields exist in the payload.

    :param payload: Incoming JSON data
    :param required_fields: List of keys to validate
    :return: (bool, missing_fields)
    """
    missing_fields = [field for field in required_fields if field not in payload]
    return (len(missing_fields) == 0, missing_fields)


def current_timestamp():
    """
    Returns current timestamp in ISO format.
    """
    return datetime.datetime.utcnow().isoformat()


def pretty_print(data):
    """
    Print data in a formatted JSON string for debugging.
    """
    print(json.dumps(data, indent=4, sort_keys=True, default=str))


def parse_command(command_str):
    """
    Parse a robot command string into a dictionary.

    Example:
        Input: "MOVE:angle=90,speed=5"
        Output: {"action": "MOVE", "params": {"angle": 90, "speed": 5}}
    """
    try:
        parts = command_str.split(":")
        action = parts[0]
        params = {}
        if len(parts) > 1:
            param_pairs = parts[1].split(",")
            for pair in param_pairs:
                key, value = pair.split("=")
                params[key.strip()] = float(value) if value.replace(".", "", 1).isdigit() else value.strip()

        return {"action": action, "params": params}
    except Exception as e:
        print(f"[ERROR] Failed to parse command: {e}")
        return None
