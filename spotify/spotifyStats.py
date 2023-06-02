#from spotifyFxns import *
from spotifyStats_2021 import *
from spotifyStats_2022 import *
from spotifyStats_2023 import *
from spotifyArtistDemo import *
from math import floor, ceil
import warnings
import numpy
import sys
def fprintf(stream, format_spec, *args):
    stream.write(format_spec % args)

artists = dict()
songs = dict()

#[songs,artists] = spotify_stats_2021(songs,artists)

#[songs,artists] = spotify_stats_2022(songs,artists)

[songs,artists] = spotify_stats_2023(songs,artists)


############################# PRINTOUT

#An artist with a really long name might make me increase this
padSpaces = 26;

fprintf(sys.stdout, '\n\nSongs:\n')
# disp(songs)
fn = list(songs.keys())
songCount = numpy.array([0] * len(fn))
for iS in range(len(fn)):
   songCount[iS] = songs[fn[iS]]
idxSort = numpy.argsort(-songCount) #minus sign is to make it descending
for iS in idxSort:
   fprintf(sys.stdout, '%s:  %d\n', fn[iS].ljust(padSpaces), songs[fn[iS]]);

print('\n\nArtists:')
fn = list(artists.keys())
artistCount = numpy.zeros(shape=(5, len(fn)))
for iA in range(len(fn)):
    for iP in range(4, -1, -1):
        artistCount[iP, iA] = artists[fn[iA]].count(iP+1);
        #adding a tiebreaker...it's kinda lazy but it works lol
        if artistCount[iP, iA] > 0:
            for iP_tiebreaker in range(iP+1, 5):
                #fprintf(sys.stdout, '%s %d %d: %.2f + %.2f=', fn[iA], iP, iP_tiebreaker, artistCount[iP, iA], artistCount[iP_tiebreaker, iA] * (6 - iP_tiebreaker) / 50)
                artistCount[iP, iA] = artistCount[iP, iA] + artistCount[iP_tiebreaker, iA] * (6 - iP_tiebreaker) / 50;
                #fprintf(sys.stdout, '%.2f\n', artistCount[iP, iA])
#print(artistCount)
#print(artists)
for iP in range(5):
    idxSort = numpy.argsort(-artistCount[iP, :]) #minus sign is to make it descending
    #[~, idxSort] = sort(artistCount[iP, :], 'descend');
    for iA in idxSort:
        val = artistCount[iP, iA]
        #Only print if
        #1) The artist has been ranked in this slot at all
        #2) The artist hasn't been printed already (aka it has a better ranking)
        if (val > 0) and (iP==0 or sum(artistCount[range(iP), iA])==0):
            #fprintf(sys.stdout,'%s %d %d\n ', fn[iA], iP, sum(artistCount[range(iP-1), iA]) );
            vec = sorted(artists[fn[iA]])
            #if len(vec) > 1:
            fprintf(sys.stdout,'%s:  ', fn[iA].ljust(padSpaces));
            for iV in range(len(vec)):
                fprintf(sys.stdout,'%d ', vec[iV]);
            fprintf(sys.stdout,'\n');
            #else:
            #    fprintf(sys.stdout,'%s:  %d\n', fn[iA].ljust(padSpaces), vec);



############################# PIE CHARTS

breakOutOnMyOwn = True #False
[demo, genreNames, discoveryMethodNames, countryNames] = spotifyArtistDemo(breakOutOnMyOwn)

artistListDemo = list(demo.keys()); 
fnDemo = list(demo[artistListDemo[0]])

#initialize aggregate structs
aggregateArtists = dict()
aggregateSongs = dict()
# I don't have much of a purpose for aggregateArtistsTop5 yet
# I made some plots in matlab that weren't super insightful, so I won't bother here
# It splits artist stats into "number of first places" etc
aggregateArtistsTop5 = [dict() for i in range(5)]
for iF in range(len(fnDemo)):
    aggregateArtists[fnDemo[iF]] = []
    aggregateSongs[fnDemo[iF]] = []
    for i in range(5):
        aggregateArtistsTop5[i][fnDemo[iF]] = []

#Aggregate stats for songs
fnSong = list(songs.keys());
for iS in range(len(fnSong)):
    #Sanity check that the artist is in my demographics list
    #if iS==1:
    #    print(fnSong[iS])
    #    print(artistListDemo)
    #    print(fnSong[iS] in artistListDemo)
    isInDemo = (fnSong[iS] in artistListDemo)
    if not isInDemo:
        print(fnSong[iS])
        warnings.warn('Add this to the demographics list.  Not aggregated in the stats for now.')
        #warning('Add %s to the demographics list.  Not aggregated in the stats for now.',fnSong{iS})
    else:
        for iF in range(len(fnDemo)):
            stat = demo[fnSong[iS]][fnDemo[iF]]
            count = songs[fnSong[iS]]
            #Add to the aggregate once for each time it's counted
            aggregateSongs[fnDemo[iF]].extend(count*[stat]) 

            
            
#print(aggregateSongs)

[fig, axs, numRowsPie, numColsPie] = spotifyAggregate2Pie(aggregateSongs, genreNames, discoveryMethodNames, countryNames)
#Add a pie chart with top 5 separate
#Make it in the last slot
row = numRowsPie-1
col = numColsPie-1
#How many artists do I want to call out
howManyHighlight = 7;
idxSort = numpy.argsort(-songCount) #minus sign is to make it descending
idxHighlight = idxSort[range(howManyHighlight)]
songsByTop5 = songCount[idxHighlight];
#Everything not in the top 5
#idxEverythingElse = range(len(songCount)).difference(idxHighlight) 
idxEverythingElse = list(range(len(songCount)))
for i in numpy.sort(-idxHighlight):
    idxEverythingElse.pop(abs(i)) 
#songsByTop5.append(sum(songCount[idxEverythingElse]))
songsByTop5 = numpy.append(songsByTop5, sum(songCount[idxEverythingElse]))
labelsPie = [fnSong[i].replace('_', ' ') for i in idxHighlight]
labelsPie.append('Other')
#add percentages to labels
for i in range(len(labelsPie)):
    labelsPie[i] = '%s (%d%%)' % (labelsPie[i], round(100*songsByTop5[i]/sum(songsByTop5)));
axs[row, col].pie(songsByTop5, labels=labelsPie, startangle=270, textprops={'fontsize': 8})
fig.suptitle('By Song Count', fontsize=16)


#Aggregate stats for artists
fnArtist = list(artists.keys())
for iA in range(len(fnArtist)):
    #Sanity check that the artist is in my demographics list
    isInDemo = (fnArtist[iA] in artistListDemo)
    if not isInDemo:
        print(fnArtist[iA])
        warnings.warn('Add this to the demographics list.  Not aggregated in the stats for now.')
    else:
        for iF in range(len(fnDemo)):
            stat = demo[fnArtist[iA]][fnDemo[iF]];
            count = len(artists[fnArtist[iA]]);
            #Add to the aggregate once for each time it's counted
            aggregateArtists[fnDemo[iF]].extend(count*[stat]) 
            #Do each in "top 5 artists" separately
            for i in range(5):
                count = artists[fnArtist[iA]].count(i+1); #+1 because 0 indexing
                aggregateArtistsTop5[i][fnDemo[iF]].extend(count*[stat]) 
                if iA==0 and iF==0:
                    fprintf(sys.stdout, '%s All: %d vs rank %d: %d\n', fnArtist[iA], len(artists[fnArtist[iA]]), i+1, count)
                    #I had trouble on my first cut initializing these variables using a REFERENCE, so they would change together
                    #print(len(aggregateArtists[fnDemo[iF]]))
                    #print(len(aggregateArtistsTop5[i][fnDemo[iF]]))




[fig, axs, numRowsPie, numColsPie] = spotifyAggregate2Pie(aggregateArtistsTop5[0], genreNames, discoveryMethodNames, countryNames)
#Add a pie chart with top 5 separate
#Make it in the last slot
row = numRowsPie-1
col = numColsPie-1
#How many artists do I want to call out
howManyHighlight = 7;
artistLength = numpy.array(len(fnArtist) * [0])
for iA in range(len(fnArtist)):
    artistLength[iA] = artists[fnArtist[iA]].count(1);
idxSort = numpy.argsort(-artistLength) #minus sign is to make it descending
idxHighlight = idxSort[range(howManyHighlight)]
songsByTop5 = artistLength[idxHighlight];
#Everything not in the top 5
#idxEverythingElse = range(len(songCount)).difference(idxHighlight) 
idxEverythingElse = list(range(len(artistLength)))
for i in numpy.sort(-idxHighlight):
    idxEverythingElse.pop(abs(i))
songsByTop5 = numpy.append(songsByTop5, sum(artistLength[idxEverythingElse]))
labelsPie = [fnArtist[i].replace('_', ' ') for i in idxHighlight]
labelsPie.append('Other')
#add percentages to labels
for i in range(len(labelsPie)):
    labelsPie[i] = '%s (%d%%)' % (labelsPie[i], round(100*songsByTop5[i]/sum(songsByTop5)));
axs[row, col].pie(songsByTop5, labels=labelsPie, startangle=270, textprops={'fontsize': 8})
fig.suptitle('Count of Artist in Number one Spot', fontsize=16)

[fig, axs, numRowsPie, numColsPie] = spotifyAggregate2Pie(aggregateArtists, genreNames, discoveryMethodNames, countryNames)
#Add a pie chart with top 5 separate
#Make it in the last slot
row = numRowsPie-1
col = numColsPie-1
#How many artists do I want to call out
howManyHighlight = 7; #7
artistLength = numpy.array(len(fnArtist) * [0])
for iA in range(len(fnArtist)):
    artistLength[iA] = len(artists[fnArtist[iA]]);
idxSort = numpy.argsort(-artistLength) #minus sign is to make it descending
idxHighlight = idxSort[range(howManyHighlight)]
songsByTop5 = artistLength[idxHighlight];
#Everything not in the top 5
idxEverythingElse = list(range(len(artistLength)))
for i in numpy.sort(-idxHighlight):
    idxEverythingElse.pop(abs(i))
songsByTop5 = numpy.append(songsByTop5, sum(artistLength[idxEverythingElse]))
labelsPie = [fnArtist[i].replace('_', ' ') for i in idxHighlight]
labelsPie.append('Other')
#add percentages to labels
for i in range(len(labelsPie)):
    labelsPie[i] = '%s (%d%%)' % (labelsPie[i], round(100*songsByTop5[i]/sum(songsByTop5)));
axs[row, col].pie(songsByTop5, labels=labelsPie, startangle=270, textprops={'fontsize': 8})
fig.suptitle('By Artist Count', fontsize=16)

#print(aggregateArtistsTop5[0])
#print(aggregateArtists)

plt.show()  