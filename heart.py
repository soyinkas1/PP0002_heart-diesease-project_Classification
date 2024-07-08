import os
from app import create_app, db
from app.db_models import HeartPredictions
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()
configuration= os.getenv('FLASK_CONFIG') 
print(configuration)
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

def make_shell_context():
    return dict(db=db, Predictions=HeartPredictions)