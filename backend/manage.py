from flask.cli import FlaskGroup
from app import create_app, db

app = create_app()
cli = FlaskGroup(app)

@cli.command("create_tables")
def create_tables():
    """Create database tables."""
    with app.app_context():
        db.create_all()
        print("✅ Tables created successfully")

if __name__ == "__main__":
    cli()
