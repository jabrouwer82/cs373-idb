#!flask3/bin/python

from models import *
from datetime import date

# remove all existing tables
db.drop_all()

# make new tables with (likely redefined) models
db.create_all()

# Celebrities
bob = Celebrity("Bob", "Is an actor")
chaz = Celebrity("Chaz", "Is an musician")

# Crimes
jayWalking = Crime("Jay Walking")
speeding = Crime("Speeding")

# Attorneys
lawyerFunk = Attorney("James Funk", "Funk & Associates")
lawyerChed = Attorney("Ronnie Ched", "Ched & Sons Law")

charges = [
  Charge(bob, jayWalking, lawyerFunk, date(2012, 4, 5), "Miami, Florida"),
  Charge(chaz, jayWalking, lawyerChed, date(2018, 3, 7),  "Austin, Texas"),
  Charge(chaz, speeding, lawyerFunk, date(1885, 12, 9), "Dallas, Texas")
  ]

db.session.add_all(charges) 
db.session.commit()






