from flask import Flask
from filters import *

app = Flask(__name__)
app.debug = True
app.jinja_env.autoescape = False
app.jinja_env.filters['firstSentence'] = firstSentence
app.jinja_env.filters['entireFirstSentence'] = entireFirstSentence
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2:///celebsdb'
app.config['tipfyext.jinja2'] = {
    'environment_args': {
         'autoescape': False,
    } 
}
