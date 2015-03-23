from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from json import JSONEncoder 
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2:///celebsdb'
db = SQLAlchemy(app)

def get_ids(t):
  return list(set(c.id for c in t))

class JsonBuilder:

  json_attr = ()
  json_attr_func = ()

  def to_json(self):
    json_map = {}
    json_map.update({p:getattr(self, p) for p in self.json_attr})
    json_map.update({k:f(getattr(self,k)) for k,f in self.json_attr_func})
    return json_map

class Celebrity(db.Model, JsonBuilder):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.Text)

  attorneys = db.relationship("Attorney", secondary='charge')
  crimes = db.relationship("Crime", secondary='charge')
  charges = db.relationship("Charge")

  json_attr = ('id', 'name', 'description')
  json_attr_func = [(k,get_ids) for k in ('attorneys', 'crimes', 'charges')]

  def __init__(self, name, description = None):
    self.name = name
    self.description = description

  def __repr__(self):
    return '(Celebrity %r)' % self.name


class Attorney(db.Model, JsonBuilder):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  firm = db.Column(db.String(80), unique=True)

  celebrities = db.relationship("Celebrity", secondary='charge')
  crimes = db.relationship("Crime", secondary='charge')
  charges = db.relationship("Charge")

  json_attr = ('id', 'name', 'firm')
  json_attr_func = [(k,get_ids) for k in ('celebrities', 'crimes', 'charges')]

  def __init__(self, name, firm = None):
    self.name = name
    self.firm = firm

  def __repr__(self):
    return '(Attorney %r)' % self.name
      
class Crime(db.Model, JsonBuilder):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True)
  celebrities = db.relationship("Celebrity", secondary='charge')
  attorneys = db.relationship("Attorney", secondary='charge')
  charges = db.relationship("Charge")

  json_attr = ('id', 'title')
  json_attr_func = [(k,get_ids) for k in ('celebrities', 'attorneys', 'charges')]

  def __init__(self, title):
    self.title = title 

  def __repr__(self):
    return '(Crime %r)' % self.title


# make this association table
class Charge(db.Model, JsonBuilder):

  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime)
  location = db.Column(db.String(80), unique=True)

  celebrity_id = db.Column(db.Integer, db.ForeignKey('celebrity.id'))
  attorney_id = db.Column(db.Integer, db.ForeignKey('attorney.id'))
  crime_id = db.Column(db.Integer, db.ForeignKey('crime.id'))
  
  crime = db.relationship('Crime')
  attorney = db.relationship('Attorney')
  celebrity = db.relationship('Celebrity')

  json_attr = ('crime_id', 'attorney_id', 'crime_id', 'location')  
  json_attr_func = [('date', lambda d : d.strftime("%m-%d-%Y"))]

  def __init__(self, celebrity, crime, attorney, date , location):
    self.celebrity = celebrity
    self.crime = crime
    self.attorney = attorney
    self.date = date
    self.location = location


  def __repr__(self):
    return '(Charge %r %r %r)' % (self.crime, self.celebrity, self.attorney)
