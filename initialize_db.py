from datetime import date
from models import Celebrity, CelebrityAlias, Crime, CrimeDescription, Charge, db

# remove all existing tables
db.drop_all()

# make new tables with (likely redefined) models
db.create_all()

# Celebrities
annak = Celebrity('Anna Kendrick', 'Is an actoress', '@AnnaKendrick47', date(1985, 8, 9), 'https://en.wikipedia.org/wiki/Anna_Kendrick', 'http://www.imdb.com/name/nm0447695/', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Anna_Kendrick_March_22%2C_2014_%28cropped%29.jpg/640px-Anna_Kendrick_March_22%2C_2014_%28cropped%29.jpg')
chaz = Celebrity('Chaz', 'Is an musician')

celebrities = [annak, chaz]
db.session.add_all(celebrities)

# Celebrity Aliases
chaz_alias_1 = CelebrityAlias('The Cheeze', chaz)
chaz_alias_2 = CelebrityAlias('Chazster', chaz)
chaz_alias_3 = CelebrityAlias('Cazster The Cheetah', chaz)

aliases = [chaz_alias_1, chaz_alias_2, chaz_alias_3]
db.session.add_all(aliases)

# Crimes
jayWalking = Crime('Jay Walking')
speeding = Crime('Speeding')

crimes = [jayWalking, speeding]
db.session.add_all(crimes)

# Crime Descriptions
jayWalking_desc = CrimeDescription('Crossing the street wrong', jayWalking)
speeding_desc_1 = CrimeDescription('Going over 80 mph', speeding, 'Texas')
speeding_desc_2 = CrimeDescription('Going over 70 mph', speeding)

descs = [jayWalking_desc, speeding_desc_1, speeding_desc_2]
db.session.add_all(descs)

# Charges
charges = [
  Charge(annak, jayWalking, date(2012, 4, 5), 'Miami, Florida'),
  Charge(chaz, jayWalking, date(2018, 3, 7),  'Austin, Texas'),
  Charge(chaz, speeding, date(1885, 12, 9), 'Dallas, Texas')
  ]

db.session.add_all(charges) 
db.session.commit()

