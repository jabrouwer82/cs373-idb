from unittest import TestCase, main
from models import db, Celebrity, Crime, Charge, CelebrityAlias, CrimeDescription
from datetime import date
from app import app

class TestModels(TestCase):

  def setUp(self):
    app.config['TESTING'] = True

    # Not sure this is legal, as already set in app.py
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2:///testsdb'
    #app.config['WTF_CSRF_ENABLED'] = False
    #self.app = app.test_client()
    db.create_all()


    self.ched = Celebrity(name='Ched', description='Actor', twitter_handle='@Ched', 
                  birthday=date(1900,1,1), wiki_url='ched.wiki', imdb_url='ched.imdb', picture_url='ched.picture')
  
    self.speeding = Crime("Speeding", "www.speeding.com")


    self.charge1 = Charge(date=date(2000,1,1), location='Austin, Texas', 
              description='Driving Fast!', attorney='James Funk',
              classification='Class A misdemeanor', 
              crime = self.speeding, 
              celebrity = self.ched)




  def tearDown(self):
    db.session.remove()
    db.drop_all()


  def test_crime_alone(self):
    c = self.speeding

    # Test object
    self.assertEqual(c.name, "Speeding")
    self.assertEqual(c.wiki_url, "www.speeding.com")
    self.assertEqual(c.descriptions, [])
    self.assertEqual(c.celebrities, [])
    self.assertEqual(c.charges, [])

    # Test db access 
    db.session.add(c)
    db.session.commit()
    self.assertEqual(Crime.query.all(), [c])


  def test_celebrity_alone(self):
    c = self.ched

    # Test object
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

    # Test db access 
    db.session.add(c)
    db.session.commit()
    self.assertEqual(Celebrity.query.all(), [c])

  def test_charge_alone(self):
    c = self.charge1

    self.assertEqual(c.date, date(2000,1,1))
    self.assertEqual(c.description, 'Driving Fast!')
    self.assertEqual(c.location, 'Austin, Texas')
    self.assertEqual(c.attorney, 'James Funk')
    self.assertEqual(c.classification, 'Class A misdemeanor')
    self.assertEqual(c.crime, self.speeding)
    self.assertEqual(c.celebrity, self.ched)

    # Test db access 
    db.session.add(c)
    db.session.commit()
    self.assertEqual(Charge.query.all(), [c])





  def test_celebrity_alias_alone(self):
    alias = CelebrityAlias("Cheese Man", self.ched)

    # Test object
    self.assertEqual(alias.alias, "Cheese Man")
    self.assertEqual(alias.celebrity, self.ched)

    # Test db access 
    db.session.add(alias)
    db.session.commit()
    self.assertEqual(CelebrityAlias.query.all(), [alias])


  

 


if __name__ == "__main__" :
    main()   
