from flask import Blueprint, jsonify

robot_bp = Blueprint('robot', __name__)

@robot_bp.route('/robots', methods=['GET'])
def get_robots():
    return jsonify({"message": "Robots list endpoint working!"})
