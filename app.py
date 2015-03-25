from flask import Flask

app = Flask(__name__)
app.jinja_env.autoescape = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2:///celebsdb'
app.config['tipfyext.jinja2'] = {
    'environment_args': {
         'autoescape': False,
    } 
}
