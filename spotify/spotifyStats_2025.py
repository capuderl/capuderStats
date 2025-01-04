from spotifyFxns import *

def spotify_stats_2025(songs,artists):

    ## 1/4/25
    artists = addArtist(artists, 'rEDOLENT',     1);  
    artists = addArtist(artists, 'Poppy',     2);
    artists = addArtist(artists, 'Tyler_the_Creator',  3);
    artists = addArtist(artists, 'The_Soft_Moon', 4);  
    artists = addArtist(artists, 'Little_Dragon', 5);

    songs = incrementSong(songs, 'rEDOLENT', 1); 
    songs = incrementSong(songs, 'The_Soft_Moon', 1);
    songs = incrementSong(songs, 'Bec_Lauder', 1); 
    songs = incrementSong(songs, 'CHVRCHES', 1); 
    songs = incrementSong(songs, 'The_National', 1); 

    return songs,artists