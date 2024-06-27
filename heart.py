import os
from app import create_app, db
from app.db_models import Predictions
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

def make_shell_context():
    return dict(db=db, Predictions=Predictions)