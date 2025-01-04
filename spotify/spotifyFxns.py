import matplotlib.pyplot as plt
from math import floor, ceil
import numpy

def addArtist(artists, artistName, rank):

    artistsExisting = list(artists.keys())

    if not (artistName in artistsExisting):
        artists[artistName] = []
        
    artists[artistName].append(rank)    
    
    return artists



def incrementSong(songs, artistName, numTimes):

    artistsExisting = list(songs.keys())
    
    if (artistName in artistsExisting):
        songs[artistName] = songs[artistName] + numTimes
    else:
        songs[artistName] = numTimes

    return songs
    
    
def spotifyAggregate2Pie(aggregate, genreNames, discoveryMethodNames, countryNames):

    fnDemo = list(aggregate.keys());

    fieldsExclude = ['Seen_Live', 'Kimi']; #{'Seen_Live', 'British'};
    counter = 0;

    #Let's hard code as a 2x3 for right now.  If I add more stats later I can change it
    numRowsPie = 2;
    numColsPie = 3;
    #setting figure size to be full screen for this computer
    #figure( 'position', [ 1          41        1920        1083]);
    
    [fig, axs] = plt.subplots(numRowsPie, numColsPie)
    fig.set_size_inches(18.5, 10.5)

    
    for iF in range(len(fnDemo)):
        if not (fnDemo[iF] in fieldsExclude):
            #axs[row, col]
            row = floor(counter/numColsPie)
            col = counter % numColsPie
            counter = counter+1;
            uniqueVals = list(set(aggregate[fnDemo[iF]]));
            #Count number of each value
            valCount = len(uniqueVals) * [0]
            for iVal in range(len(uniqueVals)):
                valCount[iVal] = aggregate[fnDemo[iF]].count(uniqueVals[iVal])
            #Treat labelsPie differently whether or not it's a boollean
            if isinstance(uniqueVals[0], bool):
                fn = fnDemo[iF]
                fn.replace('_', ' ')
                labelsPie = [('Not ' + fn), fn];
            elif (fnDemo[iF] == 'genre'):
                #labelsPie = genreNames(uniqueVals)
                labelsPie = [genreNames[i] for i in uniqueVals]
            elif (fnDemo[iF] == 'discovery'):
                #labelsPie = discoveryMethodNames(uniqueVals)
                labelsPie = [discoveryMethodNames[i] for i in uniqueVals]
            elif (fnDemo[iF] == 'country'):
                #labelsPie = discoveryMethodNames(uniqueVals)
                [valCount, uniqueVals] = condenseCategories(valCount, uniqueVals, len(countryNames)-1)
                labelsPie = [countryNames[i] for i in uniqueVals]
            else:
                print(fnDemo[iF])
                raise ValueError('is not programmed properly in demographics.')
            
            #add percentages to labelsPie
            for iVal in range(len(uniqueVals)):
                labelsPie[iVal] = '%s (%d%%)' % (labelsPie[iVal], round(100*valCount[iVal]/sum(valCount)))
                #labelsPie[iVal] = '%s (%d/%d=%d%%)' % (labelsPie[iVal], valCount[iVal], sum(valCount),  round(100*valCount[iVal]/sum(valCount)))
            
            #Fiddly color scheme thing: it's nice to have the larger thing first
            if (fnDemo[iF] in ['Male', 'Seen_Live']):
                valCount = list(reversed(valCount))
                labelsPie = list(reversed(labelsPie))

        #print(valCount) 
        #print(labelsPie)
        axs[row, col].pie(numpy.array(valCount), labels = labelsPie, startangle=90 , textprops={'fontsize': 8})
        
    #plt.show()            

    return fig, axs, numRowsPie, numColsPie


def condenseCategories(valCount, uniqueVals, valMoveTo):

    otherCount = 0
    
    #print("valCount in")
    #print(valCount)
    #print("uniqueVals in")
    #print(uniqueVals)

    #Idea is that if the value is too small, move it to the "other" category
    for iVal in reversed(range(len(uniqueVals))):
        #get rid of it if it's X% or less
        if round(100*valCount[iVal]/sum(valCount)) <= 2:
            otherCount = otherCount + valCount[iVal]
            #print('Before ' + iVal + ' del ' + valCount)
            del valCount[iVal]
            #print('After del ' + valCount)
            del uniqueVals[iVal]
    
    if otherCount > 0:
        #check to see if the "other" category is even in the unique values list.  If not append it
        if not numpy.in1d(valMoveTo, uniqueVals):
            uniqueVals.append(valMoveTo)
            valCount.append(0)
        
        #we're going to assume that valMoveTo is at the end
        #actually let's just assert it
        for i in range(len(uniqueVals)):
            assert uniqueVals[i] <= valMoveTo, 'This fxn assumes the value to move to is at the end'
        
        valCount[-1] = valCount[-1] + otherCount
    
    #print("valCount out")
    #print(valCount)
    #print("uniqueVals out")
    #print(uniqueVals)
    
    #wait = input("Breakpoint")
    
    return valCount, uniqueVals
