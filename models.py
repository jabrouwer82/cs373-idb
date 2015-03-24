from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


class Celebrity(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.Text)

  attorneys = db.relationship("Attorney", secondary='charge')
  crimes = db.relationship("Crime", secondary='charge')
  charges = db.relationship("Charge")

  def __init__(self, name, description = None):
    self.name = name
    self.description = description

  def __repr__(self):
    return '(Celebrity %r)' % self.name


class Attorney(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  firm = db.Column(db.String(80))

  celebrities = db.relationship("Celebrity", secondary='charge')
  crimes = db.relationship("Crime", secondary='charge')
  charges = db.relationship("Charge")

  def __init__(self, name, firm = None):
    self.name = name
    self.firm = firm

  def __repr__(self):
    return '(Attorney %r)' % self.name
      
class Crime(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  celebrities = db.relationship("Celebrity", secondary='charge')
  attorneys = db.relationship("Attorney", secondary='charge')
  charges = db.relationship("Charge")

  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return '(Crime %r)' % self.name


# make this association table
class Charge(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime)
  location = db.Column(db.String(80))

  celebrity_id = db.Column(db.Integer, db.ForeignKey('celebrity.id'))
  attorney_id = db.Column(db.Integer, db.ForeignKey('attorney.id'))
  crime_id = db.Column(db.Integer, db.ForeignKey('crime.id'))
  
  crime = db.relationship('Crime')
  attorney = db.relationship('Attorney')
  celebrity = db.relationship('Celebrity')

  def __init__(self, celebrity, crime, attorney, date , location):
    self.celebrity = celebrity
    self.crime = crime
    self.attorney = attorney
    self.date = date
    self.location = location


  def __repr__(self):
    return '(Charge %r %r %r)' % (self.crime, self.celebrity, self.attorney)
