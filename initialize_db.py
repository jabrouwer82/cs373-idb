from datetime import date
from models import Celebrity, CelebrityAlias, Crime, CrimeDescription, Charge, db

# remove all existing tables
db.drop_all()

# make new tables with (likely redefined) models
db.create_all()


'''
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
'''

# Celebrities
cBroadus = Celebrity(name='Calvin Cordozar Broadus Jr.', 
			  description='Musician, etc...', 
                          twitter_handle='@SnoopDogg',
			  birthday=date(1971,10,20),
                          wiki_url='http://en.wikipedia.org/wiki/Snoop_Dogg',
                          imdb_url='http://www.imdb.com/name/nm0004879/',
                          picture_url=None)

cSheen = Celebrity(name='Charley Sheen', 
			  description='Actor, etc...', 
                          twitter_handle='@CharleySheen',
			  birthday=date(1965,9,3),
                          wiki_url='http://en.wikipedia.org/wiki/Charley_Sheen',
                          imdb_url='http://www.imdb.com/name/nm0000221/',
                          picture_url=None)

rDowneyJr = Celebrity(name='Robert Downey, Jr.', 
			  description='Actor, etc...', 
                          twitter_handle='@RobertDowneyJr',
			  birthday=date(1965,4,4),
                          wiki_url='http://en.wikipedia.org/wiki/Robert_Downey_Jr',
                          imdb_url='http://www.imdb.com/name/nm0000375/',
                          picture_url=None)

mMcconaughey = Celebrity(name='Matthew McConaughey', 
			  description='Actor, etc...', 
                          twitter_handle='@McConaughey',
			  birthday=date(1969,11,4),
                          wiki_url='http://en.wikipedia.org/wiki/Matthew_McConaughey',
                          imdb_url='http://www.imdb.com/name/nm0000190/',
                          picture_url=None)

celebrities = [cBroadus, cSheen, rDowneyJr, mMcconaughey]
db.session.add_all(celebrities)

# Aliases
snoopDogg = CelebrityAlias('Snoop Dogg', cBroadus)


aliases = [snoopDogg]



# Crimes
possessionMarijuana = Crime('Possession of Marijuana', 'http://en.wikipedia.org/wiki/Drug_possession')
possessionHeroine = Crime('Possession of Heroine', 'http://en.wikipedia.org/wiki/Drug_possession')
possessionCocaine = Crime('Possession of Cocaine', 'http://en.wikipedia.org/wiki/Drug_possession')
possessionParaphernalia = Crime('Possession of Drug Paraphernalia', 'http://en.wikipedia.org/wiki/Drug_paraphernalia')
resistingArrest = Crime('Resisting Arrest', 'http://en.wikipedia.org/wiki/Resisting_arrest')
possessionFirearm = Crime('Possession of Concealed Firearm', 'http://en.wikipedia.org/wiki/Weapon_possession')

crimes = [possessionMarijuana, possessionParaphernalia, possessionHeroine, possessionCocaine, possessionFirearm, resistingArrest]


# Charges
charges = [

  Charge(mMcconaughey, possessionMarijuana, date(1999, 10, 29), 'Austin, Texas',
    description='Actor Matthew McConaughey was arrested early Monday during a disturbance at his home in which police said he was dancing naked and playing the bongo drums.',	
    attorney=None, classification=None),

  Charge(mMcconaughey, possessionParaphernalia, date(1999, 10, 29), 'Austin, Texas',
    description='Actor Matthew McConaughey was arrested early Monday during a disturbance at his home in which police said he was dancing naked and playing the bongo drums.'),

  Charge(mMcconaughey, resistingArrest, date(1999, 10, 29), 'Austin, Texas',
    description='Actor Matthew McConaughey was arrested early Monday during a disturbance at his home in which police said he was dancing naked and playing the bongo drums.',
    classification='Class A misdemeanor'),

  Charge(rDowneyJr, possessionHeroine, date(1996, 6, 23), 'Malibu, Calinfornia',
    description='On June 23 at 11:15 a.m., Malibu sheriffs pulled him over after his black 1996 Explorer was clocked going 70 mph along a 50-mph stretch of the Pacific Coast Highway. They found heroin, cocaine and crack—and the gun'),

  Charge(rDowneyJr, possessionCocaine, date(1996, 6, 23), 'Malibu, Calinfornia',
    description='On June 23 at 11:15 a.m., Malibu sheriffs pulled him over after his black 1996 Explorer was clocked going 70 mph along a 50-mph stretch of the Pacific Coast Highway. They found heroin, cocaine and crack—and the gun'),

  Charge(rDowneyJr, possessionFirearm, date(1996, 6, 23), 'Malibu, Calinfornia',
    description='On June 23 at 11:15 a.m., Malibu sheriffs pulled him over after his black 1996 Explorer was clocked going 70 mph along a 50-mph stretch of the Pacific Coast Highway. They found heroin, cocaine and crack—and the gun'),

	
]

# Add everything to the database
db.session.add_all(crimes)
db.session.add_all(celebrities)
db.session.add_all(aliases)
db.session.add_all(charges)
db.session.commit()

'''
Data to add:

Robert Downey Jr.
6-23-1996
Malibu, California
under the influence of a controlled substance

Charley Sheen
Aspen, Colorado
Felony menacing, Third-degree assault (m), criminal mischief (m)
Christmas Day incident in which he allegedly held a knife to his wife's throat in their rented Aspen home
12-25-2009
Sheen was arrested in Aspen, Colo., on charges of domestic violence, including assault and menacing, against his wife, Brooke Mueller. She reportedly told police that he had held a knife to her throat and threatened to kill her. Three months later, he was charged with felony menacing, and assault and criminal mischief, both misdemeanors. (latimes)


Snoop Dogg
10-26-2006 sale and transportation of marijuana
11-2006 felony charges of gun possession by a felon
Burbank, California
Broadus was first arrested Oct. 26 at Burbank Airport. Thompson said he had 39.14 grams of marijuana – some of it in individual canisters – at the time of this arrest. A search warrant served at his home in the Diamond Bar in November turned up a semi-automatic handgun,

'''
