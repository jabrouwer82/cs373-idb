from datetime import date
from models import Celebrity, CelebrityAlias, Crime, CrimeDescription, Charge, db

# remove all existing tables
db.drop_all()

# make new tables with (likely redefined) models
db.create_all()

# Celebrities
snoop = Celebrity(name='Calvin Cordozar Broadus Jr.', 
			            description='Musician, etc...', 
                  twitter_handle='@SnoopDogg',
			            birthday=date(1971,10,20),
                  wiki_url='http://en.wikipedia.org/wiki/Snoop_Dogg',
                  imdb_url='http://www.imdb.com/name/nm0004879/',
                  picture_url=None)

cSheen = Celebrity(name='Carlos Irwin Estévez', 
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

celebrities = [snoop, cSheen, rDowneyJr, mMcconaughey]
db.session.add_all(celebrities)

# Aliases


aliases = [
    CelebrityAlias('Snoop Dogg', snoop),
    CelebrityAlias('Charlie Sheen', cSheen)
  ]


#Crimes
possessionMarijuana = Crime('Possession of Marijuana', 'http://en.wikipedia.org/wiki/Drug_possession')
possessionHeroine = Crime('Possession of Heroine', 'http://en.wikipedia.org/wiki/Drug_possession')
possessionCocaine = Crime('Possession of Cocaine', 'http://en.wikipedia.org/wiki/Drug_possession')
possessionParaphernalia = Crime('Possession of Drug Paraphernalia', 'http://en.wikipedia.org/wiki/Drug_paraphernalia')
resistingArrest = Crime('Resisting Arrest', 'http://en.wikipedia.org/wiki/Resisting_arrest')
possessionFirearm = Crime('Possession of Concealed Firearm', 'http://en.wikipedia.org/wiki/Weapon_possession')
underInfContSubstance = Crime('Under the Influence of a Controlled Substance', 'https://en.wikipedia.org/wiki/Altered_state_of_consciousness')
menacing = Crime('Menacing', 'https://en.wikipedia.org/wiki/Menacing')
thirdAssault = Crime('Third Degree Assault', 'https://en.wikipedia.org/wiki/Assault')
mischief = Crime('Criminal Mischief', 'https://en.wikipedia.org/wiki/Mischief')
possessionGunFelon = Crime('Possession of a Gun by a Felon', 'https://en.wikipedia.org/wiki/Felon_in_possession_of_a_firearm')
saleTransportMarijuana = Crime('Sale and Transport of Marijuana', 'sales and transport of marijuana')

crimes = [possessionMarijuana, possessionParaphernalia, possessionHeroine, possessionCocaine, possessionFirearm, resistingArrest, underInfContSubstance, thirdAssault, mischief, possessionGunFelon, saleTransportMarijuana]


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

  Charge(rDowneyJr, underInfContSubstance, date(1996, 6, 23), 'Malibu, Calinfornia',
    description='On June 23 at 11:15 a.m., Malibu sheriffs pulled him over after his black 1996 Explorer was clocked going 70 mph along a 50-mph stretch of the Pacific Coast Highway. They found heroin, cocaine and crack—and the gun'),

  Charge(cSheen, menacing, date(2009, 12, 25), 'Aspen, Colorado',
    description='Sheen was arrested in Aspen, Colo., on charges of domestic violence, including assault and menacing, against his wife, Brooke Mueller. She reportedly told police that he had held a knife to her throat and threatened to kill her. Three months later, he was charged with felony menacing, and assault and criminal mischief, both misdemeanors. (latimes)', classification='Felony'),

  Charge(cSheen, thirdAssault, date(2009, 12, 25), 'Aspen, Colorado',
    description='Sheen was arrested in Aspen, Colo., on charges of domestic violence, including assault and menacing, against his wife, Brooke Mueller. She reportedly told police that he had held a knife to her throat and threatened to kill her. Three months later, he was charged with felony menacing, and assault and criminal mischief, both misdemeanors. (latimes)', classification='Misdemeanor'),

  Charge(cSheen, mischief, date(2009, 12, 25), 'Aspen, Colorado',
    description='Sheen was arrested in Aspen, Colo., on charges of domestic violence, including assault and menacing, against his wife, Brooke Mueller. She reportedly told police that he had held a knife to her throat and threatened to kill her. Three months later, he was charged with felony menacing, and assault and criminal mischief, both misdemeanors. (latimes)', classification='Misdemeanor'),

  Charge(snoop, saleTransportMarijuana, date(2006, 10, 26), 'Burbank California',
    description='Broadus was first arrested Oct. 26 at Burbank Airport. Thompson said he had 39.14 grams of marijuana – some of it in individual canisters – at the time of this arrest. A search warrant served at his home in the Diamond Bar in November turned up a semi-automatic handgun', classification='Felony'),

  Charge(snoop, possessionGunFelon, date(2006, 11, 1), 'Burbank, California',
    description='Broadus was first arrested Oct. 26 at Burbank Airport. Thompson said he had 39.14 grams of marijuana – some of it in individual canisters – at the time of this arrest. A search warrant served at his home in the Diamond Bar in November turned up a semi-automatic handgun', classification='Felony')
]

# Add everything to the database
db.session.add_all(crimes)
db.session.add_all(celebrities)
db.session.add_all(aliases)
db.session.add_all(charges)
db.session.commit()

'''
Data to add:

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

Reese Witherspoon
4-19-2013 he and husband Jim Toth had been arrested in a DUI incident

Paul Reubens (Pee Wee Herman)
7-12-1991 Indecent exposure, masturbating in an adult theater. Nearly two decades later, Reubens claimed he was innocent in a Playboy interview: "I'm right-handed, and the police report said I was jerking off with my left hand. That would have been the end of the case right there, proof it couldn't have been me."

Fred Willard
7-18-2012 Lewd conduct, the then-72-year-old actor was handcuffed after he was caught with his pants down at a Hollywood porn theater. "It was embarrassing. Embrassing as hell," the "American Pie" actor told Jimmy Kimmel. "It's the last time I'm going to listen to my wife when she says, 'Why don't you go out to see a movie?'"

Winona Ryder
12-12-2001 Ryder was caught shoplifting almost $5,000 worth of merchandise from a Saks Fifth Avenue in Beverly Hills. Ryder remains notoriously tight-lipped about the incident, but did tell Vogue in 2007 that she didn't feel all that bad about it. "I didn't have this tremendous sense of guilt, because I hadn't hurt anyone," she said 

Ozzy Osbourne
2-19-1982  Public urination, intoxication Osbourne was arrested for urinating on a statue honoring the Alamo defenders in San Antonio, Texas. To make things weirder, he was wearing his wife’s dress at the time of his arrest. The arrest got him banned from the city for 10 years, and he was eventually pardoned after making a $10,000 donation to the organization that maintains the Alamo.
'''
