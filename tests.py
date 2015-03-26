from unittest import TestCase, main
from models import db, Celebrity, Crime, Charge, CelebrityAlias, CrimeDescription
from datetime import date
from app import app
import json


# at url routes to app
from views import *
from api import *


class TestModels(TestCase):

  def setUp(self):
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2:///testsdb'

    # May want these settings for testing api calls 
    app.config['WTF_CSRF_ENABLED'] = False
    self.app = app.test_client()


    db.create_all()


    self.speeding = Crime("Speeding", "www.speeding.com")
    self.ched = Celebrity(name='Ched', description='Actor', twitter_handle='@Ched', 
                  birthday=date(1900,1,1), wiki_url='ched.wiki', imdb_url='ched.imdb', picture_url='ched.picture')
    self.charge1 = Charge(date=date(2000,1,1), location='Austin, Texas', 
              description='Driving Fast!', attorney='James Funk',
              classification='Class A misdemeanor', 
              crime = self.speeding, 
              celebrity = self.ched)

    self.cr1 = Crime("1")
    self.cr2 = Crime("2")
    self.ce1 = Celebrity("1")
    self.ce2 = Celebrity("2")



  def tearDown(self):
    db.session.remove()
    db.drop_all()


  ### Test model attributes ###
  def test_crime_attributes(self):
    c = self.speeding
    self.assertEqual(c.name, "Speeding")
    self.assertEqual(c.wiki_url, "www.speeding.com")
    self.assertEqual(c.descriptions, [])
    self.assertEqual(c.celebrities, [])
    self.assertEqual(c.charges, [])

  def test_celebrity_attributes(self):
    c = self.ched
    self.assertEqual(c.name, "Ched")
    self.assertEqual(c.description, 'Actor')
    self.assertEqual(c.twitter_handle, "@Ched")
    self.assertEqual(c.birthday, date(1900,1,1))
    self.assertEqual(c.wiki_url, "ched.wiki")
    self.assertEqual(c.imdb_url, "ched.imdb")
    self.assertEqual(c.picture_url, "ched.picture")
    self.assertEqual(c.charges, [])
    self.assertEqual(c.crimes, [])
    self.assertEqual(c.aliases, [])

  def test_charge_attributes(self):
    c = self.charge1
    self.assertEqual(c.date, date(2000,1,1))
    self.assertEqual(c.description, 'Driving Fast!')
    self.assertEqual(c.location, 'Austin, Texas')
    self.assertEqual(c.attorney, 'James Funk')
    self.assertEqual(c.classification, 'Class A misdemeanor')
    self.assertEqual(c.crime, self.speeding)
    self.assertEqual(c.celebrity, self.ched)

  def test_celebrity_alias_attributes(self):
    alias = CelebrityAlias("Cheese Man", self.ched)
    self.assertEqual(alias.alias, "Cheese Man")
    self.assertEqual(alias.celebrity, self.ched)
  
  def test_crimedescription_attributes(self):
    desc = CrimeDescription(location='Austin', description='Driving Fast', crime=self.speeding)    
    self.assertEqual(desc.location, 'Austin')
    self.assertEqual(desc.description, 'Driving Fast')
    self.assertEqual(desc.crime, self.speeding)


  ### Test models in db ###
  def test_crime_in_db(self):
    c = self.speeding
    db.session.add(c)
    db.session.commit()
    self.assertEqual(Crime.query.all(), [c])

  def test_celebrity_in_db(self):
    c = self.ched
    db.session.add(c)
    db.session.commit()
    self.assertEqual(Celebrity.query.all(), [c])

  def test_charge_in_db(self):
    c = self.charge1
    db.session.add(c)
    db.session.commit()
    self.assertEqual(Charge.query.all(), [c])

  def test_celebrity_alias_in_db(self):
    alias = CelebrityAlias("Cheese Man", self.ched)
    db.session.add(alias)
    db.session.commit()
    self.assertEqual(CelebrityAlias.query.all(), [alias])

  def test_crimedescription_in_db(self):
    desc = CrimeDescription(location='Austin', description='Driving Fast', crime=self.speeding)    
    db.session.add(desc)
    db.session.commit()
    self.assertEqual(CrimeDescription.query.all(), [desc])


  ### Query attributes ###
  def test_celebs_charges(self):
    charge1 = Charge(self.ce1, self.cr1)
    charge2 = Charge(self.ce1, self.cr1)
    db.session.add_all([charge1, charge2])
    db.session.commit()
    self.assertEqual(set(self.ce1.charges), {charge1, charge2})

  def test_celebs_crimes(self):
    charge1 = Charge(self.ce1, self.cr1)
    charge2 = Charge(self.ce1, self.cr2)
    db.session.add_all([charge1, charge2])
    db.session.commit()
    self.assertEqual(set(self.ce1.crimes), {self.cr1, self.cr2})

  def test_crimes_charges(self):
    charge1 = Charge(self.ce1, self.cr1)
    charge2 = Charge(self.ce2, self.cr1)
    db.session.add_all([charge1, charge2])
    db.session.commit()
    self.assertEqual(set(self.cr1.charges), {charge1, charge2})

  def test_crimes_celebs(self):
    charge1 = Charge(self.ce1, self.cr1)
    charge2 = Charge(self.ce2, self.cr1)
    db.session.add_all([charge1, charge2])
    db.session.commit()
    self.assertEqual(set(self.cr1.celebrities), {self.ce1, self.ce2})


  ### Query attributes don't have duplicates ###
  # Only test these relations as they're the only query that contain join
  # and might have duplicates
  def test_celebs_crimes_no_dups(self):
    charge1 = Charge(self.ce1, self.cr1)
    charge2 = Charge(self.ce1, self.cr1)
    db.session.add_all([charge1, charge2])
    db.session.commit()
    self.assertEqual(self.ce1.crimes, [self.cr1])


  def test_crimes_celebs_no_dups(self):
    charge1 = Charge(self.ce1, self.cr1)
    charge2 = Charge(self.ce1, self.cr1)
    db.session.add_all([charge1, charge2])
    db.session.commit()
    self.assertEqual(self.cr1.celebrities, [self.ce1])


  ### Test API functions ###
  def test_celebrities_api(self):
    charge1 = Charge(self.ce1, self.cr1)
    charge2 = Charge(self.ce2, self.cr1)
    db.session.add_all([charge1, charge2])
    db.session.commit()

    response_json = self.get_json_from_url('/api/celebrity')
    expected = [{'id': 1, 'name': '1', 'uri': 'http://localhost/api/celebrity/1'}, 
        {'id': 2, 'name': '2', 'uri': 'http://localhost/api/celebrity/2'}]

    self.assertEqual(response_json, expected)

  def test_celebrity_api(self):
    charge1 = Charge(self.ce1, self.cr1)
    charge2 = Charge(self.ce1, self.cr2)
    alias = CelebrityAlias("One", self.ce1)
    db.session.add_all([charge1, charge2, alias])
    db.session.commit()

    expected = {
      'name': '1', 
      'id': 1, 
      'charges': [{'uri': 'http://localhost/api/charge/1', 'id': 1}, 
                  {'uri': 'http://localhost/api/charge/2', 'id': 2}],
      'crimes' : [{'uri': 'http://localhost/api/crime/1', 'id': 1, 'name': '1'}, 
                  {'uri': 'http://localhost/api/crime/2', 'id': 2, 'name': '2'}],
      'aliases': [{'id': 1, 'alias': 'One'}],
      'description': None, 
      'picture_url': None, 
      'imdb_url': None, 
      'wiki_url': None, 
      'twitter_handle' : None,
      'birthday': None, 
    }
    response_json = self.get_json_from_url('/api/celebrity/1')
    self.assertEqual(response_json, expected)

  def test_crimes_api(self):
    charge1 = Charge(self.ce1, self.cr1)
    charge2 = Charge(self.ce2, self.cr2)
    db.session.add_all([charge1, charge2])
    db.session.commit()

    expected = [{'name': '1', 'uri': 'http://localhost/api/crime/1', 'id': 1}, 
                {'name': '2', 'uri': 'http://localhost/api/crime/2', 'id': 2}]

    response_json = self.get_json_from_url('/api/crime')
    self.assertEqual(response_json, expected)
 
  def test_crime_api(self):
    charge1 = Charge(self.ce1, self.cr1)
    charge2 = Charge(self.ce2, self.cr1)
    cr1_desc = CrimeDescription('crime description', self.cr1)
    db.session.add_all([charge1, charge2, cr1_desc])
    db.session.commit()
    expected = {'descriptions': [{'location': None, 'description': 'crime description', 'id': 1}], 
                'wiki_url': None, 
                'id': 1, 
                'name': '1', 
                'celebrities': [{'uri': 'http://localhost/api/celebrity/1', 'id': 1, 'name': '1'}, 
                                {'uri': 'http://localhost/api/celebrity/2', 'id': 2, 'name': '2'}], 
                'charges': [{'uri': 'http://localhost/api/charge/1', 'id': 1}, 
                            {'uri': 'http://localhost/api/charge/2', 'id': 2}]}
    response_json = self.get_json_from_url('/api/crime/1')
    self.assertEqual(response_json, expected)
 
  def test_charges_api(self):
    charge1 = Charge(self.ce1, self.cr1)
    charge2 = Charge(self.ce2, self.cr1)
    db.session.add_all([charge1, charge2])
    db.session.commit()
    expected = [{'uri': 'http://localhost/api/charge/1', 'id': 1}, 
                {'uri': 'http://localhost/api/charge/2', 'id': 2}]
    response_json = self.get_json_from_url('/api/charge')
    self.assertEqual(response_json, expected)

  def test_charge_api(self):
    charge1 = Charge(self.ce1, self.cr2)
    db.session.add_all([charge1])
    db.session.commit()
    response_json = self.get_json_from_url('/api/charge/1')


    expected = {'crime': {'name': '2', 'id': 1, 'uri': 'http://localhost/api/crime/1'}, 
                'celebrity': {'name': '1', 'id': 1, 'uri': 'http://localhost/api/celebrity/1'}, 
                'classification': None, 
                'location': None, 
                'attorney': None, 
                'date': None, 
                'description': None}

    self.assertEqual(response_json, expected)
    


   



  def get_json_from_url(self, url):
    str_data = self.app.get(url).get_data().decode("utf-8")
    return json.loads(str_data)


if __name__ == "__main__" :
  main()   
