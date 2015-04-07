import filters
from flask import Flask
import os

from types import FunctionType

app = Flask(__name__)
app.debug = True
app.jinja_env.autoescape = False
app.jinja_env.filters['firstSentence'] = firstSentence
app.jinja_env.filters['entireFirstSentence'] = entireFirstSentence

# get database url from os environment variables, defaults to regular (rather than test) database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('APP_DB_URL', 'postgresql+psycopg2:///celebsdb')

# Auto imports all functions in filters.py to be jinja filters
for func_name in dir(filters):
  func = getattr(filters, func_name, None)
  if isinstance(func, FunctionType):
    app.jinja_env.filters[func_name] = func

app.config['tipfyext.jinja2'] = {
    'environment_args': {
         'autoescape': False,
    } 
}



from models import db
from views import viewsBlueprint
from api import apiBlueprint


db.app = app
db.init_app(app)
app.register_blueprint(viewsBlueprint)
app.register_blueprint(apiBlueprint)


