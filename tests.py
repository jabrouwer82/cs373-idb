from unittest import TestCase, main
from models import db, Celebrity, Crime, Charge, CelebrityAlias, CrimeDescription
from datetime import date
from app import app


#TODO Remove import alls 
from views import *
from api import *


import json

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


  def test_crime_attributes(self):
    c = self.speeding
    self.assertEqual(c.name, "Speeding")
    self.assertEqual(c.wiki_url, "www.speeding.com")
    self.assertEqual(c.descriptions, [])
    self.assertEqual(c.celebrities, [])
    self.assertEqual(c.charges, [])

  def test_crime_in_db(self):
    c = self.speeding
    db.session.add(c)
    db.session.commit()
    self.assertEqual(Crime.query.all(), [c])


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

  def test_celebrity_in_db(self):
    c = self.ched
    db.session.add(c)
    db.session.commit()
    self.assertEqual(Celebrity.query.all(), [c])

  def test_charge_attributes(self):
    c = self.charge1
    self.assertEqual(c.date, date(2000,1,1))
    self.assertEqual(c.description, 'Driving Fast!')
    self.assertEqual(c.location, 'Austin, Texas')
    self.assertEqual(c.attorney, 'James Funk')
    self.assertEqual(c.classification, 'Class A misdemeanor')
    self.assertEqual(c.crime, self.speeding)
    self.assertEqual(c.celebrity, self.ched)

  def test_charge_in_db(self):
    c = self.charge1
    db.session.add(c)
    db.session.commit()
    self.assertEqual(Charge.query.all(), [c])

  def test_celebrity_alias_attributes(self):
    alias = CelebrityAlias("Cheese Man", self.ched)
    self.assertEqual(alias.alias, "Cheese Man")
    self.assertEqual(alias.celebrity, self.ched)

  def test_celebrity_alias_in_db(self):
    alias = CelebrityAlias("Cheese Man", self.ched)
    db.session.add(alias)
    db.session.commit()
    self.assertEqual(CelebrityAlias.query.all(), [alias])

  def test_crimedescription_attributes(self):
    desc = CrimeDescription(location='Austin', description='Driving Fast', crime=self.speeding)    
    self.assertEqual(desc.location, 'Austin')
    self.assertEqual(desc.description, 'Driving Fast')
    self.assertEqual(desc.crime, self.speeding)

  def test_crimedescription_in_db(self):
    desc = CrimeDescription(location='Austin', description='Driving Fast', crime=self.speeding)    
    db.session.add(desc)
    db.session.commit()
    self.assertEqual(CrimeDescription.query.all(), [desc])

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

  def test_celebs_crimes_no_dups(self):
    charge1 = Charge(self.ce1, self.cr1)
    charge2 = Charge(self.ce1, self.cr1)
    db.session.add_all([charge1, charge2])
    db.session.commit()
    self.assertEqual(self.ce1.crimes, [self.cr1])

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

    



  def get_json_from_url(self, url):
    str_data = self.app.get(url).get_data().decode("utf-8")
    return json.loads(str_data)


if __name__ == "__main__" :
  main()   
