from flask import Blueprint, jsonify

telemetry_bp = Blueprint("telemetry", __name__)

# For demo, return dummy telemetry
@telemetry_bp.route("/", methods=["GET"])
def get_telemetry():
    return jsonify({"position": 90})
