#!flask3/bin/python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from json import JSONEncoder 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2:///celebsdb'
db = SQLAlchemy(app)

# Wrapper for a dictionary to build up JSON for each model
class JSONMap:
  def __init__(self, model):
    self.json_map = dict()
    self.model = model

  def add(self, key, value):
    self.json_map[key] = value
    return self
    
  def add_scalars(self,*scalars):
    for s in scalars:
      self.json_map[s] = self.model.__dict__[s]
    return self
  
  def add_for_charges(self, name, f):
    self.json_map[name] = list(set(f(c) for c in self.model.charges.all()))
    return self
  def add_celebrities(self):
    return self.add_for_charges('celebrities', lambda c:c.celebrity_id)
  def add_crimes(self):
    return self.add_for_charges('crimes', lambda c:c.crime_id)
  def add_charges(self):
    return self.add_for_charges('charges', lambda c:c.id)
  def add_attorneys(self):
    return self.add_for_charges('attorneys', lambda c:c.attorney_id)


class Celebrity(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.Text)

  def __init__(self, name, description = None):
    self.name = name
    self.description = description

  def __repr__(self):
    return '(Celebrity %r)' % self.name

  def to_json(self):
    return JSONMap(self).add_scalars('id', 'name', 'description') \
            .add_attorneys() \
            .add_crimes() \
            .add_charges().json_map


class Attorney(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  firm = db.Column(db.String(80), unique=True)

  def __init__(self, name, firm = None):
    self.name = name
    self.firm = firm

  def __repr__(self):
    return '(Attorney %r)' % self.name

  def to_json(self):
    return JSONMap(self) \
            .add_scalars('id', 'name', 'firm') \
            .add_celebrities() \
            .add_crimes() \
            .add_charges().json_map
      
class Crime(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True)

  def __init__(self, title):
    self.title = title 
  def __repr__(self):
    return '(Crime %r)' % self.title

  def to_json(self):
     return JSONMap(self).add_scalars('id', 'title') \
            .add_attorneys() \
            .add_celebrities() \
            .add_charges().json_map


class Charge(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime)
  location = db.Column(db.String(80), unique=True)
  celebrity_id = db.Column(db.Integer, db.ForeignKey('celebrity.id'))
  celebrity = db.relationship('Celebrity', backref=db.backref('charges', lazy='dynamic'))
  attorney_id = db.Column(db.Integer, db.ForeignKey('attorney.id'))
  attorney = db.relationship('Attorney', backref=db.backref('charges', lazy='dynamic'))
  crime_id = db.Column(db.Integer, db.ForeignKey('crime.id'))
  crime = db.relationship('Crime', backref=db.backref('charges', lazy='dynamic'))

  def __init__(self, celebrity, crime, attorney, date , location):
    self.celebrity = celebrity
    self.crime = crime
    self.attorney = attorney
    self.date = date
    self.location = location

  def __repr__(self):
    return '(Charge %r %r %r)' % (self.crime, self.celebrity, self.attorney)

  def to_json(self):
    return JSONMap(self).add_scalars('celebrity_id', 'attorney_id', 'crime_id', 'location') \
                        .add('date', self.date.strftime("%m-%d-%Y")) \
                        .json_map


