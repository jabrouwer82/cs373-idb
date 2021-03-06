from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy_searchable import make_searchable
from sqlalchemy_utils.types import TSVectorType

db = SQLAlchemy()
make_searchable()

MAX_STRING = 4000

class Celebrity(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(MAX_STRING))
  description = db.Column(db.Text)
  twitter_handle = db.Column(db.String(MAX_STRING))
  birthday = db.Column(db.DateTime)
  wiki_url = db.Column(db.String(MAX_STRING))
  imdb_url = db.Column(db.String(MAX_STRING))
  picture_url = db.Column(db.String(MAX_STRING))

  aliases = db.relationship('CelebrityAlias')
  crimes = db.relationship('Crime', secondary='charge')
  charges = db.relationship('Charge')

  search_vector = db.Column(TSVectorType('name', 'description', 'twitter_handle', 'wiki_url', 'imdb_url'))

  def __init__(self,
               name,
               description=None,
               twitter_handle=None,
               birthday=None,
               wiki_url=None,
               imdb_url=None,
               picture_url=None):
    self.name = name
    self.description = description
    self.twitter_handle=twitter_handle
    self.birthday = birthday
    self.wiki_url = wiki_url
    self.imdb_url = imdb_url
    self.picture_url = picture_url

  def __repr__(self):
    return '(Celebrity {num}: {name})'.format(name=self.name, num=self.id)

class CelebrityAlias(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  alias = db.Column(db.String(MAX_STRING))
  
  celebrity_id = db.Column(db.Integer, db.ForeignKey('celebrity.id'))
  
  celebrity = db.relationship('Celebrity')
  
  search_vector = db.Column(TSVectorType('alias'))
  
  def __init__(self, alias, celebrity):
    self.alias = alias
    self.celebrity = celebrity

  def __repr__(self):
    return '(Celebrity Alias {num}: {celebrity}/{alias})'.format(
        alias=self.alias, celebrity=self.celebrity, num=self.id)

class Crime(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(MAX_STRING))
  description = db.Column(db.Text)
  wiki_url = db.Column(db.String(MAX_STRING))

  celebrities = db.relationship('Celebrity', secondary='charge')
  charges = db.relationship('Charge')

  search_vector = db.Column(TSVectorType('name', 'description', 'wiki_url'))
  
  def __init__(self, name, wiki_url=None, description=None):
    self.name = name 
    self.wiki_url = wiki_url
    self.description=description

  def __repr__(self):
    return '(Crime {num}: {name})'.format(name=self.name, num=self.id)

# Association table
class Charge(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime)
  location = db.Column(db.String(MAX_STRING))
  description = db.Column(db.Text)
  classification = db.Column(db.String(MAX_STRING))

  celebrity_id = db.Column(db.Integer, db.ForeignKey('celebrity.id'))
  crime_id = db.Column(db.Integer, db.ForeignKey('crime.id'))
  
  crime = db.relationship('Crime')
  celebrity = db.relationship('Celebrity')

  search_vector = db.Column(TSVectorType('description', 'classification'))
  
  def __init__(self,
               celebrity,
               crime,
               date=None,
               location=None,
               description=None,
               classification=None):
    self.celebrity = celebrity
    self.crime = crime
    self.date = date
    self.location = location
    self.celebrity = celebrity
    self.crime = crime
    self.description = description
    self.classification = classification

  def __repr__(self):
    return '(Charge {num}: {celebrity}, {crime})'.format(
        self.id, self.crime, self.celebrity)

