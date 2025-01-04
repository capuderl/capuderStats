
def spotifyArtistDemo(breakOutOnMyOwn):
    #Artist demographics
    #breakOutOnMyOwn - for discovery methds, do I want to have it borken down by deatail (can be overwhelming) or just say "On My Own"

    demo = dict()

    genreNames = ['Indie', 'Pre-2000', 'Emo', 'Pop', 'Musical', 'Hip Hop', 'R and B'];
    INDIE = 0
    OLD = 1
    EMO = 2
    POP = 3
    MUSICAL = 4
    HIPHOP = 5
    R_AND_B = 6
    
    #Where is the artist from?  "British" used to be a boollean
    countryNames = ['USA', 'England', 'Canada', 'Sweden', 'Australia', 'Netherlands', 'Mongolia', 'Germany', 'Russia', 'France', 'NewZealand', 'China', 'Norway', 'Romania', 'Spain', 'Venezuela', 'Ireland', 'Belgium', 'Other']
    USA = 0
    ENGLAND = 1
    CANADA = 2 
    SWEDEN = 3
    AUSTRALIA = 4
    NETHERLANDS = 5
    MONGOLIA = 6
    GERMANY = 7
    RUSSIA = 8
    FRANCE = 9
    NEW_ZEALAND = 10
    CHINA = 11
    NORWAY = 12
    ROMANIA = 13
    SPAIN = 14
    VENEZUELA = 15
    IRELAND = 16
    BELGIUM = 17
    COUNTRY_OTHER = 18
    assert countryNames[-1] == 'Other', 'Functions down the line assume that Other is last'

    if breakOutOnMyOwn:
        discoveryMethodNames = ['Brian', 'Teenage/College', 'Kimi', 'Concert', 'Media', 'Musical', 'Hip Hop Awakening', 'Emo Awakening', 'Music League', 'On my own - other'];
        # ON_MY_OWN = 4;
        ON_MY_OWN_CONCERT = 3; #, 'On my own - from concert',
        ON_MY_OWN_TV = 4; #'On my own - seen on TV',
        ON_MY_OWN_MUSICAL = 5; #'On my own - musical',
        ON_MY_OWN_HIP_HOP = 6; #'On my own - hip hop awakening',
        ON_MY_OWN_EMO = 7; #'On my own - emo awakening',
        MUSIC_LEAGUE = 8;
        ON_MY_OWN_OTHER = 9; #'On my own - other'
    else:
        discoveryMethodNames = ['Brian', 'Teenage/College', 'Kimi', 'On my own'];
        ON_MY_OWN = 3;
        ON_MY_OWN_CONCERT = ON_MY_OWN; #, 'On my own - from concert',
        ON_MY_OWN_HIP_HOP = ON_MY_OWN; #'On my own - hip hop awakening',
        ON_MY_OWN_EMO = ON_MY_OWN; #'On my own - emo awakening',
        ON_MY_OWN_TV = ON_MY_OWN; #'On my own - seen on TV',
        ON_MY_OWN_MUSICAL = ON_MY_OWN; #'On my own - musical',
        ON_MY_OWN_OTHER = ON_MY_OWN; #'On my own - other'
        MUSIC_LEAGUE = ON_MY_OWN;

    BRIAN = 0
    OLD_DAYS = 1
    KIMI = 2

    # demo[''] = dict()
    # demo['']['Male'] = True;
    # demo['']['POC'] = False;
    # demo['']['country'] = USA;
    # demo['']['genre'] = INDIE;
    # demo['']['discovery'] = BRIAN;
    # demo['']['Seen_Live'] = False;
    # demo['']['Kimi'] = True;  #shared custody

    demo['Alcazar'] = dict()
    demo['Alcazar']['Male'] = True;
    demo['Alcazar']['POC'] = False;
    demo['Alcazar']['country'] = SWEDEN;
    demo['Alcazar']['genre'] = POP;
    demo['Alcazar']['discovery'] = ON_MY_OWN_OTHER;
    demo['Alcazar']['Seen_Live'] = False;
    demo['Alcazar']['Kimi'] = False;

    demo['All_Get_Out'] = dict()
    demo['All_Get_Out']['Male'] = True;
    demo['All_Get_Out']['POC'] = False;
    demo['All_Get_Out']['country'] = USA;
    demo['All_Get_Out']['genre'] = EMO;
    demo['All_Get_Out']['discovery'] = ON_MY_OWN_CONCERT;
    demo['All_Get_Out']['Seen_Live'] = True;
    demo['All_Get_Out']['Kimi'] = False;

    demo['Arctic_Monkeys'] = dict()
    demo['Arctic_Monkeys']['Male'] = True;
    demo['Arctic_Monkeys']['POC'] = False;
    demo['Arctic_Monkeys']['country'] = ENGLAND;
    demo['Arctic_Monkeys']['genre'] = INDIE;
    demo['Arctic_Monkeys']['discovery'] = OLD_DAYS;
    demo['Arctic_Monkeys']['Seen_Live'] = True;
    demo['Arctic_Monkeys']['Kimi'] = False;

    demo['Astronauts_Etc'] = dict()
    demo['Astronauts_Etc']['Male'] = True; 
    demo['Astronauts_Etc']['POC'] = False;
    demo['Astronauts_Etc']['country'] = USA;
    demo['Astronauts_Etc']['genre'] = INDIE;
    demo['Astronauts_Etc']['discovery'] = BRIAN;
    demo['Astronauts_Etc']['Seen_Live'] = False;
    demo['Astronauts_Etc']['Kimi'] = False;

    demo['Barenaked_Ladies'] = dict()
    demo['Barenaked_Ladies']['Male'] = True; 
    demo['Barenaked_Ladies']['POC'] = False;
    demo['Barenaked_Ladies']['country'] = CANADA;
    demo['Barenaked_Ladies']['genre'] = INDIE; #not sure what to p[ut, using default lol
    demo['Barenaked_Ladies']['discovery'] = OLD_DAYS;
    demo['Barenaked_Ladies']['Seen_Live'] = True;
    demo['Barenaked_Ladies']['Kimi'] = False;

    demo['Bartees_Strange'] = dict()
    demo['Bartees_Strange']['Male'] = True; 
    demo['Bartees_Strange']['POC'] = True;
    demo['Bartees_Strange']['country'] = USA;
    demo['Bartees_Strange']['genre'] = INDIE;
    demo['Bartees_Strange']['discovery'] = BRIAN;
    demo['Bartees_Strange']['Seen_Live'] = False;
    demo['Bartees_Strange']['Kimi'] = False;

    demo['Big_Black_Delta'] = dict()
    demo['Big_Black_Delta']['Male'] = True; 
    demo['Big_Black_Delta']['POC'] = False;
    demo['Big_Black_Delta']['country'] = USA;
    demo['Big_Black_Delta']['genre'] = INDIE;
    demo['Big_Black_Delta']['discovery'] = BRIAN;  #Mr Dillon...doesn't seem like it's worth it's own category ha ha
    demo['Big_Black_Delta']['Seen_Live'] = False;
    demo['Big_Black_Delta']['Kimi'] = False;

    demo['Bo_Burnham'] = dict()
    demo['Bo_Burnham']['Male'] = True; 
    demo['Bo_Burnham']['POC'] = False;
    demo['Bo_Burnham']['country'] = USA;
    demo['Bo_Burnham']['genre'] = MUSICAL;
    demo['Bo_Burnham']['discovery'] = ON_MY_OWN_MUSICAL;
    demo['Bo_Burnham']['Seen_Live'] = True;
    demo['Bo_Burnham']['Kimi'] = False;

    demo['Bon_Iver'] = dict()
    demo['Bon_Iver']['Male'] = True; 
    demo['Bon_Iver']['POC'] = False;
    demo['Bon_Iver']['country'] = USA;
    demo['Bon_Iver']['genre'] = INDIE;
    demo['Bon_Iver']['discovery'] = OLD_DAYS;
    demo['Bon_Iver']['Seen_Live'] = False;
    demo['Bon_Iver']['Kimi'] = False;

    demo['Bruno_Mars'] = dict()
    demo['Bruno_Mars']['Male'] = True; 
    demo['Bruno_Mars']['POC'] = True;
    demo['Bruno_Mars']['country'] = USA;
    demo['Bruno_Mars']['genre'] = POP;
    demo['Bruno_Mars']['discovery'] = ON_MY_OWN_HIP_HOP;
    demo['Bruno_Mars']['Seen_Live'] = False;
    demo['Bruno_Mars']['Kimi'] = False;

    demo['CHVRCHES'] = dict()
    demo['CHVRCHES']['Male'] = False; 
    demo['CHVRCHES']['POC'] = False;
    demo['CHVRCHES']['country'] = ENGLAND;
    demo['CHVRCHES']['genre'] = INDIE;
    demo['CHVRCHES']['discovery'] = BRIAN;
    demo['CHVRCHES']['Seen_Live'] = True;
    demo['CHVRCHES']['Kimi'] = False;

    demo['Caroline_Polachek'] = dict()
    demo['Caroline_Polachek']['Male'] = False; 
    demo['Caroline_Polachek']['POC'] = False;
    demo['Caroline_Polachek']['country'] = USA;
    demo['Caroline_Polachek']['genre'] = INDIE;
    demo['Caroline_Polachek']['discovery'] = BRIAN;
    demo['Caroline_Polachek']['Seen_Live'] = True;
    demo['Caroline_Polachek']['Kimi'] = True;

    demo['Charli_XCX'] = dict()
    demo['Charli_XCX']['Male'] = False; 
    demo['Charli_XCX']['POC'] = False;
    demo['Charli_XCX']['country'] = ENGLAND;
    demo['Charli_XCX']['genre'] = POP;
    demo['Charli_XCX']['discovery'] = BRIAN;
    demo['Charli_XCX']['Seen_Live'] = True;
    demo['Charli_XCX']['Kimi'] = True;

    demo['Charlotte_Sands'] = dict()
    demo['Charlotte_Sands']['Male'] = False; 
    demo['Charlotte_Sands']['POC'] = False;
    demo['Charlotte_Sands']['country'] = USA;
    demo['Charlotte_Sands']['genre'] = EMO;
    demo['Charlotte_Sands']['discovery'] = ON_MY_OWN_CONCERT;
    demo['Charlotte_Sands']['Seen_Live'] = True;
    demo['Charlotte_Sands']['Kimi'] = True;

    demo['Cheap_Girls'] = dict()
    demo['Cheap_Girls']['Male'] = True; 
    demo['Cheap_Girls']['POC'] = False;
    demo['Cheap_Girls']['country'] = USA;
    demo['Cheap_Girls']['genre'] = EMO;
    demo['Cheap_Girls']['discovery'] = ON_MY_OWN_OTHER;
    demo['Cheap_Girls']['Seen_Live'] = True;
    demo['Cheap_Girls']['Kimi'] = False;

    demo['Childish_Gambino'] = dict()
    demo['Childish_Gambino']['Male'] = True; 
    demo['Childish_Gambino']['POC'] = True;
    demo['Childish_Gambino']['country'] = USA;
    demo['Childish_Gambino']['genre'] = HIPHOP;
    demo['Childish_Gambino']['discovery'] = ON_MY_OWN_HIP_HOP;
    demo['Childish_Gambino']['Seen_Live'] = True;
    demo['Childish_Gambino']['Kimi'] = True;

    demo['Coin'] = dict()
    demo['Coin']['Male'] = True; 
    demo['Coin']['POC'] = False;
    demo['Coin']['country'] = USA;
    demo['Coin']['genre'] = POP;
    demo['Coin']['discovery'] = ON_MY_OWN_CONCERT;
    demo['Coin']['Seen_Live'] = True;
    demo['Coin']['Kimi'] = False;

    demo['Dance_Gavin_Dance'] = dict()
    demo['Dance_Gavin_Dance']['Male'] = True; 
    demo['Dance_Gavin_Dance']['POC'] = False;
    demo['Dance_Gavin_Dance']['country'] = USA;
    demo['Dance_Gavin_Dance']['genre'] = EMO;
    demo['Dance_Gavin_Dance']['discovery'] = KIMI;
    demo['Dance_Gavin_Dance']['Seen_Live'] = False;
    demo['Dance_Gavin_Dance']['Kimi'] = True;

    demo['Dear_Evan_Hansen'] = dict()
    demo['Dear_Evan_Hansen']['Male'] = True; 
    demo['Dear_Evan_Hansen']['POC'] = False;
    demo['Dear_Evan_Hansen']['country'] = USA;
    demo['Dear_Evan_Hansen']['genre'] = MUSICAL;
    demo['Dear_Evan_Hansen']['discovery'] = ON_MY_OWN_MUSICAL;
    demo['Dear_Evan_Hansen']['Seen_Live'] = False;
    demo['Dear_Evan_Hansen']['Kimi'] = False;

    demo['Deftones'] = dict()
    demo['Deftones']['Male'] = True; 
    demo['Deftones']['POC'] = False;
    demo['Deftones']['country'] = USA;
    demo['Deftones']['genre'] = EMO;
    demo['Deftones']['discovery'] = ON_MY_OWN_OTHER;
    demo['Deftones']['Seen_Live'] = False;
    demo['Deftones']['Kimi'] = False;

    demo['Diamond_Rings'] = dict()
    demo['Diamond_Rings']['Male'] = True; 
    demo['Diamond_Rings']['POC'] = False;
    demo['Diamond_Rings']['country'] = USA;
    demo['Diamond_Rings']['genre'] = INDIE;
    demo['Diamond_Rings']['discovery'] = BRIAN;
    demo['Diamond_Rings']['Seen_Live'] = False;
    demo['Diamond_Rings']['Kimi'] = False;

    demo['Editors'] = dict()
    demo['Editors']['Male'] = True; 
    demo['Editors']['POC'] = False;
    demo['Editors']['country'] = ENGLAND;
    demo['Editors']['genre'] = INDIE;
    demo['Editors']['discovery'] = OLD_DAYS;
    demo['Editors']['Seen_Live'] = False;
    demo['Editors']['Kimi'] = False;

    demo['El_Vy'] = dict()
    demo['El_Vy']['Male'] = True; 
    demo['El_Vy']['POC'] = False;
    demo['El_Vy']['country'] = USA;
    demo['El_Vy']['genre'] = INDIE;
    demo['El_Vy']['discovery'] = OLD_DAYS;
    demo['El_Vy']['Seen_Live'] = True;
    demo['El_Vy']['Kimi'] = False;

    demo['Evanescence'] = dict()
    demo['Evanescence']['Male'] = False; 
    demo['Evanescence']['POC'] = False;
    demo['Evanescence']['country'] = USA;
    demo['Evanescence']['genre'] = EMO;
    demo['Evanescence']['discovery'] = OLD_DAYS;
    demo['Evanescence']['Seen_Live'] = False;
    demo['Evanescence']['Kimi'] = False;

    demo['Everything_Everything'] = dict()
    demo['Everything_Everything']['Male'] = True; 
    demo['Everything_Everything']['POC'] = False;
    demo['Everything_Everything']['country'] = ENGLAND;
    demo['Everything_Everything']['genre'] = INDIE;
    demo['Everything_Everything']['discovery'] = BRIAN;
    demo['Everything_Everything']['Seen_Live'] = True;
    demo['Everything_Everything']['Kimi'] = True;

    demo['Fleetwood_Mac'] = dict()
    demo['Fleetwood_Mac']['Male'] = True; 
    demo['Fleetwood_Mac']['POC'] = False;
    demo['Fleetwood_Mac']['country'] = USA;
    demo['Fleetwood_Mac']['genre'] = OLD;
    demo['Fleetwood_Mac']['discovery'] = ON_MY_OWN_TV;
    demo['Fleetwood_Mac']['Seen_Live'] = False;
    demo['Fleetwood_Mac']['Kimi'] = False;

    demo['Foals'] = dict()
    demo['Foals']['Male'] = True; 
    demo['Foals']['POC'] = False;
    demo['Foals']['country'] = ENGLAND;
    demo['Foals']['genre'] = INDIE;
    demo['Foals']['discovery'] = OLD_DAYS;
    demo['Foals']['Seen_Live'] = True; #warning('Change when you see Foals')
    demo['Foals']['Kimi'] = False;

    demo['Future'] = dict()
    demo['Future']['Male'] = True; 
    demo['Future']['POC'] = True;
    demo['Future']['country'] = USA;
    demo['Future']['genre'] = HIPHOP;
    demo['Future']['discovery'] = ON_MY_OWN_HIP_HOP;
    demo['Future']['Seen_Live'] = False;
    demo['Future']['Kimi'] = True;

    demo['Future_Islands'] = dict()
    demo['Future_Islands']['Male'] = True; 
    demo['Future_Islands']['POC'] = False;
    demo['Future_Islands']['country'] = USA;
    demo['Future_Islands']['genre'] = INDIE;
    demo['Future_Islands']['discovery'] = BRIAN;
    demo['Future_Islands']['Seen_Live'] = True;
    demo['Future_Islands']['Kimi'] = True;

    demo['George_Michael'] = dict()
    demo['George_Michael']['Male'] = True; 
    demo['George_Michael']['POC'] = False;
    demo['George_Michael']['country'] = USA;
    demo['George_Michael']['genre'] = OLD;
    demo['George_Michael']['discovery'] = ON_MY_OWN_TV;
    demo['George_Michael']['Seen_Live'] = False;
    demo['George_Michael']['Kimi'] = True;

    demo['Haiku_Hands'] = dict()
    demo['Haiku_Hands']['Male'] = False; 
    demo['Haiku_Hands']['POC'] = False;
    demo['Haiku_Hands']['country'] = AUSTRALIA; #I'm counting Australia as British
    demo['Haiku_Hands']['genre'] = INDIE;
    demo['Haiku_Hands']['discovery'] = BRIAN;
    demo['Haiku_Hands']['Seen_Live'] = False;
    demo['Haiku_Hands']['Kimi'] = False;

    demo['Hawthorne_Heights'] = dict()
    demo['Hawthorne_Heights']['Male'] = True; 
    demo['Hawthorne_Heights']['POC'] = False;
    demo['Hawthorne_Heights']['country'] = USA;
    demo['Hawthorne_Heights']['genre'] = EMO;
    demo['Hawthorne_Heights']['discovery'] = ON_MY_OWN_EMO;
    demo['Hawthorne_Heights']['Seen_Live'] = False;
    demo['Hawthorne_Heights']['Kimi'] = False;

    demo['INXS'] = dict()
    demo['INXS']['Male'] = True; 
    demo['INXS']['POC'] = False;
    demo['INXS']['country'] = ENGLAND;
    demo['INXS']['genre'] = OLD;
    demo['INXS']['discovery'] = ON_MY_OWN_OTHER;
    demo['INXS']['Seen_Live'] = False;
    demo['INXS']['Kimi'] = False;

    demo['Interpol'] = dict()
    demo['Interpol']['Male'] = True; 
    demo['Interpol']['POC'] = False;
    demo['Interpol']['country'] = USA;
    demo['Interpol']['genre'] = INDIE;
    demo['Interpol']['discovery'] = BRIAN;
    demo['Interpol']['Seen_Live'] = True;
    demo['Interpol']['Kimi'] = False;

    demo['Jack_Harlow'] = dict()
    demo['Jack_Harlow']['Male'] = True; 
    demo['Jack_Harlow']['POC'] = False;
    demo['Jack_Harlow']['country'] = USA;
    demo['Jack_Harlow']['genre'] = HIPHOP;
    demo['Jack_Harlow']['discovery'] = ON_MY_OWN_TV;
    demo['Jack_Harlow']['Seen_Live'] = False;
    demo['Jack_Harlow']['Kimi'] = False;

    demo['James_Blake'] = dict()
    demo['James_Blake']['Male'] = True; 
    demo['James_Blake']['POC'] = False;
    demo['James_Blake']['country'] = ENGLAND;
    demo['James_Blake']['genre'] = INDIE;
    demo['James_Blake']['discovery'] = KIMI;
    demo['James_Blake']['Seen_Live'] = True;
    demo['James_Blake']['Kimi'] = True;

    demo['Jeff_Rosenstock'] = dict()
    demo['Jeff_Rosenstock']['Male'] = True; 
    demo['Jeff_Rosenstock']['POC'] = False;
    demo['Jeff_Rosenstock']['country'] = USA;
    demo['Jeff_Rosenstock']['genre'] = INDIE;
    demo['Jeff_Rosenstock']['discovery'] = OLD_DAYS;
    demo['Jeff_Rosenstock']['Seen_Live'] = False;
    demo['Jeff_Rosenstock']['Kimi'] = False;

    demo['Joji'] = dict()
    demo['Joji']['Male'] = True; 
    demo['Joji']['POC'] = True;
    demo['Joji']['country'] = USA;
    demo['Joji']['genre'] = INDIE;
    demo['Joji']['discovery'] = KIMI;
    demo['Joji']['Seen_Live'] = True; #warning('Change when you see Joji')
    demo['Joji']['Kimi'] = True;

    demo['Jose_Gonzalez'] = dict()
    demo['Jose_Gonzalez']['Male'] = True; 
    demo['Jose_Gonzalez']['POC'] = True;
    demo['Jose_Gonzalez']['country'] = SWEDEN; #european...close enough
    demo['Jose_Gonzalez']['genre'] = INDIE;
    demo['Jose_Gonzalez']['discovery'] = BRIAN;
    demo['Jose_Gonzalez']['Seen_Live'] = False;
    demo['Jose_Gonzalez']['Kimi'] = False;

    demo['Joyce_Manor'] = dict()
    demo['Joyce_Manor']['Male'] = True; 
    demo['Joyce_Manor']['POC'] = False;
    demo['Joyce_Manor']['country'] = USA;
    demo['Joyce_Manor']['genre'] = EMO;
    demo['Joyce_Manor']['discovery'] = KIMI;
    demo['Joyce_Manor']['Seen_Live'] = True; 
    demo['Joyce_Manor']['Kimi'] = True;

    demo['Justin_Bieber'] = dict()
    demo['Justin_Bieber']['Male'] = True; 
    demo['Justin_Bieber']['POC'] = False;
    demo['Justin_Bieber']['country'] = CANADA;
    demo['Justin_Bieber']['genre'] = POP;
    demo['Justin_Bieber']['discovery'] = ON_MY_OWN_OTHER;
    demo['Justin_Bieber']['Seen_Live'] = False;
    demo['Justin_Bieber']['Kimi'] = False;

    demo['KennyHoopla'] = dict()
    demo['KennyHoopla']['Male'] = True; 
    demo['KennyHoopla']['POC'] = True;
    demo['KennyHoopla']['country'] = USA;
    demo['KennyHoopla']['genre'] = EMO;
    demo['KennyHoopla']['discovery'] = KIMI;
    demo['KennyHoopla']['Seen_Live'] = True;
    demo['KennyHoopla']['Kimi'] = True;

    demo['LCD_Soundsystem'] = dict()
    demo['LCD_Soundsystem']['Male'] = True; 
    demo['LCD_Soundsystem']['POC'] = False;
    demo['LCD_Soundsystem']['country'] = USA;
    demo['LCD_Soundsystem']['genre'] = INDIE;
    demo['LCD_Soundsystem']['discovery'] = OLD_DAYS;
    demo['LCD_Soundsystem']['Seen_Live'] = True;
    demo['LCD_Soundsystem']['Kimi'] = False;

    demo['LPX'] = dict()
    demo['LPX']['Male'] = False; 
    demo['LPX']['POC'] = False;
    demo['LPX']['country'] = USA;
    demo['LPX']['genre'] = INDIE;
    demo['LPX']['discovery'] = ON_MY_OWN_CONCERT;
    demo['LPX']['Seen_Live'] = False;
    demo['LPX']['Kimi'] = False;

    demo['La_La_Land'] = dict()
    demo['La_La_Land']['Male'] = True; 
    demo['La_La_Land']['POC'] = False;
    demo['La_La_Land']['country'] = USA;
    demo['La_La_Land']['genre'] = MUSICAL;
    demo['La_La_Land']['discovery'] = ON_MY_OWN_MUSICAL;
    demo['La_La_Land']['Seen_Live'] = False;
    demo['La_La_Land']['Kimi'] = False;

    demo['Lana_Del_Rey'] = dict()
    demo['Lana_Del_Rey']['Male'] = False; 
    demo['Lana_Del_Rey']['POC'] = False;
    demo['Lana_Del_Rey']['country'] = USA;
    demo['Lana_Del_Rey']['genre'] = INDIE;
    demo['Lana_Del_Rey']['discovery'] = KIMI;
    demo['Lana_Del_Rey']['Seen_Live'] = False;
    demo['Lana_Del_Rey']['Kimi'] = True;

    demo['Lauv'] = dict()
    demo['Lauv']['Male'] = True; 
    demo['Lauv']['POC'] = False;
    demo['Lauv']['country'] = USA;
    demo['Lauv']['genre'] = POP;
    demo['Lauv']['discovery'] = ON_MY_OWN_CONCERT;
    demo['Lauv']['Seen_Live'] = False;
    demo['Lauv']['Kimi'] = False;

    demo['Lil_Dicky'] = dict()
    demo['Lil_Dicky']['Male'] = True; 
    demo['Lil_Dicky']['POC'] = False;
    demo['Lil_Dicky']['country'] = USA;
    demo['Lil_Dicky']['genre'] = HIPHOP;
    demo['Lil_Dicky']['discovery'] = ON_MY_OWN_HIP_HOP;
    demo['Lil_Dicky']['Seen_Live'] = False;
    demo['Lil_Dicky']['Kimi'] = False;

    demo['Lil_Kleine'] = dict()
    demo['Lil_Kleine']['Male'] = True; 
    demo['Lil_Kleine']['POC'] = False;
    demo['Lil_Kleine']['country'] = NETHERLANDS;
    demo['Lil_Kleine']['genre'] = INDIE;
    demo['Lil_Kleine']['discovery'] = ON_MY_OWN_OTHER;
    demo['Lil_Kleine']['Seen_Live'] = False;
    demo['Lil_Kleine']['Kimi'] = False;

    demo['Lil_Pump'] = dict()
    demo['Lil_Pump']['Male'] = True; 
    demo['Lil_Pump']['POC'] = True;
    demo['Lil_Pump']['country'] = USA;
    demo['Lil_Pump']['genre'] = HIPHOP;
    demo['Lil_Pump']['discovery'] = ON_MY_OWN_HIP_HOP;
    demo['Lil_Pump']['Seen_Live'] = False;
    demo['Lil_Pump']['Kimi'] = False;

    demo['Los_Campesinos'] = dict()
    demo['Los_Campesinos']['Male'] = True; 
    demo['Los_Campesinos']['POC'] = False;
    demo['Los_Campesinos']['country'] = ENGLAND;
    demo['Los_Campesinos']['genre'] = INDIE;
    demo['Los_Campesinos']['discovery'] = OLD_DAYS;
    demo['Los_Campesinos']['Seen_Live'] = True;
    demo['Los_Campesinos']['Kimi'] = False;

    demo['Love_Victor_Theme'] = dict()
    demo['Love_Victor_Theme']['Male'] = True; 
    demo['Love_Victor_Theme']['POC'] = False;
    demo['Love_Victor_Theme']['country'] = USA;
    demo['Love_Victor_Theme']['genre'] = POP;
    demo['Love_Victor_Theme']['discovery'] = ON_MY_OWN_TV;
    demo['Love_Victor_Theme']['Seen_Live'] = False;
    demo['Love_Victor_Theme']['Kimi'] = False;

    demo['Lucky_Daye'] = dict()
    demo['Lucky_Daye']['Male'] = True; 
    demo['Lucky_Daye']['POC'] = True;
    demo['Lucky_Daye']['country'] = USA;
    demo['Lucky_Daye']['genre'] = R_AND_B;
    demo['Lucky_Daye']['discovery'] = KIMI;
    demo['Lucky_Daye']['Seen_Live'] = False;
    demo['Lucky_Daye']['Kimi'] = True;

    demo['MS_MR'] = dict()
    demo['MS_MR']['Male'] = False; 
    demo['MS_MR']['POC'] = False;
    demo['MS_MR']['country'] = USA;
    demo['MS_MR']['genre'] = INDIE;
    demo['MS_MR']['discovery'] = ON_MY_OWN_CONCERT;
    demo['MS_MR']['Seen_Live'] = True;
    demo['MS_MR']['Kimi'] = False;

    demo['Majid_Jordan'] = dict()
    demo['Majid_Jordan']['Male'] = True; 
    demo['Majid_Jordan']['POC'] = True;
    demo['Majid_Jordan']['country'] = CANADA;
    demo['Majid_Jordan']['genre'] = R_AND_B;
    demo['Majid_Jordan']['discovery'] = KIMI;
    demo['Majid_Jordan']['Seen_Live'] = False;
    demo['Majid_Jordan']['Kimi'] = True;

    demo['Maps_and_Atlases'] = dict()
    demo['Maps_and_Atlases']['Male'] = True; 
    demo['Maps_and_Atlases']['POC'] = False;
    demo['Maps_and_Atlases']['country'] = USA;
    demo['Maps_and_Atlases']['genre'] = INDIE;
    demo['Maps_and_Atlases']['discovery'] = OLD_DAYS;
    demo['Maps_and_Atlases']['Seen_Live'] = True;
    demo['Maps_and_Atlases']['Kimi'] = False;

    demo['Matt_Berninger'] = dict()
    demo['Matt_Berninger']['Male'] = True; 
    demo['Matt_Berninger']['POC'] = False;
    demo['Matt_Berninger']['country'] = USA;
    demo['Matt_Berninger']['genre'] = INDIE;
    demo['Matt_Berninger']['discovery'] = BRIAN;
    demo['Matt_Berninger']['Seen_Live'] = False;
    demo['Matt_Berninger']['Kimi'] = False;

    demo['Matt_and_Kim'] = dict()
    demo['Matt_and_Kim']['Male'] = True; 
    demo['Matt_and_Kim']['POC'] = False;
    demo['Matt_and_Kim']['country'] = USA;
    demo['Matt_and_Kim']['genre'] = INDIE;
    demo['Matt_and_Kim']['discovery'] = OLD_DAYS;
    demo['Matt_and_Kim']['Seen_Live'] = True;
    demo['Matt_and_Kim']['Kimi'] = False;

    demo['Miya_Folick'] = dict()
    demo['Miya_Folick']['Male'] = False; 
    demo['Miya_Folick']['POC'] = False;
    demo['Miya_Folick']['country'] = USA;
    demo['Miya_Folick']['genre'] = INDIE;
    demo['Miya_Folick']['discovery'] = ON_MY_OWN_TV;
    demo['Miya_Folick']['Seen_Live'] = False;
    demo['Miya_Folick']['Kimi'] = False;

    demo['Modest_Mouse'] = dict()
    demo['Modest_Mouse']['Male'] = True; 
    demo['Modest_Mouse']['POC'] = False;
    demo['Modest_Mouse']['country'] = USA;
    demo['Modest_Mouse']['genre'] = INDIE;
    demo['Modest_Mouse']['discovery'] = OLD_DAYS;
    demo['Modest_Mouse']['Seen_Live'] = True;
    demo['Modest_Mouse']['Kimi'] = False;

    demo['Motion_City_Soundtrack'] = dict()
    demo['Motion_City_Soundtrack']['Male'] = True; 
    demo['Motion_City_Soundtrack']['POC'] = False;
    demo['Motion_City_Soundtrack']['country'] = USA;
    demo['Motion_City_Soundtrack']['genre'] = EMO;
    demo['Motion_City_Soundtrack']['discovery'] = OLD_DAYS;
    demo['Motion_City_Soundtrack']['Seen_Live'] = True;
    demo['Motion_City_Soundtrack']['Kimi'] = True;

    demo['Moving_Units'] = dict()
    demo['Moving_Units']['Male'] = True; 
    demo['Moving_Units']['POC'] = False;
    demo['Moving_Units']['country'] = USA;
    demo['Moving_Units']['genre'] = INDIE;
    demo['Moving_Units']['discovery'] = OLD_DAYS;
    demo['Moving_Units']['Seen_Live'] = False;
    demo['Moving_Units']['Kimi'] = False;

    demo['My_Chemical_Romance'] = dict()
    demo['My_Chemical_Romance']['Male'] = True; 
    demo['My_Chemical_Romance']['POC'] = False;
    demo['My_Chemical_Romance']['country'] = USA;
    demo['My_Chemical_Romance']['genre'] = EMO;
    demo['My_Chemical_Romance']['discovery'] = ON_MY_OWN_EMO;
    demo['My_Chemical_Romance']['Seen_Live'] = False;
    demo['My_Chemical_Romance']['Kimi'] = True;

    demo['Nelly'] = dict()
    demo['Nelly']['Male'] = True; 
    demo['Nelly']['POC'] = True;
    demo['Nelly']['country'] = USA;
    demo['Nelly']['genre'] = HIPHOP;
    demo['Nelly']['discovery'] = ON_MY_OWN_HIP_HOP;
    demo['Nelly']['Seen_Live'] = False;
    demo['Nelly']['Kimi'] = False;

    demo['Paramore'] = dict()
    demo['Paramore']['Male'] = False; 
    demo['Paramore']['POC'] = False;
    demo['Paramore']['country'] = USA;
    demo['Paramore']['genre'] = EMO;
    demo['Paramore']['discovery'] = ON_MY_OWN_EMO;
    demo['Paramore']['Seen_Live'] = False;
    demo['Paramore']['Kimi'] = True;

    demo['Passion_Pit'] = dict()
    demo['Passion_Pit']['Male'] = True; 
    demo['Passion_Pit']['POC'] = False;
    demo['Passion_Pit']['country'] = USA;
    demo['Passion_Pit']['genre'] = INDIE;
    demo['Passion_Pit']['discovery'] = OLD_DAYS;
    demo['Passion_Pit']['Seen_Live'] = False;
    demo['Passion_Pit']['Kimi'] = False;

    demo['Pavement'] = dict()
    demo['Pavement']['Male'] = True; 
    demo['Pavement']['POC'] = False;
    demo['Pavement']['country'] = USA;
    demo['Pavement']['genre'] = OLD;
    demo['Pavement']['discovery'] = ON_MY_OWN_OTHER;
    demo['Pavement']['Seen_Live'] = False;
    demo['Pavement']['Kimi'] = True;

    demo['Plushgun'] = dict()
    demo['Plushgun']['Male'] = True; 
    demo['Plushgun']['POC'] = False;
    demo['Plushgun']['country'] = USA;
    demo['Plushgun']['genre'] = INDIE;
    demo['Plushgun']['discovery'] = OLD_DAYS;
    demo['Plushgun']['Seen_Live'] = False;
    demo['Plushgun']['Kimi'] = False;

    demo['Post_Malone'] = dict()
    demo['Post_Malone']['Male'] = True; 
    demo['Post_Malone']['POC'] = False;
    demo['Post_Malone']['country'] = USA;
    demo['Post_Malone']['genre'] = POP;
    demo['Post_Malone']['discovery'] = BRIAN;
    demo['Post_Malone']['Seen_Live'] = False;
    demo['Post_Malone']['Kimi'] = False;

    demo['Q'] = dict()
    demo['Q']['Male'] = True; 
    demo['Q']['POC'] = True;
    demo['Q']['country'] = USA; 
    demo['Q']['genre'] = INDIE;
    demo['Q']['discovery'] = KIMI;
    demo['Q']['Seen_Live'] = False;
    demo['Q']['Kimi'] = True;

    demo['RAP_Ferreira'] = dict()
    demo['RAP_Ferreira']['Male'] = True; 
    demo['RAP_Ferreira']['POC'] = True;
    demo['RAP_Ferreira']['country'] = USA;
    demo['RAP_Ferreira']['genre'] = HIPHOP;
    demo['RAP_Ferreira']['discovery'] = KIMI;
    demo['RAP_Ferreira']['Seen_Live'] = True;
    demo['RAP_Ferreira']['Kimi'] = True;

    demo['Ra_Ra_Riot'] = dict()
    demo['Ra_Ra_Riot']['Male'] = True; 
    demo['Ra_Ra_Riot']['POC'] = False;
    demo['Ra_Ra_Riot']['country'] = USA;
    demo['Ra_Ra_Riot']['genre'] = INDIE;
    demo['Ra_Ra_Riot']['discovery'] = OLD_DAYS;
    demo['Ra_Ra_Riot']['Seen_Live'] = True;
    demo['Ra_Ra_Riot']['Kimi'] = False;

    demo['Radiohead'] = dict()
    demo['Radiohead']['Male'] = True; 
    demo['Radiohead']['POC'] = False;
    demo['Radiohead']['country'] = USA;
    demo['Radiohead']['genre'] = INDIE;
    demo['Radiohead']['discovery'] = OLD_DAYS;
    demo['Radiohead']['Seen_Live'] = False;
    demo['Radiohead']['Kimi'] = False;

    demo['Regina_Spektor'] = dict()
    demo['Regina_Spektor']['Male'] = False; 
    demo['Regina_Spektor']['POC'] = False;  #huh, she's Russian
    demo['Regina_Spektor']['country'] = USA;
    demo['Regina_Spektor']['genre'] = INDIE;
    demo['Regina_Spektor']['discovery'] = OLD_DAYS;
    demo['Regina_Spektor']['Seen_Live'] = False;
    demo['Regina_Spektor']['Kimi'] = False;

    demo['Ripe'] = dict()
    demo['Ripe']['Male'] = True; 
    demo['Ripe']['POC'] = False;
    demo['Ripe']['country'] = USA;
    demo['Ripe']['genre'] = INDIE;
    demo['Ripe']['discovery'] = KIMI;
    demo['Ripe']['Seen_Live'] = True;
    demo['Ripe']['Kimi'] = True;

    demo['Run_The_Jewels'] = dict()
    demo['Run_The_Jewels']['Male'] = True; 
    demo['Run_The_Jewels']['POC'] = True;
    demo['Run_The_Jewels']['country'] = USA;
    demo['Run_The_Jewels']['genre'] = HIPHOP;
    demo['Run_The_Jewels']['discovery'] = ON_MY_OWN_HIP_HOP;
    demo['Run_The_Jewels']['Seen_Live'] = True;
    demo['Run_The_Jewels']['Kimi'] = True;

    demo['Russell_Crowe'] = dict()
    demo['Russell_Crowe']['Male'] = True; 
    demo['Russell_Crowe']['POC'] = False;
    demo['Russell_Crowe']['country'] = ENGLAND;
    demo['Russell_Crowe']['genre'] = MUSICAL;
    demo['Russell_Crowe']['discovery'] = ON_MY_OWN_MUSICAL;
    demo['Russell_Crowe']['Seen_Live'] = False;
    demo['Russell_Crowe']['Kimi'] = False;

    demo['SZA'] = dict()
    demo['SZA']['Male'] = False; 
    demo['SZA']['POC'] = True;
    demo['SZA']['country'] = USA;
    demo['SZA']['genre'] = R_AND_B;
    demo['SZA']['discovery'] = KIMI;
    demo['SZA']['Seen_Live'] = False;
    demo['SZA']['Kimi'] = True;

    demo['Sam_Smith'] = dict()
    demo['Sam_Smith']['Male'] = False; 
    demo['Sam_Smith']['POC'] = False;
    demo['Sam_Smith']['country'] = USA;
    demo['Sam_Smith']['genre'] = POP;
    demo['Sam_Smith']['discovery'] = ON_MY_OWN_TV;
    demo['Sam_Smith']['Seen_Live'] = False;
    demo['Sam_Smith']['Kimi'] = False;

    demo['San_Fermin'] = dict()
    demo['San_Fermin']['Male'] = True; 
    demo['San_Fermin']['POC'] = False;
    demo['San_Fermin']['country'] = USA;
    demo['San_Fermin']['genre'] = INDIE;
    demo['San_Fermin']['discovery'] = BRIAN;
    demo['San_Fermin']['Seen_Live'] = True;
    demo['San_Fermin']['Kimi'] = False;

    demo['Say_Anything'] = dict()
    demo['Say_Anything']['Male'] = True; 
    demo['Say_Anything']['POC'] = False;
    demo['Say_Anything']['country'] = USA;
    demo['Say_Anything']['genre'] = EMO;
    demo['Say_Anything']['discovery'] = KIMI;
    demo['Say_Anything']['Seen_Live'] = False;
    demo['Say_Anything']['Kimi'] = True;

    demo['Self_Esteem'] = dict()
    demo['Self_Esteem']['Male'] = False; 
    demo['Self_Esteem']['POC'] = False;
    demo['Self_Esteem']['country'] = ENGLAND;
    demo['Self_Esteem']['genre'] = INDIE;
    demo['Self_Esteem']['discovery'] = BRIAN;
    demo['Self_Esteem']['Seen_Live'] = False;
    demo['Self_Esteem']['Kimi'] = False;

    demo['Senses_Fail'] = dict()
    demo['Senses_Fail']['Male'] = True; 
    demo['Senses_Fail']['POC'] = False;
    demo['Senses_Fail']['country'] = USA;
    demo['Senses_Fail']['genre'] = EMO;
    demo['Senses_Fail']['discovery'] = ON_MY_OWN_EMO;
    demo['Senses_Fail']['Seen_Live'] = False;
    demo['Senses_Fail']['Kimi'] = False;

    demo['Silverstein'] = dict()
    demo['Silverstein']['Male'] = True; 
    demo['Silverstein']['POC'] = False;
    demo['Silverstein']['country'] = USA;
    demo['Silverstein']['genre'] = EMO;
    demo['Silverstein']['discovery'] = KIMI;
    demo['Silverstein']['Seen_Live'] = False;
    demo['Silverstein']['Kimi'] = True;

    demo['Sixpence_None_The_Richer'] = dict()
    demo['Sixpence_None_The_Richer']['Male'] = True; 
    demo['Sixpence_None_The_Richer']['POC'] = False;
    demo['Sixpence_None_The_Richer']['country'] = USA;
    demo['Sixpence_None_The_Richer']['genre'] = EMO;
    demo['Sixpence_None_The_Richer']['discovery'] = ON_MY_OWN_EMO;
    demo['Sixpence_None_The_Richer']['Seen_Live'] = False;
    demo['Sixpence_None_The_Richer']['Kimi'] = False;

    demo['Spoon'] = dict()
    demo['Spoon']['Male'] = True; 
    demo['Spoon']['POC'] = False;
    demo['Spoon']['country'] = USA;
    demo['Spoon']['genre'] = INDIE;
    demo['Spoon']['discovery'] = OLD_DAYS;
    demo['Spoon']['Seen_Live'] = True;
    demo['Spoon']['Kimi'] = False;

    demo['Sylvan_Esso'] = dict()
    demo['Sylvan_Esso']['Male'] = True; 
    demo['Sylvan_Esso']['POC'] = False;
    demo['Sylvan_Esso']['country'] = USA;
    demo['Sylvan_Esso']['genre'] = INDIE;
    demo['Sylvan_Esso']['discovery'] = BRIAN;
    demo['Sylvan_Esso']['Seen_Live'] = False;
    demo['Sylvan_Esso']['Kimi'] = False;

    demo['Taylor_Swift'] = dict()
    demo['Taylor_Swift']['Male'] = False; 
    demo['Taylor_Swift']['POC'] = False;
    demo['Taylor_Swift']['country'] = USA;
    demo['Taylor_Swift']['genre'] = INDIE;
    demo['Taylor_Swift']['discovery'] = ON_MY_OWN_OTHER;
    demo['Taylor_Swift']['Seen_Live'] = False;
    demo['Taylor_Swift']['Kimi'] = False;

    demo['Tegan_and_Sara'] = dict()
    demo['Tegan_and_Sara']['Male'] = False; 
    demo['Tegan_and_Sara']['POC'] = False;
    demo['Tegan_and_Sara']['country'] = USA;
    demo['Tegan_and_Sara']['genre'] = INDIE;
    demo['Tegan_and_Sara']['discovery'] = OLD_DAYS;
    demo['Tegan_and_Sara']['Seen_Live'] = False;
    demo['Tegan_and_Sara']['Kimi'] = False;

    demo['The_1975'] = dict()
    demo['The_1975']['Male'] = True; 
    demo['The_1975']['POC'] = False;
    demo['The_1975']['country'] = USA;
    demo['The_1975']['genre'] = INDIE;
    demo['The_1975']['discovery'] = BRIAN;
    demo['The_1975']['Seen_Live'] = False;
    demo['The_1975']['Kimi'] = False;

    demo['The_Bravery'] = dict()
    demo['The_Bravery']['Male'] = True; 
    demo['The_Bravery']['POC'] = False;
    demo['The_Bravery']['country'] = USA;
    demo['The_Bravery']['genre'] = INDIE;
    demo['The_Bravery']['discovery'] = OLD_DAYS;
    demo['The_Bravery']['Seen_Live'] = True;
    demo['The_Bravery']['Kimi'] = False;

    demo['The_Faint'] = dict()
    demo['The_Faint']['Male'] = True; 
    demo['The_Faint']['POC'] = False;
    demo['The_Faint']['country'] = USA;
    demo['The_Faint']['genre'] = INDIE;
    demo['The_Faint']['discovery'] = OLD_DAYS;
    demo['The_Faint']['Seen_Live'] = False;
    demo['The_Faint']['Kimi'] = False;

    demo['The_Get_Up_Kids'] = dict()
    demo['The_Get_Up_Kids']['Male'] = True; 
    demo['The_Get_Up_Kids']['POC'] = False;
    demo['The_Get_Up_Kids']['country'] = USA;
    demo['The_Get_Up_Kids']['genre'] = EMO;
    demo['The_Get_Up_Kids']['discovery'] = ON_MY_OWN_EMO;
    demo['The_Get_Up_Kids']['Seen_Live'] = True;
    demo['The_Get_Up_Kids']['Kimi'] = False;

    demo['The_Killers'] = dict()
    demo['The_Killers']['Male'] = True; 
    demo['The_Killers']['POC'] = False;
    demo['The_Killers']['country'] = USA;
    demo['The_Killers']['genre'] = INDIE;
    demo['The_Killers']['discovery'] = OLD_DAYS;
    demo['The_Killers']['Seen_Live'] = True;
    demo['The_Killers']['Kimi'] = True;

    demo['The_National'] = dict()
    demo['The_National']['Male'] = True; 
    demo['The_National']['POC'] = False;
    demo['The_National']['country'] = USA;
    demo['The_National']['genre'] = INDIE;
    demo['The_National']['discovery'] = OLD_DAYS;
    demo['The_National']['Seen_Live'] = True;
    demo['The_National']['Kimi'] = True;

    demo['The_Ninth_Wave'] = dict()
    demo['The_Ninth_Wave']['Male'] = True; 
    demo['The_Ninth_Wave']['POC'] = False;
    demo['The_Ninth_Wave']['country'] = ENGLAND;
    demo['The_Ninth_Wave']['genre'] = INDIE;
    demo['The_Ninth_Wave']['discovery'] = BRIAN;
    demo['The_Ninth_Wave']['Seen_Live'] = False;
    demo['The_Ninth_Wave']['Kimi'] = False;

    demo['The_Postal_Service'] = dict()
    demo['The_Postal_Service']['Male'] = True; 
    demo['The_Postal_Service']['POC'] = False;
    demo['The_Postal_Service']['country'] = USA;
    demo['The_Postal_Service']['genre'] = INDIE;
    demo['The_Postal_Service']['discovery'] = OLD_DAYS;
    demo['The_Postal_Service']['Seen_Live'] = False;
    demo['The_Postal_Service']['Kimi'] = False;

    demo['The_Strokes'] = dict()
    demo['The_Strokes']['Male'] = True; 
    demo['The_Strokes']['POC'] = False;
    demo['The_Strokes']['country'] = USA;
    demo['The_Strokes']['genre'] = INDIE;
    demo['The_Strokes']['discovery'] = OLD_DAYS;
    demo['The_Strokes']['Seen_Live'] = True;
    demo['The_Strokes']['Kimi'] = False;

    demo['The_Weeknd'] = dict()
    demo['The_Weeknd']['Male'] = True; 
    demo['The_Weeknd']['POC'] = True;
    demo['The_Weeknd']['country'] = CANADA;  #canadian...
    demo['The_Weeknd']['genre'] = R_AND_B;
    demo['The_Weeknd']['discovery'] = KIMI;
    demo['The_Weeknd']['Seen_Live'] = True;
    demo['The_Weeknd']['Kimi'] = True;

    demo['The_xx'] = dict()
    demo['The_xx']['Male'] = True; 
    demo['The_xx']['POC'] = False;
    demo['The_xx']['country'] = ENGLAND;
    demo['The_xx']['genre'] = INDIE;
    demo['The_xx']['discovery'] = OLD_DAYS;
    demo['The_xx']['Seen_Live'] = False;
    demo['The_xx']['Kimi'] = True;

    demo['Thom_Yorke'] = dict()
    demo['Thom_Yorke']['Male'] = True; 
    demo['Thom_Yorke']['POC'] = False;
    demo['Thom_Yorke']['country'] = ENGLAND;
    demo['Thom_Yorke']['genre'] = INDIE;
    demo['Thom_Yorke']['discovery'] = ON_MY_OWN_OTHER;
    demo['Thom_Yorke']['Seen_Live'] = False;
    demo['Thom_Yorke']['Kimi'] = False;

    demo['Tick_Tick_Boom'] = dict()
    demo['Tick_Tick_Boom']['Male'] = True; 
    demo['Tick_Tick_Boom']['POC'] = False;
    demo['Tick_Tick_Boom']['country'] = USA;
    demo['Tick_Tick_Boom']['genre'] = MUSICAL;
    demo['Tick_Tick_Boom']['discovery'] = ON_MY_OWN_MUSICAL;
    demo['Tick_Tick_Boom']['Seen_Live'] = False;
    demo['Tick_Tick_Boom']['Kimi'] = False;

    demo['Topaz_Jones'] = dict()
    demo['Topaz_Jones']['Male'] = True; 
    demo['Topaz_Jones']['POC'] = True;
    demo['Topaz_Jones']['country'] = USA;
    demo['Topaz_Jones']['genre'] = R_AND_B;
    demo['Topaz_Jones']['discovery'] = KIMI;
    demo['Topaz_Jones']['Seen_Live'] = False;
    demo['Topaz_Jones']['Kimi'] = True;

    demo['Twin_Shadow'] = dict()
    demo['Twin_Shadow']['Male'] = True; 
    demo['Twin_Shadow']['POC'] = True;
    demo['Twin_Shadow']['country'] = USA;
    demo['Twin_Shadow']['genre'] = INDIE;
    demo['Twin_Shadow']['discovery'] = BRIAN;
    demo['Twin_Shadow']['Seen_Live'] = False;
    demo['Twin_Shadow']['Kimi'] = True;

    demo['Two_Door_Cinema_Club'] = dict()
    demo['Two_Door_Cinema_Club']['Male'] = True; 
    demo['Two_Door_Cinema_Club']['POC'] = False;
    demo['Two_Door_Cinema_Club']['country'] = USA;
    demo['Two_Door_Cinema_Club']['genre'] = INDIE;
    demo['Two_Door_Cinema_Club']['discovery'] = OLD_DAYS;
    demo['Two_Door_Cinema_Club']['Seen_Live'] = True;
    demo['Two_Door_Cinema_Club']['Kimi'] = False;

    demo['Tyler_the_Creator'] = dict()
    demo['Tyler_the_Creator']['Male'] = True; 
    demo['Tyler_the_Creator']['POC'] = True;
    demo['Tyler_the_Creator']['country'] = USA;
    demo['Tyler_the_Creator']['genre'] = HIPHOP;
    demo['Tyler_the_Creator']['discovery'] = KIMI;
    demo['Tyler_the_Creator']['Seen_Live'] = False;
    demo['Tyler_the_Creator']['Kimi'] = True;

    demo['Walk_The_Moon'] = dict()
    demo['Walk_The_Moon']['Male'] = True; 
    demo['Walk_The_Moon']['POC'] = False;
    demo['Walk_The_Moon']['country'] = USA;
    demo['Walk_The_Moon']['genre'] = INDIE;
    demo['Walk_The_Moon']['discovery'] = OLD_DAYS;
    demo['Walk_The_Moon']['Seen_Live'] = True;
    demo['Walk_The_Moon']['Kimi'] = False;

    demo['We_Are_Scientists'] = dict()
    demo['We_Are_Scientists']['Male'] = True; 
    demo['We_Are_Scientists']['POC'] = False;
    demo['We_Are_Scientists']['country'] = USA;
    demo['We_Are_Scientists']['genre'] = INDIE;
    demo['We_Are_Scientists']['discovery'] = OLD_DAYS;
    demo['We_Are_Scientists']['Seen_Live'] = True;
    demo['We_Are_Scientists']['Kimi'] = False;

    demo['White_Lies'] = dict()
    demo['White_Lies']['Male'] = True; 
    demo['White_Lies']['POC'] = False;
    demo['White_Lies']['country'] = ENGLAND;
    demo['White_Lies']['genre'] = INDIE;
    demo['White_Lies']['discovery'] = BRIAN;
    demo['White_Lies']['Seen_Live'] = False;
    demo['White_Lies']['Kimi'] = False;

    demo['The_White_Stripes'] = dict()
    demo['The_White_Stripes']['Male'] = True; 
    demo['The_White_Stripes']['POC'] = False;
    demo['The_White_Stripes']['country'] = USA;
    demo['The_White_Stripes']['genre'] = INDIE;
    demo['The_White_Stripes']['discovery'] = OLD_DAYS;
    demo['The_White_Stripes']['Seen_Live'] = False;
    demo['The_White_Stripes']['Kimi'] = False;

    demo['Yeasayer'] = dict()
    demo['Yeasayer']['Male'] = True; 
    demo['Yeasayer']['POC'] = False;
    demo['Yeasayer']['country'] = USA;
    demo['Yeasayer']['genre'] = INDIE;
    demo['Yeasayer']['discovery'] = BRIAN;
    demo['Yeasayer']['Seen_Live'] = True;
    demo['Yeasayer']['Kimi'] = False;

    demo['One_Hundred_Gecs'] = dict()
    demo['One_Hundred_Gecs']['Male'] = False; 
    demo['One_Hundred_Gecs']['POC'] = False;
    demo['One_Hundred_Gecs']['country'] = USA;
    demo['One_Hundred_Gecs']['genre'] = POP;
    demo['One_Hundred_Gecs']['discovery'] = BRIAN;
    demo['One_Hundred_Gecs']['Seen_Live'] = False;
    demo['One_Hundred_Gecs']['Kimi'] = False;

    demo['The_Shins'] = dict()
    demo['The_Shins']['Male'] = True; 
    demo['The_Shins']['POC'] = False;
    demo['The_Shins']['country'] = USA;
    demo['The_Shins']['genre'] = INDIE;
    demo['The_Shins']['discovery'] = ON_MY_OWN_CONCERT;
    demo['The_Shins']['Seen_Live'] = True;
    demo['The_Shins']['Kimi'] = False;

    demo['Franz_Ferdinand'] = dict()
    demo['Franz_Ferdinand']['Male'] = True; 
    demo['Franz_Ferdinand']['POC'] = False;
    demo['Franz_Ferdinand']['country'] = ENGLAND;
    demo['Franz_Ferdinand']['genre'] = INDIE;
    demo['Franz_Ferdinand']['discovery'] = OLD_DAYS;
    demo['Franz_Ferdinand']['Seen_Live'] = False;
    demo['Franz_Ferdinand']['Kimi'] = False;

    demo['Ok_Go'] = dict()
    demo['Ok_Go']['Male'] = True; 
    demo['Ok_Go']['POC'] = False;
    demo['Ok_Go']['country'] = USA;
    demo['Ok_Go']['genre'] = INDIE;
    demo['Ok_Go']['discovery'] = OLD_DAYS;
    demo['Ok_Go']['Seen_Live'] = True;
    demo['Ok_Go']['Kimi'] = False;

    demo['Fun'] = dict()
    demo['Fun']['Male'] = True; 
    demo['Fun']['POC'] = False;
    demo['Fun']['country'] = USA;
    demo['Fun']['genre'] = INDIE;
    demo['Fun']['discovery'] = OLD_DAYS;
    demo['Fun']['Seen_Live'] = True;
    demo['Fun']['Kimi'] = False;

    demo['Elton_John'] = dict()
    demo['Elton_John']['Male'] = True; 
    demo['Elton_John']['POC'] = False;
    demo['Elton_John']['country'] = ENGLAND;
    demo['Elton_John']['genre'] = OLD;
    demo['Elton_John']['discovery'] = ON_MY_OWN_TV;
    demo['Elton_John']['Seen_Live'] = False;
    demo['Elton_John']['Kimi'] = False;

    demo['Mumford_And_Sons'] = dict()
    demo['Mumford_And_Sons']['Male'] = True; 
    demo['Mumford_And_Sons']['POC'] = False;
    demo['Mumford_And_Sons']['country'] = ENGLAND;
    demo['Mumford_And_Sons']['genre'] = INDIE;
    demo['Mumford_And_Sons']['discovery'] = OLD_DAYS;
    demo['Mumford_And_Sons']['Seen_Live'] = True;
    demo['Mumford_And_Sons']['Kimi'] = False;

    demo['Bloc_Party'] = dict()
    demo['Bloc_Party']['Male'] = True; 
    demo['Bloc_Party']['POC'] = True;
    demo['Bloc_Party']['country'] = ENGLAND;
    demo['Bloc_Party']['genre'] = INDIE;
    demo['Bloc_Party']['discovery'] = OLD_DAYS;
    demo['Bloc_Party']['Seen_Live'] = False;
    demo['Bloc_Party']['Kimi'] = False;

    demo['The_Kooks'] = dict()
    demo['The_Kooks']['Male'] = True; 
    demo['The_Kooks']['POC'] = False;
    demo['The_Kooks']['country'] = ENGLAND;
    demo['The_Kooks']['genre'] = INDIE;
    demo['The_Kooks']['discovery'] = OLD_DAYS;
    demo['The_Kooks']['Seen_Live'] = True;
    demo['The_Kooks']['Kimi'] = True;

    demo['Kaiser_Chiefs'] = dict()
    demo['Kaiser_Chiefs']['Male'] = True; 
    demo['Kaiser_Chiefs']['POC'] = False;
    demo['Kaiser_Chiefs']['country'] = ENGLAND;
    demo['Kaiser_Chiefs']['genre'] = INDIE;
    demo['Kaiser_Chiefs']['discovery'] = OLD_DAYS;
    demo['Kaiser_Chiefs']['Seen_Live'] = True;
    demo['Kaiser_Chiefs']['Kimi'] = False;

    demo['Jungle'] = dict()
    demo['Jungle']['Male'] = True; 
    demo['Jungle']['POC'] = False;
    demo['Jungle']['country'] = ENGLAND;
    demo['Jungle']['genre'] = INDIE;
    demo['Jungle']['discovery'] = BRIAN;
    demo['Jungle']['Seen_Live'] = False;
    demo['Jungle']['Kimi'] = False;

    demo['Beyonce'] = dict()
    demo['Beyonce']['Male'] = False; 
    demo['Beyonce']['POC'] = True;
    demo['Beyonce']['country'] = USA;
    demo['Beyonce']['genre'] = POP;
    demo['Beyonce']['discovery'] = ON_MY_OWN_OTHER;
    demo['Beyonce']['Seen_Live'] = False;
    demo['Beyonce']['Kimi'] = False;

    demo['Dirty_Projectors'] = dict()
    demo['Dirty_Projectors']['Male'] = True; 
    demo['Dirty_Projectors']['POC'] = False;
    demo['Dirty_Projectors']['country'] = USA;
    demo['Dirty_Projectors']['genre'] = INDIE;
    demo['Dirty_Projectors']['discovery'] = ON_MY_OWN_CONCERT;
    demo['Dirty_Projectors']['Seen_Live'] = True;
    demo['Dirty_Projectors']['Kimi'] = False;

    demo['Bad_Bunny'] = dict()
    demo['Bad_Bunny']['Male'] = True; 
    demo['Bad_Bunny']['POC'] = True;
    demo['Bad_Bunny']['country'] = USA; #puerto rico
    demo['Bad_Bunny']['genre'] = HIPHOP; #Latin trap · reggaeton · alternative reggaeton....doesn't fit anything!
    demo['Bad_Bunny']['discovery'] = ON_MY_OWN_OTHER;
    demo['Bad_Bunny']['Seen_Live'] = False;
    demo['Bad_Bunny']['Kimi'] = False;

    demo['Zoeys_Extra_Playlist'] = dict()
    demo['Zoeys_Extra_Playlist']['Male'] = False; 
    demo['Zoeys_Extra_Playlist']['POC'] = False;
    demo['Zoeys_Extra_Playlist']['country'] = USA;
    demo['Zoeys_Extra_Playlist']['genre'] = MUSICAL;
    demo['Zoeys_Extra_Playlist']['discovery'] = ON_MY_OWN_MUSICAL;
    demo['Zoeys_Extra_Playlist']['Seen_Live'] = False;
    demo['Zoeys_Extra_Playlist']['Kimi'] = True;

    demo['Black_English'] = dict()
    demo['Black_English']['Male'] = True; 
    demo['Black_English']['POC'] = False;
    demo['Black_English']['country'] = USA;
    demo['Black_English']['genre'] = INDIE;
    demo['Black_English']['discovery'] = OLD_DAYS;
    demo['Black_English']['Seen_Live'] = False;
    demo['Black_English']['Kimi'] = False;

    demo['Kishi_Bashi'] = dict()
    demo['Kishi_Bashi']['Male'] = True; 
    demo['Kishi_Bashi']['POC'] = True;
    demo['Kishi_Bashi']['country'] = USA;
    demo['Kishi_Bashi']['genre'] = INDIE;
    demo['Kishi_Bashi']['discovery'] = ON_MY_OWN_OTHER; #Shazam Restraunt in Philly
    demo['Kishi_Bashi']['Seen_Live'] = False;
    demo['Kishi_Bashi']['Kimi'] = False;

    demo['Dijon'] = dict()
    demo['Dijon']['Male'] = True; 
    demo['Dijon']['POC'] = True;
    demo['Dijon']['country'] = USA;
    demo['Dijon']['genre'] = R_AND_B;
    demo['Dijon']['discovery'] = KIMI;
    demo['Dijon']['Seen_Live'] = False;
    demo['Dijon']['Kimi'] = True;

    demo['Broken_Bells'] = dict()
    demo['Broken_Bells']['Male'] = True; 
    demo['Broken_Bells']['POC'] = False;
    demo['Broken_Bells']['country'] = USA;
    demo['Broken_Bells']['genre'] = INDIE;
    demo['Broken_Bells']['discovery'] = ON_MY_OWN_OTHER;
    demo['Broken_Bells']['Seen_Live'] = False;
    demo['Broken_Bells']['Kimi'] = False;

    demo['Arkells'] = dict()
    demo['Arkells']['Male'] = True; 
    demo['Arkells']['POC'] = False;
    demo['Arkells']['country'] = USA;
    demo['Arkells']['genre'] = INDIE;
    demo['Arkells']['discovery'] = ON_MY_OWN_CONCERT;
    demo['Arkells']['Seen_Live'] = True;
    demo['Arkells']['Kimi'] = False;

    demo['Holly_Homberstone'] = dict()
    demo['Holly_Homberstone']['Male'] = False; 
    demo['Holly_Homberstone']['POC'] = False;
    demo['Holly_Homberstone']['country'] = USA;
    demo['Holly_Homberstone']['genre'] = INDIE;
    demo['Holly_Homberstone']['discovery'] = BRIAN;
    demo['Holly_Homberstone']['Seen_Live'] = False;
    demo['Holly_Homberstone']['Kimi'] = True;

    demo['Ying_Yang_Twins'] = dict()
    demo['Ying_Yang_Twins']['Male'] = True; 
    demo['Ying_Yang_Twins']['POC'] = True;
    demo['Ying_Yang_Twins']['country'] = USA;
    demo['Ying_Yang_Twins']['genre'] = HIPHOP;
    demo['Ying_Yang_Twins']['discovery'] = ON_MY_OWN_HIP_HOP;
    demo['Ying_Yang_Twins']['Seen_Live'] = False;
    demo['Ying_Yang_Twins']['Kimi'] = False;

    demo['Mates_Of_State'] = dict()
    demo['Mates_Of_State']['Male'] = True; 
    demo['Mates_Of_State']['POC'] = False;
    demo['Mates_Of_State']['country'] = USA;
    demo['Mates_Of_State']['genre'] = INDIE;
    demo['Mates_Of_State']['discovery'] = OLD_DAYS;
    demo['Mates_Of_State']['Seen_Live'] = False;
    demo['Mates_Of_State']['Kimi'] = False;

    demo['The_Fall_of_Troy'] = dict()
    demo['The_Fall_of_Troy']['Male'] = True; 
    demo['The_Fall_of_Troy']['POC'] = False;
    demo['The_Fall_of_Troy']['country'] = USA;
    demo['The_Fall_of_Troy']['genre'] = EMO;
    demo['The_Fall_of_Troy']['discovery'] = ON_MY_OWN_EMO;
    demo['The_Fall_of_Troy']['Seen_Live'] = False;
    demo['The_Fall_of_Troy']['Kimi'] = False;

    demo['Crystal_Castles'] = dict()
    demo['Crystal_Castles']['Male'] = True; 
    demo['Crystal_Castles']['POC'] = False;
    demo['Crystal_Castles']['country'] = USA;
    demo['Crystal_Castles']['genre'] = INDIE;
    demo['Crystal_Castles']['discovery'] = OLD_DAYS;
    demo['Crystal_Castles']['Seen_Live'] = False;
    demo['Crystal_Castles']['Kimi'] = False;

    demo['Peaches'] = dict()
    demo['Peaches']['Male'] = False; 
    demo['Peaches']['POC'] = False;
    demo['Peaches']['country'] = CANADA;
    demo['Peaches']['genre'] = INDIE;
    demo['Peaches']['discovery'] = BRIAN;
    demo['Peaches']['Seen_Live'] = False;
    demo['Peaches']['Kimi'] = False;

    demo['Razorlight'] = dict()
    demo['Razorlight']['Male'] = True;
    demo['Razorlight']['POC'] = False;
    demo['Razorlight']['country'] = ENGLAND;
    demo['Razorlight']['genre'] = INDIE;
    demo['Razorlight']['discovery'] = OLD_DAYS;
    demo['Razorlight']['Seen_Live'] = False;
    demo['Razorlight']['Kimi'] = False;
    
    demo['She_Wants_Revenge'] = dict()
    demo['She_Wants_Revenge']['Male'] = True; 
    demo['She_Wants_Revenge']['POC'] = False;
    demo['She_Wants_Revenge']['country'] = USA;
    demo['She_Wants_Revenge']['genre'] = EMO;
    demo['She_Wants_Revenge']['discovery'] = ON_MY_OWN_OTHER;
    demo['She_Wants_Revenge']['Seen_Live'] = False;
    demo['She_Wants_Revenge']['Kimi'] = False;
    
    demo['The_Birthday_Massacre'] = dict()
    demo['The_Birthday_Massacre']['Male'] = True; 
    demo['The_Birthday_Massacre']['POC'] = False;
    demo['The_Birthday_Massacre']['country'] = USA;
    demo['The_Birthday_Massacre']['genre'] = EMO;
    demo['The_Birthday_Massacre']['discovery'] = MUSIC_LEAGUE; #music league Brian
    demo['The_Birthday_Massacre']['Seen_Live'] = False;
    demo['The_Birthday_Massacre']['Kimi'] = False;
    
    demo['Maximum_Baloon'] = dict()
    demo['Maximum_Baloon']['Male'] = True; 
    demo['Maximum_Baloon']['POC'] = False;
    demo['Maximum_Baloon']['country'] = USA;
    demo['Maximum_Baloon']['genre'] = INDIE;
    demo['Maximum_Baloon']['discovery'] = OLD_DAYS; 
    demo['Maximum_Baloon']['Seen_Live'] = False;
    demo['Maximum_Baloon']['Kimi'] = False;
    
    demo['Arlo_Parks'] = dict()
    demo['Arlo_Parks']['Male'] = False; 
    demo['Arlo_Parks']['POC'] = True;
    demo['Arlo_Parks']['country'] = ENGLAND;
    demo['Arlo_Parks']['genre'] = R_AND_B;
    demo['Arlo_Parks']['discovery'] = MUSIC_LEAGUE; #music league
    demo['Arlo_Parks']['Seen_Live'] = False;
    demo['Arlo_Parks']['Kimi'] = False;
    
    demo['Chappell_Roan'] = dict()
    demo['Chappell_Roan']['Male'] = False; 
    demo['Chappell_Roan']['POC'] = False;
    demo['Chappell_Roan']['country'] = USA;
    demo['Chappell_Roan']['genre'] = INDIE;
    demo['Chappell_Roan']['discovery'] = MUSIC_LEAGUE; #music league
    demo['Chappell_Roan']['Seen_Live'] = False;
    demo['Chappell_Roan']['Kimi'] = True;

    demo['Four_Year_Strong'] = dict()
    demo['Four_Year_Strong']['Male'] = True; 
    demo['Four_Year_Strong']['POC'] = False;
    demo['Four_Year_Strong']['country'] = USA;
    demo['Four_Year_Strong']['genre'] = EMO;
    demo['Four_Year_Strong']['discovery'] = MUSIC_LEAGUE; #SPENCER! music league
    demo['Four_Year_Strong']['Seen_Live'] = False;
    demo['Four_Year_Strong']['Kimi'] = False;    

    demo['Brent_Faiyaz'] = dict()
    demo['Brent_Faiyaz']['Male'] = True; 
    demo['Brent_Faiyaz']['POC'] = True;
    demo['Brent_Faiyaz']['country'] = USA;
    demo['Brent_Faiyaz']['genre'] = R_AND_B;
    demo['Brent_Faiyaz']['discovery'] = KIMI;
    demo['Brent_Faiyaz']['Seen_Live'] = False;
    demo['Brent_Faiyaz']['Kimi'] = True;
    
    demo['Bring_Me_the_Horizon'] = dict()
    demo['Bring_Me_the_Horizon']['Male'] = True; 
    demo['Bring_Me_the_Horizon']['POC'] = False;
    demo['Bring_Me_the_Horizon']['country'] = USA;
    demo['Bring_Me_the_Horizon']['genre'] = EMO;
    demo['Bring_Me_the_Horizon']['discovery'] = ON_MY_OWN_EMO;
    demo['Bring_Me_the_Horizon']['Seen_Live'] = False;
    demo['Bring_Me_the_Horizon']['Kimi'] = False; 
    
    demo['Half_Alive'] = dict()
    demo['Half_Alive']['Male'] = True; 
    demo['Half_Alive']['POC'] = False;
    demo['Half_Alive']['country'] = USA;
    demo['Half_Alive']['genre'] = INDIE;
    demo['Half_Alive']['discovery'] = MUSIC_LEAGUE; #Music League
    demo['Half_Alive']['Seen_Live'] = False;
    demo['Half_Alive']['Kimi'] = False; 
    
    demo['Poppy'] = dict()
    demo['Poppy']['Male'] = False; 
    demo['Poppy']['POC'] = False;
    demo['Poppy']['country'] = USA;
    demo['Poppy']['genre'] = EMO;  #wtf genre is this lol
    demo['Poppy']['discovery'] = MUSIC_LEAGUE; #Music League
    demo['Poppy']['Seen_Live'] = False;
    demo['Poppy']['Kimi'] = False;

    demo['Pale_Waves'] = dict()
    demo['Pale_Waves']['Male'] = False; 
    demo['Pale_Waves']['POC'] = False;
    demo['Pale_Waves']['country'] = ENGLAND;
    demo['Pale_Waves']['genre'] = EMO;  #wtf genre is this lol
    demo['Pale_Waves']['discovery'] = BRIAN; #Music League
    demo['Pale_Waves']['Seen_Live'] = False;
    demo['Pale_Waves']['Kimi'] = False;
    
    demo['Charming_Jo'] = dict()
    demo['Charming_Jo']['Male'] = True; 
    demo['Charming_Jo']['POC'] = True;
    demo['Charming_Jo']['country'] = USA;
    demo['Charming_Jo']['genre'] = POP;  #wtf genre is this lol
    demo['Charming_Jo']['discovery'] = ON_MY_OWN_OTHER; #reddit
    demo['Charming_Jo']['Seen_Live'] = False;
    demo['Charming_Jo']['Kimi'] = False;
    
    demo['Yves_Tumor'] = dict()
    demo['Yves_Tumor']['Male'] = True; 
    demo['Yves_Tumor']['POC'] = True;
    demo['Yves_Tumor']['country'] = USA;
    demo['Yves_Tumor']['genre'] = R_AND_B;
    demo['Yves_Tumor']['discovery'] = KIMI;
    demo['Yves_Tumor']['Seen_Live'] = False;
    demo['Yves_Tumor']['Kimi'] = True;
    
    demo['Jukebox_the_Ghost'] = dict()
    demo['Jukebox_the_Ghost']['Male'] = True; 
    demo['Jukebox_the_Ghost']['POC'] = False;
    demo['Jukebox_the_Ghost']['country'] = USA;
    demo['Jukebox_the_Ghost']['genre'] = INDIE;
    demo['Jukebox_the_Ghost']['discovery'] = MUSIC_LEAGUE; #music league - Nikki
    demo['Jukebox_the_Ghost']['Seen_Live'] = True;
    demo['Jukebox_the_Ghost']['Kimi'] = False;
    
    demo['AJR'] = dict()
    demo['AJR']['Male'] = True; 
    demo['AJR']['POC'] = False;
    demo['AJR']['country'] = USA;
    demo['AJR']['genre'] = INDIE;
    demo['AJR']['discovery'] = MUSIC_LEAGUE;  #music league
    demo['AJR']['Seen_Live'] = False;
    demo['AJR']['Kimi'] = False;
    
    demo['dvsn'] = dict()
    demo['dvsn']['Male'] = True; 
    demo['dvsn']['POC'] = True;
    demo['dvsn']['country'] = USA;
    demo['dvsn']['genre'] = R_AND_B;
    demo['dvsn']['discovery'] = KIMI;
    demo['dvsn']['Seen_Live'] = False;
    demo['dvsn']['Kimi'] = True;

    demo['Vanshire'] = dict()
    demo['Vanshire']['Male'] = True; 
    demo['Vanshire']['POC'] = False;
    demo['Vanshire']['country'] = USA;
    demo['Vanshire']['genre'] = INDIE;
    demo['Vanshire']['discovery'] = ON_MY_OWN_OTHER;
    demo['Vanshire']['Seen_Live'] = False;
    demo['Vanshire']['Kimi'] = False;
    
    demo['Phoebe_Bridgers'] = dict()
    demo['Phoebe_Bridgers']['Male'] = False; 
    demo['Phoebe_Bridgers']['POC'] = False;
    demo['Phoebe_Bridgers']['country'] = USA;
    demo['Phoebe_Bridgers']['genre'] = INDIE;
    demo['Phoebe_Bridgers']['discovery'] = BRIAN;
    demo['Phoebe_Bridgers']['Seen_Live'] = False;
    demo['Phoebe_Bridgers']['Kimi'] = False;
    
    demo['The_Kooks'] = dict()
    demo['The_Kooks']['Male'] = True; 
    demo['The_Kooks']['POC'] = False;
    demo['The_Kooks']['country'] = ENGLAND;
    demo['The_Kooks']['genre'] = INDIE;
    demo['The_Kooks']['discovery'] = OLD_DAYS;
    demo['The_Kooks']['Seen_Live'] = True;
    demo['The_Kooks']['Kimi'] = True;
    
    demo['Griff'] = dict()
    demo['Griff']['Male'] = False; 
    demo['Griff']['POC'] = True;
    demo['Griff']['country'] = ENGLAND;
    demo['Griff']['genre'] = INDIE;
    demo['Griff']['discovery'] = MUSIC_LEAGUE; #Music League
    demo['Griff']['Seen_Live'] = False;
    demo['Griff']['Kimi'] = False;\
    
    demo['The_Chainsmokers'] = dict()
    demo['The_Chainsmokers']['Male'] = True; 
    demo['The_Chainsmokers']['POC'] = False;
    demo['The_Chainsmokers']['country'] = USA;
    demo['The_Chainsmokers']['genre'] = POP;
    demo['The_Chainsmokers']['discovery'] = ON_MY_OWN_OTHER;
    demo['The_Chainsmokers']['Seen_Live'] = False;
    demo['The_Chainsmokers']['Kimi'] = False;
    
    demo['Lany'] = dict()
    demo['Lany']['Male'] = True; 
    demo['Lany']['POC'] = False;
    demo['Lany']['country'] = USA;
    demo['Lany']['genre'] = POP;
    demo['Lany']['discovery'] = ON_MY_OWN_CONCERT;
    demo['Lany']['Seen_Live'] = True;
    demo['Lany']['Kimi'] = False;

    demo['Genesis_Owusu'] = dict()
    demo['Genesis_Owusu']['Male'] = True; 
    demo['Genesis_Owusu']['POC'] = True;
    demo['Genesis_Owusu']['country'] = AUSTRALIA; #australian is british
    demo['Genesis_Owusu']['genre'] = INDIE;
    demo['Genesis_Owusu']['discovery'] = ON_MY_OWN_CONCERT;
    demo['Genesis_Owusu']['Seen_Live'] = True;
    demo['Genesis_Owusu']['Kimi'] = False;
    
    demo['The_Wombats'] = dict()
    demo['The_Wombats']['Male'] = True; 
    demo['The_Wombats']['POC'] = False;
    demo['The_Wombats']['country'] = ENGLAND;
    demo['The_Wombats']['genre'] = INDIE;
    demo['The_Wombats']['discovery'] = BRIAN;
    demo['The_Wombats']['Seen_Live'] = False;
    demo['The_Wombats']['Kimi'] = False;
    
    demo['Jaime_xx'] = dict()
    demo['Jaime_xx']['Male'] = True; 
    demo['Jaime_xx']['POC'] = False;
    demo['Jaime_xx']['country'] = ENGLAND;
    demo['Jaime_xx']['genre'] = INDIE;
    demo['Jaime_xx']['discovery'] = BRIAN;
    demo['Jaime_xx']['Seen_Live'] = False;
    demo['Jaime_xx']['Kimi'] = False;
    
    demo['Yeah_Yeah_Yeahs'] = dict()
    demo['Yeah_Yeah_Yeahs']['Male'] = False; 
    demo['Yeah_Yeah_Yeahs']['POC'] = False;
    demo['Yeah_Yeah_Yeahs']['country'] = USA;
    demo['Yeah_Yeah_Yeahs']['genre'] = INDIE;
    demo['Yeah_Yeah_Yeahs']['Seen_Live'] = True;
    demo['Yeah_Yeah_Yeahs']['discovery'] = OLD_DAYS;
    demo['Yeah_Yeah_Yeahs']['Kimi'] = False;
    
    demo['MYSS_KETA'] = dict()
    demo['MYSS_KETA']['Male'] = False; 
    demo['MYSS_KETA']['POC'] = False;
    demo['MYSS_KETA']['country'] = USA;
    demo['MYSS_KETA']['genre'] = POP;
    demo['MYSS_KETA']['discovery'] = ON_MY_OWN_TV;
    demo['MYSS_KETA']['Seen_Live'] = False;
    demo['MYSS_KETA']['Kimi'] = False;
    
    demo['Toro_y_Moi'] = dict()
    demo['Toro_y_Moi']['Male'] = True; 
    demo['Toro_y_Moi']['POC'] = True;
    demo['Toro_y_Moi']['country'] = USA;
    demo['Toro_y_Moi']['genre'] = POP;
    demo['Toro_y_Moi']['discovery'] = ON_MY_OWN_CONCERT;
    demo['Toro_y_Moi']['Seen_Live'] = True;
    demo['Toro_y_Moi']['Kimi'] = True;
    
    demo['Born_Ruffians'] = dict()
    demo['Born_Ruffians']['Male'] = True; 
    demo['Born_Ruffians']['POC'] = False;
    demo['Born_Ruffians']['country'] = CANADA;
    demo['Born_Ruffians']['genre'] = INDIE;
    demo['Born_Ruffians']['discovery'] = OLD_DAYS;
    demo['Born_Ruffians']['Seen_Live'] = False;
    demo['Born_Ruffians']['Kimi'] = False;
    
    demo['Streetlight_Manifesto'] = dict()
    demo['Streetlight_Manifesto']['Male'] = True; 
    demo['Streetlight_Manifesto']['POC'] = False;
    demo['Streetlight_Manifesto']['country'] = USA;
    demo['Streetlight_Manifesto']['genre'] = EMO;
    demo['Streetlight_Manifesto']['discovery'] = MUSIC_LEAGUE; #music league
    demo['Streetlight_Manifesto']['Seen_Live'] = False;
    demo['Streetlight_Manifesto']['Kimi'] = False;
    
    demo['Fred_Again'] = dict()
    demo['Fred_Again']['Male'] = True; 
    demo['Fred_Again']['POC'] = False;
    demo['Fred_Again']['country'] = ENGLAND;
    demo['Fred_Again']['genre'] = POP;
    demo['Fred_Again']['discovery'] = ON_MY_OWN_CONCERT; #Found while researching 070 shake
    demo['Fred_Again']['Seen_Live'] = False;
    demo['Fred_Again']['Kimi'] = True;
    
    demo['boygenius'] = dict()
    demo['boygenius']['Male'] = False; 
    demo['boygenius']['POC'] = False;
    demo['boygenius']['country'] = USA;
    demo['boygenius']['genre'] = INDIE;
    demo['boygenius']['discovery'] = ON_MY_OWN_CONCERT;
    demo['boygenius']['Seen_Live'] = True;
    demo['boygenius']['Kimi'] = False;
    
    demo['O70_Shake'] = dict()
    demo['O70_Shake']['Male'] = False; 
    demo['O70_Shake']['POC'] = True;
    demo['O70_Shake']['country'] = USA;
    demo['O70_Shake']['genre'] = HIPHOP;
    demo['O70_Shake']['discovery'] = KIMI;
    demo['O70_Shake']['Seen_Live'] = True;
    demo['O70_Shake']['Kimi'] = True;
    
    demo['Muse'] = dict()
    demo['Muse']['Male'] = True; 
    demo['Muse']['POC'] = False;
    demo['Muse']['country'] = ENGLAND;
    demo['Muse']['genre'] = INDIE;
    demo['Muse']['discovery'] = OLD_DAYS;
    demo['Muse']['Seen_Live'] = True;
    demo['Muse']['Kimi'] = False;
    
    demo['Nine_Inch_Nails'] = dict()
    demo['Nine_Inch_Nails']['Male'] = True; 
    demo['Nine_Inch_Nails']['POC'] = False;
    demo['Nine_Inch_Nails']['country'] = USA;
    demo['Nine_Inch_Nails']['genre'] = OLD;
    demo['Nine_Inch_Nails']['discovery'] = MUSIC_LEAGUE;  #music league
    demo['Nine_Inch_Nails']['Seen_Live'] = False;
    demo['Nine_Inch_Nails']['Kimi'] = False;
    
    demo['Siames'] = dict()
    demo['Siames']['Male'] = True; 
    demo['Siames']['POC'] = True;
    demo['Siames']['country'] = USA; #Argentenian
    demo['Siames']['genre'] = POP;
    demo['Siames']['discovery'] = MUSIC_LEAGUE; #music league
    demo['Siames']['Seen_Live'] = False;
    demo['Siames']['Kimi'] = True;
    
    demo['Hard_Fi'] = dict()
    demo['Hard_Fi']['Male'] = True; 
    demo['Hard_Fi']['POC'] = False;
    demo['Hard_Fi']['country'] = ENGLAND;
    demo['Hard_Fi']['genre'] = INDIE;
    demo['Hard_Fi']['discovery'] = OLD_DAYS;
    demo['Hard_Fi']['Seen_Live'] = False;
    demo['Hard_Fi']['Kimi'] = False;
    
    demo['Dan_Deacon'] = dict()
    demo['Dan_Deacon']['Male'] = True; 
    demo['Dan_Deacon']['POC'] = False;
    demo['Dan_Deacon']['country'] = USA;
    demo['Dan_Deacon']['genre'] = INDIE;
    demo['Dan_Deacon']['discovery'] = MUSIC_LEAGUE;
    demo['Dan_Deacon']['Seen_Live'] = False;
    demo['Dan_Deacon']['Kimi'] = False;
    
    demo['Tengger_Cavalry'] = dict()
    demo['Tengger_Cavalry']['Male'] = True; 
    demo['Tengger_Cavalry']['POC'] = True;
    demo['Tengger_Cavalry']['country'] = MONGOLIA;
    demo['Tengger_Cavalry']['genre'] = INDIE; #wtf genre is this, I don't have an "other"...maybe I need?
    demo['Tengger_Cavalry']['discovery'] = MUSIC_LEAGUE;
    demo['Tengger_Cavalry']['Seen_Live'] = False;
    demo['Tengger_Cavalry']['Kimi'] = False;
    
    demo['Britney_Spears'] = dict()
    demo['Britney_Spears']['Male'] = False; 
    demo['Britney_Spears']['POC'] = False;
    demo['Britney_Spears']['country'] = USA;
    demo['Britney_Spears']['genre'] = POP;
    demo['Britney_Spears']['discovery'] = ON_MY_OWN_OTHER;  #tiktok
    demo['Britney_Spears']['Seen_Live'] = False;
    demo['Britney_Spears']['Kimi'] = False;
    
    demo['Armor_for_Sleep'] = dict()
    demo['Armor_for_Sleep']['Male'] = True; 
    demo['Armor_for_Sleep']['POC'] = False;
    demo['Armor_for_Sleep']['country'] = USA;
    demo['Armor_for_Sleep']['genre'] = EMO;
    demo['Armor_for_Sleep']['discovery'] = ON_MY_OWN_EMO;
    demo['Armor_for_Sleep']['Seen_Live'] = True;
    demo['Armor_for_Sleep']['Kimi'] = False;
    
    demo['The_Fall_Troy'] = dict()
    demo['The_Fall_Troy']['Male'] = True; 
    demo['The_Fall_Troy']['POC'] = False;
    demo['The_Fall_Troy']['country'] = USA;
    demo['The_Fall_Troy']['genre'] = EMO;
    demo['The_Fall_Troy']['discovery'] = ON_MY_OWN_EMO;
    demo['The_Fall_Troy']['Seen_Live'] = False;
    demo['The_Fall_Troy']['Kimi'] = False;
    
    demo['Nova_Twins'] = dict()
    demo['Nova_Twins']['Male'] = False; 
    demo['Nova_Twins']['POC'] = True;
    demo['Nova_Twins']['country'] = ENGLAND;
    demo['Nova_Twins']['genre'] = EMO;
    demo['Nova_Twins']['discovery'] = BRIAN;
    demo['Nova_Twins']['Seen_Live'] = False;
    demo['Nova_Twins']['Kimi'] = False;
    
    demo['Caroline_Rose'] = dict()
    demo['Caroline_Rose']['Male'] = False; 
    demo['Caroline_Rose']['POC'] = False;
    demo['Caroline_Rose']['country'] = USA;
    demo['Caroline_Rose']['genre'] = INDIE;
    demo['Caroline_Rose']['discovery'] = KIMI;
    demo['Caroline_Rose']['Seen_Live'] = True;
    demo['Caroline_Rose']['Kimi'] = True;
    
    demo['Finch'] = dict()
    demo['Finch']['Male'] = True; 
    demo['Finch']['POC'] = False;
    demo['Finch']['country'] = GERMANY;
    demo['Finch']['genre'] = POP;  #It's more like eletronic
    demo['Finch']['discovery'] = ON_MY_OWN_OTHER;
    demo['Finch']['Seen_Live'] = False;
    demo['Finch']['Kimi'] = False;
    
    demo['The_Ophelias'] = dict()
    demo['The_Ophelias']['Male'] = False; 
    demo['The_Ophelias']['POC'] = False;
    demo['The_Ophelias']['country'] = USA;
    demo['The_Ophelias']['genre'] = INDIE;  #It's more like eletronic
    demo['The_Ophelias']['discovery'] = BRIAN;
    demo['The_Ophelias']['Seen_Live'] = False;
    demo['The_Ophelias']['Kimi'] = False;
    
    demo['Linkin_Park'] = dict()
    demo['Linkin_Park']['Male'] = True; 
    demo['Linkin_Park']['POC'] = False;
    demo['Linkin_Park']['country'] = USA;
    demo['Linkin_Park']['genre'] = EMO; 
    demo['Linkin_Park']['discovery'] = ON_MY_OWN_EMO;
    demo['Linkin_Park']['Seen_Live'] = False;
    demo['Linkin_Park']['Kimi'] = False;

    demo['King_Princess'] = dict()
    demo['King_Princess']['Male'] = False; 
    demo['King_Princess']['POC'] = False;
    demo['King_Princess']['country'] = USA;
    demo['King_Princess']['genre'] = INDIE; 
    demo['King_Princess']['discovery'] = ON_MY_OWN_CONCERT;
    demo['King_Princess']['Seen_Live'] = True;
    demo['King_Princess']['Kimi'] = False;
    
    demo['Little_Dragon'] = dict()
    demo['Little_Dragon']['Male'] = False; 
    demo['Little_Dragon']['POC'] = False;
    demo['Little_Dragon']['country'] = SWEDEN; #They are swedish i think
    demo['Little_Dragon']['genre'] = INDIE; 
    demo['Little_Dragon']['discovery'] = BRIAN;
    demo['Little_Dragon']['Seen_Live'] = False;
    demo['Little_Dragon']['Kimi'] = False;
    
    demo['MGMT'] = dict()
    demo['MGMT']['Male'] = True; 
    demo['MGMT']['POC'] = False;
    demo['MGMT']['country'] = USA;
    demo['MGMT']['genre'] = INDIE; 
    demo['MGMT']['discovery'] = OLD_DAYS;
    demo['MGMT']['Seen_Live'] = True;
    demo['MGMT']['Kimi'] = False;
    
    demo['slowthai'] = dict()
    demo['slowthai']['Male'] = True; 
    demo['slowthai']['POC'] = False;
    demo['slowthai']['country'] = ENGLAND;
    demo['slowthai']['genre'] = HIPHOP; 
    demo['slowthai']['discovery'] = BRIAN;
    demo['slowthai']['Seen_Live'] = False;
    demo['slowthai']['Kimi'] = False;

    demo['The_Joy_Formidable'] = dict()
    demo['The_Joy_Formidable']['Male'] = False; 
    demo['The_Joy_Formidable']['POC'] = False;
    demo['The_Joy_Formidable']['country'] = ENGLAND;
    demo['The_Joy_Formidable']['genre'] = INDIE;
    demo['The_Joy_Formidable']['discovery'] = OLD_DAYS;
    demo['The_Joy_Formidable']['Seen_Live'] = True;
    demo['The_Joy_Formidable']['Kimi'] = False;
    
    demo['The_Knife'] = dict()
    demo['The_Knife']['Male'] = False; 
    demo['The_Knife']['POC'] = False;
    demo['The_Knife']['country'] = SWEDEN; #Swedish
    demo['The_Knife']['genre'] = INDIE;
    demo['The_Knife']['discovery'] = OLD_DAYS;
    demo['The_Knife']['Seen_Live'] = False;
    demo['The_Knife']['Kimi'] = False;

    demo['Lincoln_Park'] = dict()
    demo['Lincoln_Park']['Male'] = True; 
    demo['Lincoln_Park']['POC'] = False;
    demo['Lincoln_Park']['country'] = USA;
    demo['Lincoln_Park']['genre'] = EMO;
    demo['Lincoln_Park']['discovery'] = ON_MY_OWN_EMO;
    demo['Lincoln_Park']['Seen_Live'] = False;
    demo['Lincoln_Park']['Kimi'] = False;
    
    demo['Periphery'] = dict()
    demo['Periphery']['Male'] = True; 
    demo['Periphery']['POC'] = False;
    demo['Periphery']['country'] = USA;
    demo['Periphery']['genre'] = EMO;
    demo['Periphery']['discovery'] = ON_MY_OWN_OTHER;  #Chris...I don't have a category for other friends ha ha
    demo['Periphery']['Seen_Live'] = False;
    demo['Periphery']['Kimi'] = False;
    
    demo['Slipknot'] = dict()
    demo['Slipknot']['Male'] = True; 
    demo['Slipknot']['POC'] = False;
    demo['Slipknot']['country'] = USA;
    demo['Slipknot']['genre'] = EMO;
    demo['Slipknot']['discovery'] = ON_MY_OWN_EMO;
    demo['Slipknot']['Seen_Live'] = False;
    demo['Slipknot']['Kimi'] = False;
    
    demo['Origami_Angel'] = dict()
    demo['Origami_Angel']['Male'] = True; 
    demo['Origami_Angel']['POC'] = False;
    demo['Origami_Angel']['country'] = USA;
    demo['Origami_Angel']['genre'] = EMO;
    demo['Origami_Angel']['discovery'] = BRIAN;
    demo['Origami_Angel']['Seen_Live'] = False;
    demo['Origami_Angel']['Kimi'] = False;
    
    demo['Little_Big'] = dict()
    demo['Little_Big']['Male'] = True; 
    demo['Little_Big']['POC'] = False;
    demo['Little_Big']['country'] = RUSSIA;
    demo['Little_Big']['genre'] = POP;
    demo['Little_Big']['discovery'] = ON_MY_OWN_TV;
    demo['Little_Big']['Seen_Live'] = False;
    demo['Little_Big']['Kimi'] = False;
    
    demo['Voxtrot'] = dict()
    demo['Voxtrot']['Male'] = True; 
    demo['Voxtrot']['POC'] = False;
    demo['Voxtrot']['country'] = USA;
    demo['Voxtrot']['genre'] = INDIE;
    demo['Voxtrot']['discovery'] = OLD_DAYS;
    demo['Voxtrot']['Seen_Live'] = False;
    demo['Voxtrot']['Kimi'] = False;
    
    demo['Model_Actriz'] = dict()
    demo['Model_Actriz']['Male'] = True; 
    demo['Model_Actriz']['POC'] = False;
    demo['Model_Actriz']['country'] = USA;
    demo['Model_Actriz']['genre'] = EMO;
    demo['Model_Actriz']['discovery'] = BRIAN;
    demo['Model_Actriz']['Seen_Live'] = False;
    demo['Model_Actriz']['Kimi'] = False;
    
    demo['Defeater'] = dict()
    demo['Defeater']['Male'] = True; 
    demo['Defeater']['POC'] = False;
    demo['Defeater']['country'] = USA;
    demo['Defeater']['genre'] = EMO;
    demo['Defeater']['discovery'] = ON_MY_OWN_OTHER; #jordan's friend with the leather jacket
    demo['Defeater']['Seen_Live'] = False;
    demo['Defeater']['Kimi'] = False;
    
    demo['Thundercat'] = dict()
    demo['Thundercat']['Male'] = True; 
    demo['Thundercat']['POC'] = True;
    demo['Thundercat']['country'] = USA;
    demo['Thundercat']['genre'] = POP;
    demo['Thundercat']['discovery'] = KIMI;
    demo['Thundercat']['Seen_Live'] = False;
    demo['Thundercat']['Kimi'] = True;
    
    demo['A_Tribe_Called_Quest'] = dict()
    demo['A_Tribe_Called_Quest']['Male'] = True; 
    demo['A_Tribe_Called_Quest']['POC'] = True;
    demo['A_Tribe_Called_Quest']['country'] = USA;
    demo['A_Tribe_Called_Quest']['genre'] = HIPHOP;
    demo['A_Tribe_Called_Quest']['discovery'] = ON_MY_OWN_TV;
    demo['A_Tribe_Called_Quest']['Seen_Live'] = False;
    demo['A_Tribe_Called_Quest']['Kimi'] = False;
    
    demo['Fall_Out_BOy'] = dict()
    demo['Fall_Out_BOy']['Male'] = True; 
    demo['Fall_Out_BOy']['POC'] = False;
    demo['Fall_Out_BOy']['country'] = USA;
    demo['Fall_Out_BOy']['genre'] = EMO;
    demo['Fall_Out_BOy']['discovery'] = KIMI;
    demo['Fall_Out_BOy']['Seen_Live'] = False;
    demo['Fall_Out_BOy']['Kimi'] = True;
    
    demo['Geese'] = dict()
    demo['Geese']['Male'] = True; 
    demo['Geese']['POC'] = False;
    demo['Geese']['country'] = USA;
    demo['Geese']['genre'] = INDIE;
    demo['Geese']['discovery'] = BRIAN;
    demo['Geese']['Seen_Live'] = False;
    demo['Geese']['Kimi'] = False;
    
    demo['Foushee'] = dict()
    demo['Foushee']['Male'] = False; 
    demo['Foushee']['POC'] = True;
    demo['Foushee']['country'] = USA;
    demo['Foushee']['genre'] = HIPHOP;
    demo['Foushee']['discovery'] = ON_MY_OWN_CONCERT;
    demo['Foushee']['Seen_Live'] = True;
    demo['Foushee']['Kimi'] = False;
    
    demo['Raye'] = dict()
    demo['Raye']['Male'] = False; 
    demo['Raye']['POC'] = True;
    demo['Raye']['country'] = USA;
    demo['Raye']['genre'] = INDIE;
    demo['Raye']['discovery'] = KIMI;
    demo['Raye']['Seen_Live'] = True;
    demo['Raye']['Kimi'] = True;
    
    demo['A_Day_To_Remember'] = dict()
    demo['A_Day_To_Remember']['Male'] = True; 
    demo['A_Day_To_Remember']['POC'] = False;
    demo['A_Day_To_Remember']['country'] = USA;
    demo['A_Day_To_Remember']['genre'] = EMO;
    demo['A_Day_To_Remember']['discovery'] = MUSIC_LEAGUE;
    demo['A_Day_To_Remember']['Seen_Live'] = False;
    demo['A_Day_To_Remember']['Kimi'] = False;
    
    demo['Hail_the_Sun'] = dict()
    demo['Hail_the_Sun']['Male'] = True; 
    demo['Hail_the_Sun']['POC'] = False;
    demo['Hail_the_Sun']['country'] = USA;
    demo['Hail_the_Sun']['genre'] = EMO;
    demo['Hail_the_Sun']['discovery'] = ON_MY_OWN_OTHER;  #Chris...I don't have a category for other friends ha ha
    demo['Hail_the_Sun']['Seen_Live'] = True;
    demo['Hail_the_Sun']['Kimi'] = False;
    
    demo['Three_Days_Grace'] = dict()
    demo['Three_Days_Grace']['Male'] = True; 
    demo['Three_Days_Grace']['POC'] = False;
    demo['Three_Days_Grace']['country'] = USA;
    demo['Three_Days_Grace']['genre'] = EMO;
    demo['Three_Days_Grace']['discovery'] = ON_MY_OWN_EMO;
    demo['Three_Days_Grace']['Seen_Live'] = False;
    demo['Three_Days_Grace']['Kimi'] = False;
    
    demo['The_Used'] = dict()
    demo['The_Used']['Male'] = True; 
    demo['The_Used']['POC'] = False;
    demo['The_Used']['country'] = USA;
    demo['The_Used']['genre'] = EMO;
    demo['The_Used']['discovery'] = MUSIC_LEAGUE;
    demo['The_Used']['Seen_Live'] = False;
    demo['The_Used']['Kimi'] = False;
    
    demo['Girl_Scout'] = dict()
    demo['Girl_Scout']['Male'] = False; 
    demo['Girl_Scout']['POC'] = False;
    demo['Girl_Scout']['country'] = USA;
    demo['Girl_Scout']['genre'] = INDIE;
    demo['Girl_Scout']['discovery'] = BRIAN;
    demo['Girl_Scout']['Seen_Live'] = False;
    demo['Girl_Scout']['Kimi'] = False;
    
    demo['Fall_Out_Boy'] = dict()
    demo['Fall_Out_Boy']['Male'] = True; 
    demo['Fall_Out_Boy']['POC'] = False;
    demo['Fall_Out_Boy']['country'] = USA;
    demo['Fall_Out_Boy']['genre'] = EMO;
    demo['Fall_Out_Boy']['discovery'] = KIMI;
    demo['Fall_Out_Boy']['Seen_Live'] = False;
    demo['Fall_Out_Boy']['Kimi'] = True;
    
    demo['Frank_Zappa'] = dict()
    demo['Frank_Zappa']['Male'] = True; 
    demo['Frank_Zappa']['POC'] = False;
    demo['Frank_Zappa']['country'] = USA;
    demo['Frank_Zappa']['genre'] = OLD;
    demo['Frank_Zappa']['discovery'] = MUSIC_LEAGUE; #Geoff
    demo['Frank_Zappa']['Seen_Live'] = False;
    demo['Frank_Zappa']['Kimi'] = False;
    
    demo['Lake_Street_Dive'] = dict()
    demo['Lake_Street_Dive']['Male'] = False; 
    demo['Lake_Street_Dive']['POC'] = False;
    demo['Lake_Street_Dive']['country'] = USA;
    demo['Lake_Street_Dive']['genre'] = INDIE;
    demo['Lake_Street_Dive']['discovery'] = MUSIC_LEAGUE;
    demo['Lake_Street_Dive']['Seen_Live'] = False;
    demo['Lake_Street_Dive']['Kimi'] = False;
    
    demo['Lynks'] = dict()
    demo['Lynks']['Male'] = True; 
    demo['Lynks']['POC'] = False;
    demo['Lynks']['country'] = ENGLAND;
    demo['Lynks']['genre'] = INDIE;
    demo['Lynks']['discovery'] = BRIAN;
    demo['Lynks']['Seen_Live'] = False;
    demo['Lynks']['Kimi'] = False;
    
    demo['Jens_Lekman'] = dict()
    demo['Jens_Lekman']['Male'] = True; 
    demo['Jens_Lekman']['POC'] = False;
    demo['Jens_Lekman']['country'] = SWEDEN;
    demo['Jens_Lekman']['genre'] = INDIE;
    demo['Jens_Lekman']['discovery'] = MUSIC_LEAGUE;
    demo['Jens_Lekman']['Seen_Live'] = False;
    demo['Jens_Lekman']['Kimi'] = False;
    
    demo['Mandy_Moore'] = dict()
    demo['Mandy_Moore']['Male'] = False; 
    demo['Mandy_Moore']['POC'] = False;
    demo['Mandy_Moore']['country'] = USA;
    demo['Mandy_Moore']['genre'] = POP;
    demo['Mandy_Moore']['discovery'] = MUSIC_LEAGUE;
    demo['Mandy_Moore']['Seen_Live'] = False;
    demo['Mandy_Moore']['Kimi'] = True;
    
    demo['Alexisonfire'] = dict()
    demo['Alexisonfire']['Male'] = True; 
    demo['Alexisonfire']['POC'] = False;
    demo['Alexisonfire']['country'] = CANADA;
    demo['Alexisonfire']['genre'] = EMO;
    demo['Alexisonfire']['discovery'] = ON_MY_OWN_EMO; #Adi at emo night
    demo['Alexisonfire']['Seen_Live'] = False;
    demo['Alexisonfire']['Kimi'] = False;
    
    demo['Underoath'] = dict()
    demo['Underoath']['Male'] = True; 
    demo['Underoath']['POC'] = False;
    demo['Underoath']['country'] = USA;
    demo['Underoath']['genre'] = EMO;
    demo['Underoath']['discovery'] = ON_MY_OWN_EMO;  #emo night
    demo['Underoath']['Seen_Live'] = False;
    demo['Underoath']['Kimi'] = False;
    
    demo['Thank_You_Scientist'] = dict()
    demo['Thank_You_Scientist']['Male'] = True; 
    demo['Thank_You_Scientist']['POC'] = False;
    demo['Thank_You_Scientist']['country'] = USA;
    demo['Thank_You_Scientist']['genre'] = INDIE;
    demo['Thank_You_Scientist']['discovery'] = MUSIC_LEAGUE; #Chris!
    demo['Thank_You_Scientist']['Seen_Live'] = False;
    demo['Thank_You_Scientist']['Kimi'] = False;
    
    demo['Blood_Orange'] = dict()
    demo['Blood_Orange']['Male'] = True; 
    demo['Blood_Orange']['POC'] = True;
    demo['Blood_Orange']['country'] = ENGLAND;
    demo['Blood_Orange']['genre'] = INDIE;
    demo['Blood_Orange']['discovery'] = MUSIC_LEAGUE;
    demo['Blood_Orange']['Seen_Live'] = False;
    demo['Blood_Orange']['Kimi'] = True;
    
    demo['Sleep_Token'] = dict()
    demo['Sleep_Token']['Male'] = True; 
    demo['Sleep_Token']['POC'] = False;
    demo['Sleep_Token']['country'] = ENGLAND;
    demo['Sleep_Token']['genre'] = EMO;
    demo['Sleep_Token']['discovery'] = ON_MY_OWN_OTHER;  #Chris!
    demo['Sleep_Token']['Seen_Live'] = False;
    demo['Sleep_Token']['Kimi'] = False;
    
    demo['Christine_and_the_Queens'] = dict()
    demo['Christine_and_the_Queens']['Male'] = False; 
    demo['Christine_and_the_Queens']['POC'] = False;
    demo['Christine_and_the_Queens']['country'] = FRANCE;
    demo['Christine_and_the_Queens']['genre'] = INDIE;
    demo['Christine_and_the_Queens']['discovery'] = BRIAN;
    demo['Christine_and_the_Queens']['Seen_Live'] = False;
    demo['Christine_and_the_Queens']['Kimi'] = True;
    
    demo['The_Naked_and_the_Famous'] = dict()
    demo['The_Naked_and_the_Famous']['Male'] = False; 
    demo['The_Naked_and_the_Famous']['POC'] = False;
    demo['The_Naked_and_the_Famous']['country'] = NEW_ZEALAND;
    demo['The_Naked_and_the_Famous']['genre'] = INDIE;
    demo['The_Naked_and_the_Famous']['discovery'] = OLD_DAYS;
    demo['The_Naked_and_the_Famous']['Seen_Live'] = False;
    demo['The_Naked_and_the_Famous']['Kimi'] = False;
    
    demo['Five_for_Fighting'] = dict()
    demo['Five_for_Fighting']['Male'] = True; 
    demo['Five_for_Fighting']['POC'] = False;
    demo['Five_for_Fighting']['country'] = USA;
    demo['Five_for_Fighting']['genre'] = POP;
    demo['Five_for_Fighting']['discovery'] = OLD_DAYS;
    demo['Five_for_Fighting']['Seen_Live'] = False;
    demo['Five_for_Fighting']['Kimi'] = False;
    
    demo['Kavinsky'] = dict()
    demo['Kavinsky']['Male'] = True; 
    demo['Kavinsky']['POC'] = False;
    demo['Kavinsky']['country'] = FRANCE;
    demo['Kavinsky']['genre'] = INDIE;
    demo['Kavinsky']['discovery'] = MUSIC_LEAGUE;
    demo['Kavinsky']['Seen_Live'] = False;
    demo['Kavinsky']['Kimi'] = False;
    
    demo['Kelela'] = dict()
    demo['Kelela']['Male'] = False; 
    demo['Kelela']['POC'] = True;
    demo['Kelela']['country'] = USA;
    demo['Kelela']['genre'] = R_AND_B;
    demo['Kelela']['discovery'] = KIMI; #Also a rando on OKCupid
    demo['Kelela']['Seen_Live'] = False;
    demo['Kelela']['Kimi'] = True;
    
    demo['Beirut'] = dict()
    demo['Beirut']['Male'] = True; 
    demo['Beirut']['POC'] = False;
    demo['Beirut']['country'] = INDIE;
    demo['Beirut']['genre'] = R_AND_B;
    demo['Beirut']['discovery'] = OLD_DAYS;
    demo['Beirut']['Seen_Live'] = False;
    demo['Beirut']['Kimi'] = False;
    
    demo['Sebastien_Tellier'] = dict()
    demo['Sebastien_Tellier']['Male'] = True; 
    demo['Sebastien_Tellier']['POC'] = False;
    demo['Sebastien_Tellier']['country'] = FRANCE;
    demo['Sebastien_Tellier']['genre'] = INDIE;
    demo['Sebastien_Tellier']['discovery'] = ON_MY_OWN_OTHER;
    demo['Sebastien_Tellier']['Seen_Live'] = False;
    demo['Sebastien_Tellier']['Kimi'] = True;
    
    demo['Malik_Djoudi'] = dict()
    demo['Malik_Djoudi']['Male'] = True; 
    demo['Malik_Djoudi']['POC'] = False;
    demo['Malik_Djoudi']['country'] = FRANCE;
    demo['Malik_Djoudi']['genre'] = INDIE;
    demo['Malik_Djoudi']['discovery'] = ON_MY_OWN_OTHER;
    demo['Malik_Djoudi']['Seen_Live'] = False;
    demo['Malik_Djoudi']['Kimi'] = True;
   
    demo['Carly_Cosgrove'] = dict()
    demo['Carly_Cosgrove']['Male'] = True; 
    demo['Carly_Cosgrove']['POC'] = False;
    demo['Carly_Cosgrove']['country'] = USA;
    demo['Carly_Cosgrove']['genre'] = EMO;
    demo['Carly_Cosgrove']['discovery'] = ON_MY_OWN_EMO;
    demo['Carly_Cosgrove']['Seen_Live'] = False;
    demo['Carly_Cosgrove']['Kimi'] = False;
    
    demo['LA_Priest'] = dict()
    demo['LA_Priest']['Male'] = True; 
    demo['LA_Priest']['POC'] = False;
    demo['LA_Priest']['country'] = ENGLAND;
    demo['LA_Priest']['genre'] = INDIE;
    demo['LA_Priest']['discovery'] = ON_MY_OWN_OTHER;
    demo['LA_Priest']['Seen_Live'] = False;
    demo['LA_Priest']['Kimi'] = True;
    
    demo['Freelance_Whales'] = dict()
    demo['Freelance_Whales']['Male'] = True; 
    demo['Freelance_Whales']['POC'] = False;
    demo['Freelance_Whales']['country'] = USA;
    demo['Freelance_Whales']['genre'] = INDIE;
    demo['Freelance_Whales']['discovery'] = OLD_DAYS;
    demo['Freelance_Whales']['Seen_Live'] = True;
    demo['Freelance_Whales']['Kimi'] = False;
    
    demo['Asking_Alexandria'] = dict()
    demo['Asking_Alexandria']['Male'] = True; 
    demo['Asking_Alexandria']['POC'] = False;
    demo['Asking_Alexandria']['country'] = ENGLAND;
    demo['Asking_Alexandria']['genre'] = EMO;
    demo['Asking_Alexandria']['discovery'] = ON_MY_OWN_EMO;
    demo['Asking_Alexandria']['Seen_Live'] = False;
    demo['Asking_Alexandria']['Kimi'] = False;
    
    demo['Nick_Lutsko'] = dict()
    demo['Nick_Lutsko']['Male'] = True; 
    demo['Nick_Lutsko']['POC'] = False;
    demo['Nick_Lutsko']['country'] = USA;
    demo['Nick_Lutsko']['genre'] = INDIE;
    demo['Nick_Lutsko']['discovery'] = MUSIC_LEAGUE;
    demo['Nick_Lutsko']['Seen_Live'] = False;
    demo['Nick_Lutsko']['Kimi'] = False;
    
    demo['Alice_Longyu_Gao'] = dict()
    demo['Alice_Longyu_Gao']['Male'] = False; 
    demo['Alice_Longyu_Gao']['POC'] = True;
    demo['Alice_Longyu_Gao']['country'] = CHINA;
    demo['Alice_Longyu_Gao']['genre'] = POP;
    demo['Alice_Longyu_Gao']['discovery'] = KIMI; #Rich bitch juice
    demo['Alice_Longyu_Gao']['Seen_Live'] = False;
    demo['Alice_Longyu_Gao']['Kimi'] = True;
    
    demo['Stellar_Circuits'] = dict()
    demo['Stellar_Circuits']['Male'] = True; 
    demo['Stellar_Circuits']['POC'] = False;
    demo['Stellar_Circuits']['country'] = USA;
    demo['Stellar_Circuits']['genre'] = EMO;  #Metal really
    demo['Stellar_Circuits']['discovery'] = ON_MY_OWN_OTHER; #Chris
    demo['Stellar_Circuits']['Seen_Live'] = False;
    demo['Stellar_Circuits']['Kimi'] = False;
    
    demo['Currents'] = dict()
    demo['Currents']['Male'] = True; 
    demo['Currents']['POC'] = False;
    demo['Currents']['country'] = USA;
    demo['Currents']['genre'] = EMO;  #Metal really
    demo['Currents']['discovery'] = MUSIC_LEAGUE; #Chris
    demo['Currents']['Seen_Live'] = False;
    demo['Currents']['Kimi'] = False;
    
    demo['Frank_Ocean'] = dict()
    demo['Frank_Ocean']['Male'] = True; 
    demo['Frank_Ocean']['POC'] = True;
    demo['Frank_Ocean']['country'] = USA;
    demo['Frank_Ocean']['genre'] = R_AND_B;
    demo['Frank_Ocean']['discovery'] = KIMI;
    demo['Frank_Ocean']['Seen_Live'] = False;
    demo['Frank_Ocean']['Kimi'] = True;
    
    demo['From_Autumn_to_Ashes'] = dict()
    demo['From_Autumn_to_Ashes']['Male'] = True; 
    demo['From_Autumn_to_Ashes']['POC'] = False;
    demo['From_Autumn_to_Ashes']['country'] = USA;
    demo['From_Autumn_to_Ashes']['genre'] = EMO;
    demo['From_Autumn_to_Ashes']['discovery'] = ON_MY_OWN_EMO;
    demo['From_Autumn_to_Ashes']['Seen_Live'] = False;
    demo['From_Autumn_to_Ashes']['Kimi'] = False;
    
    demo['Scary_Kids_Scaring_Kids'] = dict()
    demo['Scary_Kids_Scaring_Kids']['Male'] = True; 
    demo['Scary_Kids_Scaring_Kids']['POC'] = False;
    demo['Scary_Kids_Scaring_Kids']['country'] = USA;
    demo['Scary_Kids_Scaring_Kids']['genre'] = EMO;
    demo['Scary_Kids_Scaring_Kids']['discovery'] = ON_MY_OWN_EMO;
    demo['Scary_Kids_Scaring_Kids']['Seen_Live'] = False;
    demo['Scary_Kids_Scaring_Kids']['Kimi'] = False;

    demo['Princess_Nokia'] = dict()
    demo['Princess_Nokia']['Male'] = False; 
    demo['Princess_Nokia']['POC'] = True;
    demo['Princess_Nokia']['country'] = USA;
    demo['Princess_Nokia']['genre'] = HIPHOP;
    demo['Princess_Nokia']['discovery'] = MUSIC_LEAGUE;
    demo['Princess_Nokia']['Seen_Live'] = False;
    demo['Princess_Nokia']['Kimi'] = False;
    
    demo['Noah_Kahan'] = dict()
    demo['Noah_Kahan']['Male'] = True; 
    demo['Noah_Kahan']['POC'] = False;
    demo['Noah_Kahan']['country'] = USA;
    demo['Noah_Kahan']['genre'] = INDIE;  #folk really...
    demo['Noah_Kahan']['discovery'] = KIMI;
    demo['Noah_Kahan']['Seen_Live'] = False;
    demo['Noah_Kahan']['Kimi'] = True;
    
    demo['Rent'] = dict()
    demo['Rent']['Male'] = True; 
    demo['Rent']['POC'] = True;
    demo['Rent']['country'] = USA;
    demo['Rent']['genre'] = MUSICAL; 
    demo['Rent']['discovery'] = ON_MY_OWN_MUSICAL;
    demo['Rent']['Seen_Live'] = True;
    demo['Rent']['Kimi'] = False;
    
    demo['Vince_Staples'] = dict()
    demo['Vince_Staples']['Male'] = True; 
    demo['Vince_Staples']['POC'] = True;
    demo['Vince_Staples']['country'] = USA;
    demo['Vince_Staples']['genre'] = HIPHOP;  
    demo['Vince_Staples']['discovery'] = KIMI;
    demo['Vince_Staples']['Seen_Live'] = False;
    demo['Vince_Staples']['Kimi'] = True;
    
    demo['Kings_of_Convenience'] = dict()
    demo['Kings_of_Convenience']['Male'] = True; 
    demo['Kings_of_Convenience']['POC'] = False;
    demo['Kings_of_Convenience']['country'] = NORWAY;
    demo['Kings_of_Convenience']['genre'] = INDIE;
    demo['Kings_of_Convenience']['discovery'] = OLD_DAYS;
    demo['Kings_of_Convenience']['Seen_Live'] = False;
    demo['Kings_of_Convenience']['Kimi'] = False;
    
    demo['Air'] = dict()
    demo['Air']['Male'] = True; 
    demo['Air']['POC'] = False;
    demo['Air']['country'] = FRANCE;
    demo['Air']['genre'] = INDIE;
    demo['Air']['discovery'] = ON_MY_OWN_OTHER; #Erin
    demo['Air']['Seen_Live'] = False;
    demo['Air']['Kimi'] = False;

    demo['Tranda'] = dict()
    demo['Tranda']['Male'] = True; 
    demo['Tranda']['POC'] = False;
    demo['Tranda']['country'] = ROMANIA;
    demo['Tranda']['genre'] = HIPHOP;
    demo['Tranda']['discovery'] = KIMI;
    demo['Tranda']['Seen_Live'] = False;
    demo['Tranda']['Kimi'] = True;
    
    demo['Fat_Dog'] = dict()
    demo['Fat_Dog']['Male'] = True; 
    demo['Fat_Dog']['POC'] = False;
    demo['Fat_Dog']['country'] = ENGLAND;
    demo['Fat_Dog']['genre'] = INDIE;
    demo['Fat_Dog']['discovery'] = BRIAN;
    demo['Fat_Dog']['Seen_Live'] = False;
    demo['Fat_Dog']['Kimi'] = False;
    
    demo['Denzel_Curry'] = dict()
    demo['Denzel_Curry']['Male'] = True; 
    demo['Denzel_Curry']['POC'] = True;
    demo['Denzel_Curry']['country'] = USA;
    demo['Denzel_Curry']['genre'] = HIPHOP;
    demo['Denzel_Curry']['discovery'] = KIMI;
    demo['Denzel_Curry']['Seen_Live'] = False;
    demo['Denzel_Curry']['Kimi'] = True;
    
    demo['Justice'] = dict()
    demo['Justice']['Male'] = True; 
    demo['Justice']['POC'] = False;
    demo['Justice']['country'] = FRANCE;
    demo['Justice']['genre'] = INDIE;
    demo['Justice']['discovery'] = KIMI;
    demo['Justice']['Seen_Live'] = False;
    demo['Justice']['Kimi'] = True;
    
    demo['Space_Weather'] = dict()
    demo['Space_Weather']['Male'] = True; 
    demo['Space_Weather']['POC'] = False;
    demo['Space_Weather']['country'] = USA;
    demo['Space_Weather']['genre'] = EMO;
    demo['Space_Weather']['discovery'] = ON_MY_OWN_EMO; #spencer
    demo['Space_Weather']['Seen_Live'] = False;
    demo['Space_Weather']['Kimi'] = False;
        
    demo['Gorillaz'] = dict()
    demo['Gorillaz']['Male'] = True; 
    demo['Gorillaz']['POC'] = False;
    demo['Gorillaz']['country'] = ENGLAND;
    demo['Gorillaz']['genre'] = INDIE;
    demo['Gorillaz']['discovery'] = OLD_DAYS;
    demo['Gorillaz']['Seen_Live'] = False;
    demo['Gorillaz']['Kimi'] = False;
    
    demo['Jakey'] = dict()
    demo['Jakey']['Male'] = True; 
    demo['Jakey']['POC'] = False;
    demo['Jakey']['country'] = USA;
    demo['Jakey']['genre'] = HIPHOP;
    demo['Jakey']['discovery'] = MUSIC_LEAGUE;
    demo['Jakey']['Seen_Live'] = False;
    demo['Jakey']['Kimi'] = False;
    
    demo['Megan_Thee_Stallion'] = dict()
    demo['Megan_Thee_Stallion']['Male'] = False; 
    demo['Megan_Thee_Stallion']['POC'] = True;
    demo['Megan_Thee_Stallion']['country'] = USA;
    demo['Megan_Thee_Stallion']['genre'] = HIPHOP;
    demo['Megan_Thee_Stallion']['discovery'] = KIMI;
    demo['Megan_Thee_Stallion']['Seen_Live'] = False;
    demo['Megan_Thee_Stallion']['Kimi'] = True;
    
    demo['FKA_Twigs'] = dict()
    demo['FKA_Twigs']['Male'] = False; 
    demo['FKA_Twigs']['POC'] = True;
    demo['FKA_Twigs']['country'] = ENGLAND;
    demo['FKA_Twigs']['genre'] = R_AND_B;
    demo['FKA_Twigs']['discovery'] = MUSIC_LEAGUE;
    demo['FKA_Twigs']['Seen_Live'] = False;
    demo['FKA_Twigs']['Kimi'] = True;
    
    demo['Bag_Raiders'] = dict()
    demo['Bag_Raiders']['Male'] = True; 
    demo['Bag_Raiders']['POC'] = False;
    demo['Bag_Raiders']['country'] = AUSTRALIA;
    demo['Bag_Raiders']['genre'] = INDIE;
    demo['Bag_Raiders']['discovery'] = ON_MY_OWN_OTHER; #TORO did a cover...
    demo['Bag_Raiders']['Seen_Live'] = False;
    demo['Bag_Raiders']['Kimi'] = True;
    
    demo['Anna_Meredith'] = dict()
    demo['Anna_Meredith']['Male'] = False; 
    demo['Anna_Meredith']['POC'] = False;
    demo['Anna_Meredith']['country'] = ENGLAND;
    demo['Anna_Meredith']['genre'] = INDIE;
    demo['Anna_Meredith']['discovery'] = BRIAN; 
    demo['Anna_Meredith']['Seen_Live'] = False;
    demo['Anna_Meredith']['Kimi'] = False;
    
    demo['Julian_Plenti'] = dict()
    demo['Julian_Plenti']['Male'] = True; 
    demo['Julian_Plenti']['POC'] = False;
    demo['Julian_Plenti']['country'] = USA;
    demo['Julian_Plenti']['genre'] = INDIE;
    demo['Julian_Plenti']['discovery'] = OLD_DAYS; 
    demo['Julian_Plenti']['Seen_Live'] = False;
    demo['Julian_Plenti']['Kimi'] = False;
    
    demo['Hugh_Jackman'] = dict()
    demo['Hugh_Jackman']['Male'] = True; 
    demo['Hugh_Jackman']['POC'] = False;
    demo['Hugh_Jackman']['country'] = AUSTRALIA;
    demo['Hugh_Jackman']['genre'] = MUSICAL;
    demo['Hugh_Jackman']['discovery'] = ON_MY_OWN_MUSICAL; 
    demo['Hugh_Jackman']['Seen_Live'] = False;
    demo['Hugh_Jackman']['Kimi'] = False;
    
    demo['Fun'] = dict()
    demo['Fun']['Male'] = True; 
    demo['Fun']['POC'] = False;
    demo['Fun']['country'] = USA;
    demo['Fun']['genre'] = INDIE;
    demo['Fun']['discovery'] = OLD_DAYS; 
    demo['Fun']['Seen_Live'] = True;
    demo['Fun']['Kimi'] = False;
    
    demo['ROSALIA'] = dict()
    demo['ROSALIA']['Male'] = False; 
    demo['ROSALIA']['POC'] = True;
    demo['ROSALIA']['country'] = SPAIN;
    demo['ROSALIA']['genre'] = POP; #perreo
    demo['ROSALIA']['discovery'] = ON_MY_OWN_OTHER; 
    demo['ROSALIA']['Seen_Live'] = False;
    demo['ROSALIA']['Kimi'] = False;
    
    demo['rEDOLENT'] = dict()
    demo['rEDOLENT']['Male'] = True; 
    demo['rEDOLENT']['POC'] = False;
    demo['rEDOLENT']['country'] = ENGLAND;
    demo['rEDOLENT']['genre'] = INDIE; 
    demo['rEDOLENT']['discovery'] = BRIAN; 
    demo['rEDOLENT']['Seen_Live'] = False;
    demo['rEDOLENT']['Kimi'] = False;
    
    demo['Digitalism'] = dict()
    demo['Digitalism']['Male'] = True; 
    demo['Digitalism']['POC'] = False;
    demo['Digitalism']['country'] = GERMANY;
    demo['Digitalism']['genre'] = INDIE; 
    demo['Digitalism']['discovery'] = MUSIC_LEAGUE; #a guess
    demo['Digitalism']['Seen_Live'] = False;
    demo['Digitalism']['Kimi'] = False;
    
    demo['Bronski_Beat'] = dict()
    demo['Bronski_Beat']['Male'] = True; 
    demo['Bronski_Beat']['POC'] = False;
    demo['Bronski_Beat']['country'] = ENGLAND;
    demo['Bronski_Beat']['genre'] = INDIE; 
    demo['Bronski_Beat']['discovery'] = BRIAN; 
    demo['Bronski_Beat']['Seen_Live'] = False;
    demo['Bronski_Beat']['Kimi'] = False;
    
    demo['Arca'] = dict()
    demo['Arca']['Male'] = True; 
    demo['Arca']['POC'] = True;
    demo['Arca']['country'] = VENEZUELA;
    demo['Arca']['genre'] = HIPHOP; #Latin trap · reggaeton · alternative reggaeton....doesn't fit anything!
    demo['Arca']['discovery'] = ON_MY_OWN_OTHER; #perreo awakening
    demo['Arca']['Seen_Live'] = False;
    demo['Arca']['Kimi'] = False;
    
    demo['Magdalena_Bay'] = dict()
    demo['Magdalena_Bay']['Male'] = False; 
    demo['Magdalena_Bay']['POC'] = False;
    demo['Magdalena_Bay']['country'] = USA;
    demo['Magdalena_Bay']['genre'] = INDIE; 
    demo['Magdalena_Bay']['discovery'] = ON_MY_OWN_OTHER; #Sarah
    demo['Magdalena_Bay']['Seen_Live'] = False;
    demo['Magdalena_Bay']['Kimi'] = False;
    
    demo['Princeton'] = dict()
    demo['Princeton']['Male'] = True; 
    demo['Princeton']['POC'] = False;
    demo['Princeton']['country'] = USA;
    demo['Princeton']['genre'] = INDIE; 
    demo['Princeton']['discovery'] = OLD_DAYS; 
    demo['Princeton']['Seen_Live'] = True;
    demo['Princeton']['Kimi'] = False;
    
    demo['I_Prevail'] = dict()
    demo['I_Prevail']['Male'] = True; 
    demo['I_Prevail']['POC'] = False;
    demo['I_Prevail']['country'] = USA;
    demo['I_Prevail']['genre'] = EMO; 
    demo['I_Prevail']['discovery'] = KIMI; 
    demo['I_Prevail']['Seen_Live'] = False;
    demo['I_Prevail']['Kimi'] = True;
    
    demo['Dora_Jar'] = dict()
    demo['Dora_Jar']['Male'] = False; 
    demo['Dora_Jar']['POC'] = False;
    demo['Dora_Jar']['country'] = USA;
    demo['Dora_Jar']['genre'] = INDIE; 
    demo['Dora_Jar']['discovery'] = BRIAN; 
    demo['Dora_Jar']['Seen_Live'] = True;
    demo['Dora_Jar']['Kimi'] = False;
    
    demo['Moving_Units'] = dict()
    demo['Moving_Units']['Male'] = True; 
    demo['Moving_Units']['POC'] = False;
    demo['Moving_Units']['country'] = USA;
    demo['Moving_Units']['genre'] = INDIE;
    demo['Moving_Units']['discovery'] = OLD_DAYS;
    demo['Moving_Units']['Seen_Live'] = False;
    demo['Moving_Units']['Kimi'] = False;
    
    demo['Metronomy'] = dict()
    demo['Metronomy']['Male'] = True; 
    demo['Metronomy']['POC'] = False;
    demo['Metronomy']['country'] = USA;
    demo['Metronomy']['genre'] = INDIE;
    demo['Metronomy']['discovery'] = OLD_DAYS;
    demo['Metronomy']['Seen_Live'] = False;
    demo['Metronomy']['Kimi'] = False;
    
    artistStr = 'Remi_Wolf';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = False; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = USA;
    demo[artistStr]['genre'] = INDIE;
    demo[artistStr]['discovery'] = BRIAN;
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'Roisin_Murphy';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = False; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = IRELAND;
    demo[artistStr]['genre'] = POP;
    demo[artistStr]['discovery'] = KIMI;
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = True;
    
    artistStr = 'Jack_Off_Jill';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = False; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = USA;
    demo[artistStr]['genre'] = EMO;
    demo[artistStr]['discovery'] = MUSIC_LEAGUE; #Sarah
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'Sophie_Hunter';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = False; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = USA;
    demo[artistStr]['genre'] = HIPHOP;
    demo[artistStr]['discovery'] = MUSIC_LEAGUE; #I think?
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'Ultra_Sunn';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = BELGIUM;
    demo[artistStr]['genre'] = EMO;
    demo[artistStr]['discovery'] = ON_MY_OWN_CONCERT; #Shazammed at Manray
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'Late_Again';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = USA;
    demo[artistStr]['genre'] = INDIE;
    demo[artistStr]['discovery'] = ON_MY_OWN_OTHER; #museum wandering playlist
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'Linea_Aspera';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = False; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = GERMANY;
    demo[artistStr]['genre'] = EMO;
    demo[artistStr]['discovery'] = ON_MY_OWN_CONCERT; #Shazammed at Manray
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'BAYNK';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = NEW_ZEALAND;
    demo[artistStr]['genre'] = INDIE;
    demo[artistStr]['discovery'] = ON_MY_OWN_OTHER; #instagram add
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = True;
    
    artistStr = 'MGL';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = ROMANIA;
    demo[artistStr]['genre'] = HIPHOP;
    demo[artistStr]['discovery'] = ON_MY_OWN_OTHER; #jack
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = True;
    
    artistStr = 'SASAMI';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = False; 
    demo[artistStr]['POC'] = True;
    demo[artistStr]['country'] = USA;
    demo[artistStr]['genre'] = INDIE;
    demo[artistStr]['discovery'] = BRIAN; 
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = True;
    
    artistStr = 'Maribou_State';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = ENGLAND;
    demo[artistStr]['genre'] = INDIE;
    demo[artistStr]['discovery'] = BRIAN; 
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'Parcels';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = AUSTRALIA;
    demo[artistStr]['genre'] = INDIE;
    demo[artistStr]['discovery'] = KIMI; 
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = True;
    
    artistStr = 'Caribou';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = CANADA;
    demo[artistStr]['genre'] = INDIE;  #electronic dance?
    demo[artistStr]['discovery'] = KIMI; 
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = True;
    
    artistStr = 'Icon_of_Coil';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = NORWAY;
    demo[artistStr]['genre'] = EMO;
    demo[artistStr]['discovery'] = ON_MY_OWN_CONCERT; #Shazammed at Manray
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'Icon_of_Coil';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = NORWAY;
    demo[artistStr]['genre'] = EMO;
    demo[artistStr]['discovery'] = ON_MY_OWN_CONCERT; #Shazammed at Manray
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'London_After_Minight';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = USA;
    demo[artistStr]['genre'] = EMO;
    demo[artistStr]['discovery'] = ON_MY_OWN_CONCERT; #Shazammed at Manray
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'Cabaret_Nocture';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = BELGIUM;
    demo[artistStr]['genre'] = EMO;
    demo[artistStr]['discovery'] = ON_MY_OWN_CONCERT; #Shazammed at Manray
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'TV_on_the_Radio';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = True;
    demo[artistStr]['country'] = USA;
    demo[artistStr]['genre'] = INDIE;
    demo[artistStr]['discovery'] = OLD_DAYS; 
    demo[artistStr]['Seen_Live'] = True;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'Doechii';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = False; 
    demo[artistStr]['POC'] = True;
    demo[artistStr]['country'] = USA;
    demo[artistStr]['genre'] = HIPHOP;
    demo[artistStr]['discovery'] = BRIAN; 
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = True;
    
    artistStr = 'The_Soft_Moon';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = True; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = USA;
    demo[artistStr]['genre'] = EMO;
    demo[artistStr]['discovery'] = ON_MY_OWN_CONCERT; #I guess this is what I use for shazam
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;
    
    artistStr = 'Bec_Lauder';
    demo[artistStr] = dict()
    demo[artistStr]['Male'] = False; 
    demo[artistStr]['POC'] = False;
    demo[artistStr]['country'] = USA;
    demo[artistStr]['genre'] = INDIE;
    demo[artistStr]['discovery'] = MUSIC_LEAGUE; 
    demo[artistStr]['Seen_Live'] = False;
    demo[artistStr]['Kimi'] = False;

    # demo[''] = dict()
    # demo['']['Male'] = True; 
    # demo['']['POC'] = False;
    # demo['']['country'] = USA;
    # demo['']['genre'] = INDIE;
    # demo['']['discovery'] = BRIAN;
    # demo['']['Seen_Live'] = False;
    # demo['']['Kimi'] = False;


    return demo, genreNames, discoveryMethodNames, countryNames
