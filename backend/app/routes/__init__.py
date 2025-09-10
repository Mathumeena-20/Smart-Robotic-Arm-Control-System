def register_routes(app):
    from .robot_routes import robot_bp
    app.register_blueprint(robot_bp, url_prefix="/api")
