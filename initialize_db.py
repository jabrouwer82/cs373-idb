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

Earl Simmons (DMX, Dark Man X)
Rapper, ...etc
https://en.wikipedia.org/wiki/DMX_%28rapper%29
http://www.imdb.com/name/nm0229422/
@DMX
12-18-1970
7-2-199 When officers of the Fort Lee Police Department executed a search of his home in 1999, DMX promptly surrendered himself on weapons possession charges
5-5-2000 DMX served a 15-day jail sentence in 2000 for possession of marijuana.
5-22-2000 DMX served another jail sentence in 2001 for driving without a license and possession of marijuana. His appeal to reduce the sentence was denied; rather, he was charged with assault for throwing objects at prison guards. DMX entered rehab to treat his addiction to drugs in 2002
6-26-2004 DMX was arrested in June 2004, at the John F. Kennedy International Airport, on charges of cocaine possession, criminal impersonation, criminal possession of a weapon, criminal mischief, menacing, and driving under the influence of drugs or alcohol, while claiming to be a federal agent and attempting to carjack a vehicle. He was given a conditional discharge on December 8, 2004, but pled guilty on October 25, 2005, to violating parole.
11-18-2005 DMX was sentenced to 70 days in jail on November 18, 2005, for violating parole; the lateness charge added a 10-day extension to the original 60-day sentence. DMX was released early (for "good behavior") on December 30, 2005.
12-30-2008 DMX pled guilty to charges of drug possession, theft, and animal cruelty, at a hearing on December 30, 2008; he was sentenced to ninety days in jail on January 31, 2009.
5-22-2009 On May 22, 2009, DMX entered a plea agreement/change of plea, and pled guilty to attempted aggravated assault.
7-27-2010 On July 27, 2010, DMX turned himself in to Los Angeles Metropolitan Court for a reckless driving charge he received in 2002. He was sentenced to serve ninety days in jail
11-19-2010 DMX was arrested in Maricopa County, Arizona on November 19, 2010, on charges of violating his probation by consuming alcohol (at a performance). On December 20, 2010, DMX was moved to the Mental Health Unit of the Arizona State Prison, and released on July 18, 2011.
8-24-2011 DMX was arrested on August 24, 2011, for speeding (recorded as 102 mph in a 65 mph zone), reckless driving, and driving with a suspended license. While DMX admitted to speeding, he claims he was driving 85 mph, not 102 mph as charged
2-13-2013 DMX was arrested on February 13, 2013 in Spartanburg, South Carolina for driving without a drivers license
7-26-2013 He was arrested again on July 26, 2013 in Greenville County, South Carolina and charged with driving under the influence of alcohol, as well as driving without a license.
8-20-2013 DMX was arrested on August 20, 2013 in Greer, South Carolina during a traffic stop after a car he was a passenger in made an improper u-turn. He was arrested due to an outstanding warrant for driving under suspension. Four packages of marijuana were also found in the vehicle, and he along with the driver were cited for them
11-4-2013 DMX was again arrested on November 4, 2013 by the Greenville-Spartanburg International Airport police near Greer, South Carolina after police, who were familiar with his prior arrests, noticed DMX behind the wheel of a vehicle at the terminal. DMX was booked on charges of driving under suspension, having an uninsured vehicle, and not having a licensed vehicle. He was subsequently released after spending three hours in jail

Ramón Antonio Gerardo Estévez (Martin Sheen)
Actor, activist, ... etc
https://en.wikipedia.org/wiki/Martin_Sheen
http://www.imdb.com/name/nm0000640
@csheensdad
8-3-1940
4-1-2007 Sheen was arrested, with 38 other activists, for trespassing at the Nevada Test Site at a Nevada Desert Experience event protesting against the site
5-16-1990 Actor Martin Sheen and three others were arrested Wednesday morning after they splashed what appeared to be blood on the front of the downtown Federal Building in the latest of a series of demonstrations there to protest U.S. policies in El Salvador.
8-12-2000 Martin was one of 22 people arrested for crossing over a line established by the Air Force in an anti-militarization protest at California's Vandenberg Air Force base. He was charged with trespassing.


George Clooney
Actor, ... etc
@clooney_clooney
https://en.wikipedia.org/wiki/George_Clooney
http://www.imdb.com/name/nm0000123/
5-6-1961
3-16-2012 Clooney was arrested Friday for civil disobedience after taking part in a protest outside of the Sudanese embassy in Washington, D.C.

'''
