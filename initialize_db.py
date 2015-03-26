from datetime import date
from models import Celebrity, CelebrityAlias, Crime, CrimeDescription, Charge, db

# remove all existing tables
db.drop_all()

# make new tables with (likely redefined) models
db.create_all()

# Celebrities
snoop = Celebrity(name='Calvin Cordozar Broadus Jr.', 
			            description='&nbsp;&nbsp;&nbsp;&nbsp;Calvin Cordozar Broadus Jr. (born October 20, 1971), best known as Snoop Dogg, is an American rapper, singer-songwriter, and actor. He has sold over 30 million albums worldwide. His music career began in 1992 when he was discovered by Dr. Dre. He collaborated on Dre\'s solo debut The Chronic (1992), and on the theme song to the feature film Deep Cover.<br />&nbsp;&nbsp;&nbsp;&nbsp;Snoop\'s debut album, Doggystyle, was released in 1993 under Death Row Records, debuting at No. 1 on both the Billboard 200 and Billboard Hot R&B/Hip-Hop Songs charts. Selling almost a million copies in the first week of its release, Doggystyle became certified 4× platinum in 1994 and spawned several hit singles, including "What\'s My Name" and "Gin & Juice". In 1994, Snoop released a soundtrack on Death Row Records for the short film Murder Was The Case, starring himself. His second album Tha Doggfather (1996), also debuted at No. 1 on both charts with "Snoop\'s Upside Ya Head" as the lead single. The album was certified double platinum in 1997.<br />&nbsp;&nbsp;&nbsp;&nbsp;After leaving Death Row, Snoop signed with No Limit Records, where he recorded his next three albums. Da Game Is to Be Sold, Not to Be Told (1998), No Limit Top Dogg (1999), and Tha Last Meal (2000). Snoop then signed with Priority/Capitol/EMI Records in 2002, where he released Paid tha Cost to Be da Boss. He then signed with Geffen Records in 2004 for his next three albums R&G (Rhythm & Gangsta): The Masterpiece, Tha Blue Carpet Treatment, and Ego Trippin\'. Malice \'n Wonderland (2009) and Doggumentary (2011), were released on Priority. Snoop Dogg has starred in motion pictures and hosted several television shows including, Doggy Fizzle Televizzle, Snoop Dogg\'s Father Hood, and Dogg After Dark. He also coaches a youth football league and high school football team. In September 2009, Snoop was hired by EMI as the chairman of a reactivated Priority Records.<br />&nbsp;&nbsp;&nbsp;&nbsp;In 2012, after a trip to Jamaica, Snoop announced a conversion to the Rastafari movement and a new alias, Snoop Lion. Under the new moniker, he released a reggae album, Reincarnated, and a documentary film of the same name, of his Jamaican experience, in early 2013. He is currently working on his last solo studio album under his rap moniker Snoop Dogg.', 
                  twitter_handle='@SnoopDogg',
			            birthday=date(1971,10,20),
                  wiki_url='http://en.wikipedia.org/wiki/Snoop_Dogg',
                  imdb_url='http://www.imdb.com/name/nm0004879/',
                  picture_url='http://www.logoi.com/picture-movies/img/snoop_dogg_03.jpg')

cSheen = Celebrity(name='Carlos Irwin Estévez', 
			             description='&nbsp;&nbsp;&nbsp;&nbsp;Carlos Irwin Estévez (born September 3, 1965), best known by his stage name Charlie Sheen, is an American actor. Sheen rose to fame after a series of successful films such as Platoon (1986), Lucas (1986), Ferris Bueller\'s Day Off (1986), Wall Street (1987), Young Guns (1988), Eight Men Out (1988), Major League (1989), Hot Shots! (1991), The Three Musketeers (1993), The Arrival (1996), Money Talks (1997), and Being John Malkovich (1999).<br />&nbsp;&nbsp;&nbsp;&nbsp;In the 2000s, Sheen became best known for his television roles. He replaced Michael J. Fox in Spin City and his performance earned him a Golden Globe Award for Best Actor – Television Series Musical or Comedy and then starred in Two and a Half Men which earned him several Golden Globe and Emmy Award nominations. He most recently starred in the FX comedy series Anger Management, which concluded its 100-episode run in 2014. In 2010, Sheen was the highest paid actor on television and earned US$1.8 million per episode of Two and a Half Men.<br />&nbsp;&nbsp;&nbsp;&nbsp;Sheen\'s personal life has made headlines, including reports of alcohol and drug abuse and marital problems, as well as allegations of domestic violence. He was fired from Two and a Half Men by CBS and Warner Bros. in March 2011. Sheen subsequently went on a nationwide tour.', 
                   twitter_handle='@CharleySheen',
			             birthday=date(1965,9,3),
                   wiki_url='http://en.wikipedia.org/wiki/Charley_Sheen',
                   imdb_url='http://www.imdb.com/name/nm0000221/',
                   picture_url='http://media.oregonlive.com/ent_impact_tvfilm/photo/charlie-sheen-mugshot-cf155afa4968314c.jpg')

rDowneyJr = Celebrity(name='Robert Downey, Jr.', 
                      description='&nbsp;&nbsp;&nbsp;&nbsp;Robert John Downey Jr. (born April 4, 1965) is an American actor, producer, and singer, whose career has included critical and popular success in his youth, followed by a period of substance abuse and legal troubles, and a resurgence of commercial success in middle age.<br />&nbsp;&nbsp;&nbsp;&nbsp;Making his screen debut at the age of five, appearing in his father Robert Downey Sr.\'s film Pound (1970), he appeared in roles associated with the Brat Pack, such as the teen sci-fi comedy Weird Science (1985) and the drama Less Than Zero (1987). Other films he has starred in include the action comedy Air America (1990), the comedy Soapdish (1991), and the crime film Natural Born Killers (1994). He starred as Charlie Chaplin, the title character in the 1992 film Chaplin, which earned him a nomination for the Academy Award for Best Actor.<br />&nbsp;&nbsp;&nbsp;&nbsp;After being released in 2000 from the California Substance Abuse Treatment Facility and State Prison where he was on drug charges, Downey joined the cast of the TV series Ally McBeal playing Calista Flockhart\'s love interest. His performance was praised and he received a Golden Globe Award for Best Performance by an Actor in a Supporting Role in a Series, Miniseries, or Television Film. His character was written out when Downey was fired after two drug arrests in late 2000 and early 2001. After one last stay in a court-ordered drug treatment program, Downey finally achieved sobriety.<br />&nbsp;&nbsp;&nbsp;&nbsp;His more recent films include the musical comedy crime film The Singing Detective (2003), the supernatural horror film Gothika (2003), the crime comedy Kiss Kiss Bang Bang (2005), the animated science fiction thriller A Scanner Darkly (2006), the mystery thriller Zodiac (2007), and the satirical action comedy Tropic Thunder (2008), for which he was nominated for an Academy Award for Best Supporting Actor. Beginning in 2008, Downey played the role of Marvel superhero Tony Stark/Iron Man in several live action films, as either the lead or part of an ensemble cast. He played the title character in Guy Ritchie\'s Sherlock Holmes (2009) and its sequel (2011).<br />&nbsp;&nbsp;&nbsp;&nbsp;Downey has starred in six movies that have each grossed over $500 million at the box office worldwide. Two of those films, The Avengers and Iron Man 3, each earned over $1 billion. Downey tops the Forbes list of Hollywood\'s highest-paid actors with an estimated $75 million in earnings between June 2012 and June 2013.', 
                      twitter_handle='@RobertDowneyJr',
			                birthday=date(1965,4,4),
                      wiki_url='http://en.wikipedia.org/wiki/Robert_Downey_Jr',
                      imdb_url='http://www.imdb.com/name/nm0000375/',
                      picture_url='http://photos.posh24.com/p/861774/z/chace_crawford/robert_downey_jr_mug_shot.jpg')

mMcconaughey = Celebrity(name='Matthew McConaughey', 
			                   description='&nbsp;&nbsp;&nbsp;&nbsp;Matthew David McConaughey (born November 4, 1969) is an American actor and producer. He first gained notice for his breakout role in the coming-of-age comedy Dazed and Confused (1993), and went on to appear in films such as the slasher Texas Chainsaw Massacre: The Next Generation (1994), the legal thriller A Time to Kill (1996), Steven Spielberg\'s historical drama Amistad (1997), the science fiction drama Contact (1997), the comedy EDtv (1999) and the war film U-571 (2000).<br />&nbsp;&nbsp;&nbsp;&nbsp;In the 2000s, he became best known for starring in romantic comedies, including The Wedding Planner (2001), How to Lose a Guy in 10 Days (2003), Failure to Launch (2006), Fool\'s Gold (2008) and Ghosts of Girlfriends Past (2009). Since 2010 he has moved away from romantic comedies and has had roles in the films The Lincoln Lawyer (2011), Bernie (2011), Killer Joe (2011), The Paperboy (2012), Mud (2012), Magic Mike (2012), The Wolf of Wall Street (2013), Dallas Buyers Club (2013), and Interstellar (2014).<br />&nbsp;&nbsp;&nbsp;&nbsp;McConaughey achieved much success in 2013 for portraying a cowboy diagnosed with AIDS in the biographical film Dallas Buyers Club, which earned him the Academy Award for Best Actor and Golden Globe Award for Best Actor – Drama, among other awards and nominations. He also starred as Rustin Cohle in the acclaimed 2014 HBO crime anthology series True Detective for which he won a Critics\' Choice Award and was nominated for a Primetime Emmy Award for Outstanding Lead Actor in a Drama Series.', 
                         twitter_handle='@McConaughey',
			                   birthday=date(1969,11,4),
                         wiki_url='http://en.wikipedia.org/wiki/Matthew_McConaughey',
                         imdb_url='http://www.imdb.com/name/nm0000190/',
                         picture_url='http://www.monkeybearreviews.com/wp-content/uploads/2009/05/matthew-mcconaughey-mug-shot.jpg')

dMX = Celebrity(name='Earl Simmons',
                description='&nbsp;&nbsp;&nbsp;&nbsp;Earl Simmons (born December 18, 1970), better known by his stage names DMX and Dark Man X, is an American rapper and actor. In 1999, DMX released his best-selling album ...And Then There Was X, which featured the hit single "Party Up (Up in Here)". He has acted in films such as Belly, Romeo Must Die, Exit Wounds, Cradle 2 The Grave, and Last Hour. In 2006, he starred in the reality television series DMX: Soul of a Man, which was primarily aired on the BET cable television network. In 2003, DMX published a book of his memoirs entitled, E.A.R.L.: The Autobiography of DMX. DMX has sold over 30 million records worldwide, making him one of the best-selling hip-hop artists of all time.',
                twitter_handle='@DMX',
                birthday=date(1970, 12, 18),
                wiki_url='http://en.wikipedia.org/wiki/DMX_%28rapper%29',
                imdb_url='http://www.imdb.com/name/nm0229422/',
                picture_url='http://upload.wikimedia.org/wikipedia/commons/a/a2/DMX_mug_shot.jpg')

mSheen = Celebrity(name='Ramón Antonio Gerardo Estévez',
                   description='&nbsp;&nbsp;&nbsp;&nbsp;Ramón Antonio Gerardo Estévez (born August 3, 1940), better known by his stage name Martin Sheen, is an American actor who first achieved fame with roles in the films Badlands (1973) and Apocalypse Now (1979).<br />&nbsp;&nbsp;&nbsp;&nbsp;Other notable films in Sheen\'s career include Gettysburg (1993), The Departed (2006), and The Amazing Spider-Man (2012). He also starred in the television series The West Wing (1999–2006) as President Josiah Bartlet.<br />&nbsp;&nbsp;&nbsp;&nbsp;In film, he has won the Best Actor award at the San Sebastián International Film Festival for his performance as Kit Carruthers in Badlands. His portrayal of Capt. Willard in Apocalypse Now earned a nomination for the BAFTA Award for Best Actor. Sheen has worked with a wide variety of film directors, such as Richard Attenborough, Francis Ford Coppola, Terrence Malick, David Cronenberg, Mike Nichols, Martin Scorsese, Steven Spielberg, and Oliver Stone. He has had a star on the Hollywood Walk of Fame since 1989. In television, he has won both a Golden Globe and two Screen Actors Guild awards for playing the role of President Josiah Bartlet in The West Wing, and an Emmy for guest starring in the sitcom Murphy Brown.<br />&nbsp;&nbsp;&nbsp;&nbsp;Born and raised in the United States from immigrant parents, he adopted the stage name Martin Sheen to help him gain acting parts. He is the father of four children (Emilio, Ramón, Carlos (Charlie Sheen), and Renée), all of whom are actors, as is his younger brother Joe Estevez.<br />&nbsp;&nbsp;&nbsp;&nbsp;Although known as an actor, Sheen also has directed one film, Cadence (1990), appearing alongside sons Charlie and Ramón. He has narrated, produced, and directed documentary television, earning two Daytime Emmy awards in the 1980s. In addition to film and television, Sheen has been active in liberal politics.',
                   twitter_handle='@csheensdad',
                   birthday=date(1940, 8, 3),
                   wiki_url='http://en.wikipedia.org/wiki/Martin_Sheen',
                   imdb_url='http://www.imdb.com/name/nm0000640',
                   picture_url='http://a.abcnews.com/images/Entertainment/ap_martin_sheen_nt_120316_wmain.jpg')

gClooney = Celebrity(name='George Clooney',
                     description='&nbsp&nbsp;&nbsp;&nbsp;George Timothy Clooney (born May 6, 1961) is an American actor, writer, producer, director, and activist. He has received three Golden Globe Awards for his work as an actor and two Academy Awards, one for acting and the other for producing.<br />&nbsp&nbsp;&nbsp;&nbsp;Clooney made his acting debut on television in 1978, and later gained wide recognition in his role as Dr. Doug Ross on the long-running medical drama ER from 1994 to 1999, for which he received two Emmy Award nominations. While working on ER, he began attracting a variety of leading roles in films, including the superhero film Batman & Robin (1997) and the crime comedy Out of Sight (1998), in which he first worked with a director who would become a long-time collaborator, Steven Soderbergh. In 1999, Clooney took the lead role in Three Kings, a well-received war satire set during the Gulf War.<br />&nbsp&nbsp;&nbsp;&nbsp;In 2001, Clooney\'s fame widened with the release of his biggest commercial success, the heist comedy Ocean\'s Eleven, the first of the film trilogy, a remake of the 1960 film with Frank Sinatra as Danny Ocean. He made his directorial debut a year later with the biographical thriller Confessions of a Dangerous Mind, and has since directed the drama Good Night, and Good Luck (2005), the sports comedy Leatherheads (2008), the political drama The Ides of March (2011), and the comedy-drama war film The Monuments Men (2014).<br />&nbsp&nbsp;&nbsp;&nbsp;He won an Academy Award for Best Supporting Actor for the Middle East thriller Syriana (2005), and subsequently earned Best Actor nominations for the legal thriller Michael Clayton (2007), the comedy-drama Up in the Air (2009) and the drama The Descendants (2011). In 2013, he received the Academy Award for Best Picture for producing the political thriller Argo, alongside Ben Affleck and Grant Heslov. He is the only person ever to be nominated for Academy Awards in six categories.<br />&nbsp&nbsp;&nbsp;&nbsp;Clooney is sometimes described as one of the most handsome men in the world. In 2005, TV Guide ranked Clooney No. 1 on its "50 Sexiest Stars of All Time" list. In 2009, he was included in Time\'s annual Time 100 as one of the "Most Influential People in the World". Clooney is also noted for his political activism and has served as one of the United Nations Messengers of Peace since January 31, 2008. His humanitarian work includes his advocacy of finding a resolution for the Darfur conflict, raising funds for the 2010 Haiti earthquake, 2004 Tsunami, and 9/11 victims, and creating documentaries such as Sand and Sorrow to raise awareness about international crises. He is also a member of the Council on Foreign Relations.',
                     twitter_handle='@clooney_clooney',
                     birthday=date(1961, 5, 6),
                     wiki_url='http://en.wikipedia.org/wiki/George_Clooney',
                     imdb_url='http://www.imdb.com/name/nm0000123/',
                     picture_url='http://static2.refinery29.com/bin/entry/5aa/x/162197/george-clooney-3-300.jpg')

rWitherspoon = Celebrity(name='Reese Witherspoon',
                         description='&nbsp&nbsp;&nbsp;&nbsp;Laura Jeanne Reese Witherspoon (born March 22, 1976) is an American actress and producer. She made her film debut as the female lead in the film The Man in the Moon in 1991. In 1996, she appeared in Freeway and starred in Pleasantville in 1998. In 2000, she earned a Golden Globe Award for Best Actress – Comedy or Musical nomination for Election.<br />&nbsp&nbsp;&nbsp;&nbsp;Witherspoon\'s breakthrough role came in 2001 with the box-office hit Legally Blonde and in 2002 she starred in the romantic comedy Sweet Home Alabama, which emerged as her biggest live-action commercial success. In 2005, Witherspoon received worldwide attention and praise for her portrayal of June Carter Cash in Walk the Line, which earned her the Academy Award, Golden Globe Award, BAFTA Award, Screen Actors Guild Award and the Critics Choice Award for Best Actress. Her other films include Legally Blonde 2: Red, White & Blonde (2003), Monsters vs. Aliens (2009) and Water for Elephants (2011). In 2014, Witherspoon produced the thriller Gone Girl and garnered praise for portraying Cheryl Strayed in Wild, for which she earned her second Best Actress nomination at the Academy Awards.<br />&nbsp&nbsp;&nbsp;&nbsp;She married actor Ryan Phillippe in 1999; the couple separated in 2006 and divorced in 2007. She married talent agent Jim Toth in 2011. Witherspoon owns a production company, Pacific Standard and she is actively involved in children\'s and women\'s advocacy organizations. She serves on the board of the Children\'s Defense Fund (CDF) and was named Global Ambassador of Avon Products in 2007, serving as honorary chair of the charitable Avon Foundation. In December 2010, Witherspoon received a star on the Hollywood Walk of Fame.',
                         twitter_handle='@reesewitherspoon',
                         birthday=date(1976, 3, 22),
                         wiki_url='http://en.wikipedia.org/wiki/Reese_Witherspoon',
                         imdb_url='http://www.imdb.com/name/nm0000702/',
                         picture_url='http://starcasm.net/wp-content/uploads/2013/04/Reese_Witherspoon_mug_shot.jpg')

fWillard = Celebrity(name='Fred WIllard',
                     description='&nbsp&nbsp;&nbsp;&nbsp;Frederic Willard (born September 18, 1939) is an American actor, comedian, voice actor, and writer, best known for his improvisational comedy. He is known for his roles in the Rob Reiner mockumentary film This Is Spinal Tap, the Christopher Guest mockumentary films Waiting for Guffman, Best in Show, A Mighty Wind, and For Your Consideration, and the Anchorman films. He is an alumnus of The Second City. He received three Emmy nominations for his recurring role on the TV series Everybody Loves Raymond as Robert Barone\'s father-in-law, Hank MacDougall. In 2010, he received an Emmy nomination for Outstanding Guest Actor in a Comedy Series for his role on the ABC TV series Modern Family as Phil Dunphy\'s father, Frank Dunphy.<br />&nbsp&nbsp;&nbsp;&nbsp;He also received a Daytime Emmy Nomination for Outstanding Talk Show Host for What\'s Hot, What\'s Not. One of his earliest jobs was at The Second City, Chicago, where he shared the stage with Robert Klein and David Steinberg. He was a founding member of the improvisational comedy group Ace Trucking Company. Fellow members of Ace included Michael Mislove and Bill Saluga. They performed sketches on The Tonight Show With Johnny Carson over 50 times and appeared regularly on This is Tom Jones.',
                     twitter_handle='@fred_willard',
                     birthday=date(1939, 11, 18),
                     wiki_url='http://en.wikipedia.org/wiki/Fred_Willard',
                     imdb_url='http://www.imdb.com/name/nm0929609/',
                     picture_url='http://thecount.com/wp-content/uploads/fred-willard-mugshot1.png')

pReubens = Celebrity(name='Paul Reubens',
                     description='&nbsp&nbsp;&nbsp;&nbsp;Paul Reubens (born Paul Rubenfeld; August 27, 1952) is an American actor, writer, film producer, game show host, and comedian, best known for his character Pee-wee Herman. Reubens joined the Los Angeles troupe The Groundlings in the 1970s and started his career as an improvisational comedian and stage actor. In 1982, Reubens put up a show about a character he had been developing for years. The show was called The Pee-wee Herman Show and it ran for five sold-out months with HBO producing a successful special about it. Pee-wee became an instant cult figure and for the next decade Reubens would be completely committed to his character, doing all of his public appearances and interviews as Pee-wee. In 1985 Pee-wee\'s Big Adventure, directed by the then-unknown Tim Burton, was a financial success and, despite receiving mixed reviews, it developed into a cult film. Big Top Pee-wee, 1988\'s sequel, was less successful than its predecessor. Between 1986 and 1990, Reubens starred as Pee-wee in the CBS Saturday-morning children\'s program Pee-wee\'s Playhouse.<br />&nbsp&nbsp;&nbsp;&nbsp;Thereafter, Reubens decided to take a sabbatical from Pee-wee. In July 1991, Reubens was arrested for indecent exposure in an adult theater in Sarasota, Florida. The arrest set off a chain reaction of national media attention that changed the general public\'s view of Reubens and Pee-wee. The arrest postponed Reubens\' involvement in major projects until 1999, when he appeared in several big-budget projects Mystery Men and Blow and started giving interviews as himself rather than as Pee-wee.<br />&nbsp&nbsp;&nbsp;&nbsp;Since 2006, Reubens has been making cameos and guest appearances in numerous projects, such as Reno 911!, 30 Rock, Dirt, Pushing Daisies, and The Blacklist. Since the 1990s, he has worked on two possible Pee-wee films — one dark and adult, dubbed The Pee-wee Herman Story, and one a family-friendly epic adventure called Pee-wee\'s Playhouse: The Movie. In 2010, he starred on Broadway in The Pee-wee Herman Show.',
                     twitter_handle='@peeweeherman',
                     birthday=date(1952, 8, 27),
                     wiki_url='http://en.wikipedia.org/wiki/Paul_Reubens',
                     imdb_url='http://www.imdb.com/name/nm0000607/',
                     picture_url='http://www.celebrityinsightsblog.com/wp-content/uploads/ReubensPaulMug.jpg')

wRyder = Celebrity(name='Winona Ryder',
                   description='&nbsp&nbsp;&nbsp;&nbsp;Winona Ryder (born Winona Laura Horowitz; October 29, 1971) is an American actress. She made her film debut in the 1986 film Lucas. As Lydia Deetz, a goth teenager in Tim Burton\'s Beetlejuice (1988), she won critical and popular recognition. After various appearances in film and on television, Ryder continued her acting career with the cult film Heathers (1988), a controversial satire of teenage suicide and high school life that drew Ryder further critical attention and commercial success. She later appeared in Mermaids (1990), earning a Golden Globe nomination, in Burton\'s Edward Scissorhands (1990), and in Francis Ford Coppola\'s gothic romance Bram Stoker\'s Dracula (1992).<br />&nbsp&nbsp;&nbsp;&nbsp;Having played diverse roles in many well-received films, Ryder won a Golden Globe Award for Best Supporting Actress and an Academy Award nomination in the same category for her role in The Age of Innocence in 1993 as well as another Academy Award nomination, as Best Actress, for Little Women the following year. She later appeared in the Generation X cult hit Reality Bites (1994), Alien: Resurrection (1997), the Woody Allen comedy Celebrity (1998), and Girl, Interrupted (1999), which she also executive-produced. In 2000, Ryder received a star on the Walk of Fame in Hollywood, California.<br />&nbsp&nbsp;&nbsp;&nbsp;Ryder\'s personal life has attracted significant media attention. Her relationship with Johnny Depp and a 2001 arrest for shoplifting were constant subjects of tabloid journalism. She has since revealed her personal struggles with anxiety and depression. In 2002, she appeared in the box office smash Mr. Deeds. In 2006, Ryder returned to the screen after a brief hiatus, later appearing in high-profile films such as Star Trek. In 2010, she was nominated for two Screen Actors Guild Awards: as the lead actress in When Love Is Not Enough: The Lois Wilson Story and as part of the cast of Black Swan. She also reunited with Burton for Frankenweenie (2012).',
                   twitter_handle='@WinonaROnline',
                   birthday=date(1971, 10, 29),
                   wiki_url='http://en.wikipedia.org/wiki/Winona_Ryder',
                   imdb_url='http://www.imdb.com/name/nm0000213/',
                   picture_url='http://cbsnews2.cbsistatic.com/hub/i/r/2012/01/05/fee18367-a643-11e2-a3f0-029118418759/resize/620x465/e51a52e855a077b839a5e6ace912b77f/winonaryder_ss2jpg.jpg')

jOsbourne = Celebrity(name='John Michael Osbourne',
                      description='&nbsp&nbsp;&nbsp;&nbsp;John Michael "Ozzy" Osbourne (born 3 December 1948) is an English vocalist, songwriter, and television personality. He rose to prominence in the early 1970s as the lead vocalist of the pioneering band Black Sabbath, whose dark and heavy sound has often been cited as key to the development of the heavy metal genre. Osbourne was fired from Black Sabbath in 1979 and has since had a successful solo career, releasing 11 studio albums, the first seven of which were all awarded multi-platinum certifications in the U.S., although he has reunited with Black Sabbath on several occasions, most recently in 2011, to record the album 13, which was released in 2013. Osbourne\'s longevity and success have earned him the informal title of "Godfather of Heavy Metal".<br />&nbsp&nbsp;&nbsp;&nbsp;Osbourne\'s total album sales from his years in Black Sabbath, combined with his solo work, is over 100 million. As a member of Black Sabbath, he was inducted into the U.S. Rock and Roll Hall of Fame, and he was inducted into the UK Music Hall of Fame as a solo artist and as a member of the band. Osbourne has a star on the Birmingham Walk of Stars in his hometown as well as the Hollywood Walk of Fame. At the 2014 MTV Europe Music Awards he received the Global Icon Award. In the early 2000s, he became a TV star, appearing as himself in the MTV reality program The Osbournes, alongside wife/manager Sharon and two of their three children, Kelly and Jack.',
                      twitter_handle='@OzzyOsbourne',
                      birthday=date(1948, 12, 3),
                      wiki_url='http://en.wikipedia.org/wiki/Ozzy_Osbourne',
                      imdb_url='http://www.imdb.com/name/nm0005285/',
                      picture_url='http://www.thesmokinggun.com/sites/default/files/imagecache/670xX/photos/Ozzymug.jpg')

celebrities = [snoop, cSheen, rDowneyJr, mMcconaughey, mSheen, dMX, gClooney, fWillard, pReubens, wRyder, jOsbourne]
db.session.add_all(celebrities)

# Aliases


aliases = [
    CelebrityAlias('Snoop Dogg', snoop),
    CelebrityAlias('Charlie Sheen', cSheen),
    CelebrityAlias('Martin Sheen', mSheen),
    CelebrityAlias('DMX', dMX),
    CelebrityAlias('Dark Man X', dMX),
    CelebrityAlias('Pee Wee Herman', pReubens),
    CelebrityAlias('Ozzy Osbourne', jOsbourne),
    CelebrityAlias('RDJ', rDowneyJr)
  ]


#Crimes
possessionMarijuana = Crime('Possession of Marijuana', 'http://en.wikipedia.org/wiki/Drug_possession')
possessionHeroine = Crime('Possession of Heroine', 'http://en.wikipedia.org/wiki/Drug_possession')
possessionCocaine = Crime('Possession of Cocaine', 'http://en.wikipedia.org/wiki/Drug_possession')
possessionParaphernalia = Crime('Possession of Drug Paraphernalia', 'http://en.wikipedia.org/wiki/Drug_paraphernalia')
resistingArrest = Crime('Resisting Arrest', 'http://en.wikipedia.org/wiki/Resisting_arrest')
possessionFirearm = Crime('Possession of Concealed Firearm', 'http://en.wikipedia.org/wiki/Weapon_possession')
underInfContSubstance = Crime('Under the Influence of a Controlled Substance', 'http://en.wikipedia.org/wiki/Altered_state_of_consciousness')
menacing = Crime('Menacing', 'http://en.wikipedia.org/wiki/Menacing')
thirdAssault = Crime('Third Degree Assault', 'http://en.wikipedia.org/wiki/Assault')
mischief = Crime('Criminal Mischief', 'http://en.wikipedia.org/wiki/Mischief')
possessionGunFelon = Crime('Possession of a Gun by a Felon', 'http://en.wikipedia.org/wiki/Felon_in_possession_of_a_firearm')
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
http://en.wikipedia.org/wiki/DMX_%28rapper%29
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
http://en.wikipedia.org/wiki/Martin_Sheen
http://www.imdb.com/name/nm0000640
@csheensdad
8-3-1940
4-1-2007 Sheen was arrested, with 38 other activists, for trespassing at the Nevada Test Site at a Nevada Desert Experience event protesting against the site
5-16-1990 Actor Martin Sheen and three others were arrested Wednesday morning after they splashed what appeared to be blood on the front of the downtown Federal Building in the latest of a series of demonstrations there to protest U.S. policies in El Salvador.
8-12-2000 Martin was one of 22 people arrested for crossing over a line established by the Air Force in an anti-militarization protest at California's Vandenberg Air Force base. He was charged with trespassing.


George Clooney
Actor, ... etc
@clooney_clooney
http://en.wikipedia.org/wiki/George_Clooney
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
