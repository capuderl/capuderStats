
from spotifyFxns import *


def spotify_stats_2021(songs,artists):

    ## 8/6/21

    artists = addArtist(artists, 'James_Blake',        1);
    artists = addArtist(artists, 'Bo_Burnham',         2);
    artists = addArtist(artists, 'Caroline_Polachek',  3);
    artists = addArtist(artists, 'Silverstein',        4);
    artists = addArtist(artists, 'La_La_Land',     5);

    songs = incrementSong(songs, 'James_Blake', 1);
    songs = incrementSong(songs, 'Bo_Burnham', 3);
    songs = incrementSong(songs, 'LPX', 1);

    print('\n\n8/6/21: Getting into James Blake and Caroline Polachek because we bought tickets for the concerts.  Still hooked on Bo, had a few days of La La Land.  Losing respect for Lil Dicky after the show.')


    ## 8/13/21

    artists = addArtist(artists, 'James_Blake',       1);
    artists = addArtist(artists, 'Bo_Burnham',        2);
    artists = addArtist(artists, 'Caroline_Polachek', 3);
    artists = addArtist(artists, 'Silverstein',       4);
    artists = addArtist(artists, 'RAP_Ferreira',      5);

    songs = incrementSong(songs, 'James_Blake', 3);
    songs = incrementSong(songs, 'Caroline_Polachek', 1);
    songs = incrementSong(songs, 'Lucky_Daye', 1);

    print('8/13/21: James Blake.  So much James Blake.')

    ## 8/20/21

    artists = addArtist(artists, 'The_Weeknd', 1);
    artists = addArtist(artists, 'Charli_XCX', 2);
    artists = addArtist(artists, 'Interpol',   3);
    artists = addArtist(artists, 'CHVRCHES',   4);
    artists = addArtist(artists, 'Future',     5);

    songs = incrementSong(songs, 'Interpol', 1);
    songs = incrementSong(songs, 'Haiku_Hands', 1);
    songs = incrementSong(songs, 'Everything_Everything', 1);
    songs = incrementSong(songs, 'Future', 1);
    songs = incrementSong(songs, 'The_Weeknd', 1);

    print('8/20/21: On vacation in Ohio, this is based on very little data lol')

    ## 8/27/21

    artists = addArtist(artists, 'Self_Esteem',      1);
    artists = addArtist(artists, 'James_Blake',      2);
    artists = addArtist(artists, 'Bo_Burnham',       3);
    artists = addArtist(artists, 'Matt_Berninger',   4);
    artists = addArtist(artists, 'Barenaked_Ladies', 5);

    songs = incrementSong(songs, 'Self_Esteem', 1);
    songs = incrementSong(songs, 'James_Blake', 3);
    songs = incrementSong(songs, 'Matt_Berninger', 1);


    ## 9/3/21

    artists = addArtist(artists, 'CHVRCHES',      1);
    artists = addArtist(artists, 'James_Blake',   2);
    artists = addArtist(artists, 'Joji',          3);
    artists = addArtist(artists, 'The_National',  4);
    artists = addArtist(artists, 'Thom_Yorke',    5);

    songs = incrementSong(songs, 'CHVRCHES', 2);
    songs = incrementSong(songs, 'James_Blake', 1);
    songs = incrementSong(songs, 'Thom_Yorke', 1);
    songs = incrementSong(songs, 'Joji', 1);

    print('9/3/21: I''ll be your bubble, I''ll make myself useful.  New CHVRCHES!')

    ## 9/10/21

    artists = addArtist(artists, 'James_Blake', 1);
    artists = addArtist(artists, 'Interpol',    2);
    artists = addArtist(artists, 'Passion_Pit', 3);
    artists = addArtist(artists, 'Joyce_Manor', 4);
    artists = addArtist(artists, 'Ripe',        5);

    songs = incrementSong(songs, 'James_Blake', 4);
    songs = incrementSong(songs, 'Passion_Pit', 1);

    print('9/10/21: Evaluating replacing Modest Mouse with James Blake in my top 5')

    ## 9/17/21

    artists = addArtist(artists, 'James_Blake',            1);
    artists = addArtist(artists, 'Ripe',                   2);
    artists = addArtist(artists, 'CHVRCHES',               3);
    artists = addArtist(artists, 'Motion_City_Soundtrack', 4);
    artists = addArtist(artists, 'Twin_Shadow',            5);

    songs = incrementSong(songs, 'James_Blake', 3);
    songs = incrementSong(songs, 'Twin_Shadow', 1);
    songs = incrementSong(songs, 'Deftones', 1);

    ## 9/24/21

    artists = addArtist(artists, 'James_Blake',    1);
    artists = addArtist(artists, 'Future_Islands', 2);
    artists = addArtist(artists, 'KennyHoopla',    3);
    artists = addArtist(artists, 'Taylor_Swift',   4);
    artists = addArtist(artists, 'Justin_Bieber',  5);

    songs = incrementSong(songs, 'James_Blake', 1);
    songs = incrementSong(songs, 'Justin_Bieber', 1);
    songs = incrementSong(songs, 'Future_Islands', 1);
    songs = incrementSong(songs, 'Jose_Gonzalez', 1);
    songs = incrementSong(songs, 'Hawthorne_Heights', 1);

    print('9/24/21: Future Islands concert.  So cathartic to experience after quarantine.  I sobbed during Walking Through That Door, so much hope')

    ## 9/30/21

    artists = addArtist(artists, 'Self_Esteem',         1);
    artists = addArtist(artists, 'James_Blake',         2);
    artists = addArtist(artists, 'Bo_Burnham',          3);
    artists = addArtist(artists, 'My_Chemical_Romance', 4);
    artists = addArtist(artists, 'Twin_Shadow',         5);

    songs = incrementSong(songs, 'Editors', 1);
    songs = incrementSong(songs, 'Jeff_Rosenstock', 1); #Nausea - I got so tired of discussing my future, I started avoiding the people I love
    songs = incrementSong(songs, 'Twin_Shadow', 2);
    songs = incrementSong(songs, 'White_Lies', 1);

    print('9/30/21: This is the age I decided to get into MCR')

    ## 10/8/21

    artists = addArtist(artists, 'James_Blake',         1);
    artists = addArtist(artists, 'My_Chemical_Romance', 2);
    artists = addArtist(artists, 'KennyHoopla',         3);
    artists = addArtist(artists, 'The_Bravery',         4);
    artists = addArtist(artists, 'Bon_Iver',            5);

    songs = incrementSong(songs, 'My_Chemical_Romance', 2);
    songs = incrementSong(songs, 'James_Blake', 2);
    songs = incrementSong(songs, 'Twin_Shadow', 1);

    print('10/8/21: James Blake concert was phenominal.  You could feel the big notes vibrate in your chest')

    ## 10/15/21

    artists = addArtist(artists, 'James_Blake',     1);
    artists = addArtist(artists, 'The_National',    2);
    artists = addArtist(artists, 'Joyce_Manor',     3);
    artists = addArtist(artists, 'Q',               4);
    artists = addArtist(artists, 'Bartees_Strange', 5);

    songs = incrementSong(songs, 'Q', 1);
    songs = incrementSong(songs, 'James_Blake', 3);
    songs = incrementSong(songs, 'INXS', 1);

    print('10/15/21: New James Blake Album is a bit underwhelming, but we''ll see how it settles in.')

    ## 10/22/21

    artists = addArtist(artists, 'Bo_Burnham',    1);
    artists = addArtist(artists, 'The_National',  2);
    artists = addArtist(artists, 'Self_Esteem',   3);
    artists = addArtist(artists, 'Charli_XCX',    4);
    artists = addArtist(artists, 'Majid_Jordan',  5);

    songs = incrementSong(songs, 'Self_Esteem', 1);
    songs = incrementSong(songs, 'Charli_XCX', 1);
    songs = incrementSong(songs, 'The_National', 2);
    songs = incrementSong(songs, 'The_Killers', 1);


    ## 10/29/21

    artists = addArtist(artists, 'Self_Esteem',        1);
    artists = addArtist(artists, 'James_Blake',        2);
    artists = addArtist(artists, 'Tyler_the_Creator',  3);
    artists = addArtist(artists, 'The_National',       4);
    artists = addArtist(artists, 'Love_Victor_Theme',  5); #Changed from Tyler_Glenn for clarity lol

    songs = incrementSong(songs, 'James_Blake', 1);
    songs = incrementSong(songs, 'Self_Esteem', 4);

    print('10/29/21: New Self Esteem album.  Obiviously that''s been on a loop all week, so incredible.  We had such a good time at The Encore, it was so good that I feel like I had a click where I felt closer to her.  I feel so much better when she''s around')

    ## 11/5/21

    artists = addArtist(artists, 'My_Chemical_Romance', 1);
    artists = addArtist(artists, 'Editors',             2);
    artists = addArtist(artists, 'Caroline_Polachek',   3);
    artists = addArtist(artists, 'CHVRCHES',            4);
    artists = addArtist(artists, 'Self_Esteem',         5);

    songs = incrementSong(songs, 'Caroline_Polachek',   2);
    songs = incrementSong(songs, 'Editors',             2);
    songs = incrementSong(songs, 'My_Chemical_Romance', 1);


    ## 11/12/21

    artists = addArtist(artists, 'James_Blake',    1);
    artists = addArtist(artists, 'Foals',          2);
    artists = addArtist(artists, 'My_Chemical_Romance', 3);
    artists = addArtist(artists, 'Silverstein',    4);
    artists = addArtist(artists, 'Alcazar',        5);

    songs = incrementSong(songs, 'Foals', 2);
    songs = incrementSong(songs, 'My_Chemical_Romance', 1);
    songs = incrementSong(songs, 'Alcazar', 1);
    songs = incrementSong(songs, 'James_Blake', 1);

    print('11/12/21: Welp, I guess James Blake is back.  I''ve been sleeping on Foals.')

    ## 11/19/21

    artists = addArtist(artists, 'Motion_City_Soundtrack', 1);
    artists = addArtist(artists, 'LCD_Soundsystem',        2);
    artists = addArtist(artists, 'James_Blake',            3);
    artists = addArtist(artists, 'Foals',                  4);
    artists = addArtist(artists, 'Interpol',               5);

    songs = incrementSong(songs, 'LCD_Soundsystem', 1);
    songs = incrementSong(songs, 'James_Blake',     1);
    songs = incrementSong(songs, 'Interpol',        1);
    songs = incrementSong(songs, 'Motion_City_Soundtrack', 2);

    ## 11/26/21

    artists = addArtist(artists, 'The_Weeknd', 1);
    artists = addArtist(artists, 'James_Blake',    2);
    artists = addArtist(artists, 'Say_Anything', 3);
    artists = addArtist(artists, 'Dear_Evan_Hansen', 4);
    artists = addArtist(artists, 'The_National',        5);

    songs = incrementSong(songs, 'The_Weeknd', 1);
    songs = incrementSong(songs, 'Dear_Evan_Hansen', 1);
    songs = incrementSong(songs, 'Senses_Fail', 1);
    songs = incrementSong(songs, 'Post_Malone', 1);
    songs = incrementSong(songs, 'Cheap_Girls', 1);

    ## 12/3/21

    artists = addArtist(artists, 'Editors',           1);
    artists = addArtist(artists, 'James_Blake',       2);
    artists = addArtist(artists, 'Caroline_Polachek', 3);
    artists = addArtist(artists, 'Foals',             4);
    artists = addArtist(artists, 'Lauv',              5);
     
    songs = incrementSong(songs, 'Lauv', 1);
    songs = incrementSong(songs, 'Interpol', 1);
    songs = incrementSong(songs, 'Charli_XCX', 1);
    songs = incrementSong(songs, 'Editors', 1);
    songs = incrementSong(songs, 'Matt_and_Kim', 1);
     
    
    ## 12/10/21

    artists = addArtist(artists, 'Self_Esteem',       1);
    artists = addArtist(artists, 'James_Blake',       2);
    artists = addArtist(artists, 'Tyler_the_Creator', 3);
    artists = addArtist(artists, 'Bo_Burnham',        4);
    artists = addArtist(artists, 'The_Weeknd',        5);

    songs = incrementSong(songs, 'Maps_and_Atlases', 1);
    songs = incrementSong(songs, 'Miya_Folick', 1);
    songs = incrementSong(songs, 'Self_Esteem', 1);
    songs = incrementSong(songs, 'Jack_Harlow', 1);
    songs = incrementSong(songs, 'Spoon', 1);

    ## 12/17/21

    artists = addArtist(artists, 'Tick_Tick_Boom',          1);
    artists = addArtist(artists, 'Dance_Gavin_Dance',       2);
    artists = addArtist(artists, 'Self_Esteem',             3);
    artists = addArtist(artists, 'Motion_City_Soundtrack',  4);
    artists = addArtist(artists, 'Plushgun',                5);

    songs = incrementSong(songs, 'Tick_Tick_Boom', 1);
    songs = incrementSong(songs, 'Bo_Burnham', 1);
    songs = incrementSong(songs, 'Plushgun', 1);
    songs = incrementSong(songs, 'James_Blake', 1);
    songs = incrementSong(songs, 'Motion_City_Soundtrack', 1);


    ## 12/24/21

    artists = addArtist(artists, 'Bo_Burnham',  1);
    artists = addArtist(artists, 'Joji',        2);
    artists = addArtist(artists, 'Nelly',       3);
    artists = addArtist(artists, 'James_Blake', 4);
    artists = addArtist(artists, 'Self_Esteem', 5);

    songs = incrementSong(songs, 'Joji', 1);
    songs = incrementSong(songs, 'Nelly', 1);
    songs = incrementSong(songs, 'Bo_Burnham', 3);

    ## 12/31/21

    artists = addArtist(artists, 'Everything_Everything',  1);
    artists = addArtist(artists, 'Taylor_Swift',        2);
    artists = addArtist(artists, 'Interpol',         3);
    artists = addArtist(artists, 'The_Strokes',      4);
    artists = addArtist(artists, 'Barenaked_Ladies', 5);

    songs = incrementSong(songs, 'Arctic_Monkeys', 1);
    songs = incrementSong(songs, 'Astronauts_Etc', 1);
    songs = incrementSong(songs, 'Barenaked_Ladies', 2);
    songs = incrementSong(songs, 'Taylor_Swift', 1);
    
    return songs,artists


