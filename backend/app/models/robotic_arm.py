from app.extensions import db

class RoboticArm(db.Model):
    __tablename__ = 'robotic_arms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='idle')
    position_x = db.Column(db.Float, default=0.0)
    position_y = db.Column(db.Float, default=0.0)
    position_z = db.Column(db.Float, default=0.0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'position_x': self.position_x,
            'position_y': self.position_y,
            'position_z': self.position_z
        }
