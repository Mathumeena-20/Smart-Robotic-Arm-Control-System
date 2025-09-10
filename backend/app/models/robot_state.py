from app.extensions import db

class RobotState(db.Model):
    __tablename__ = 'robot_state'

    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(50))
    status = db.Column(db.String(50))
