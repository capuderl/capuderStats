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
    
breakOutOnMyOwn = True #False
[demo, genreNames, discoveryMethodNames, countryNames] = spotifyArtistDemo(breakOutOnMyOwn)

#artistListDemo is all of the artists in the demographics
artistListDemo = list(demo.keys()); 
#fnDemo is the demographics fields (like Male or British)
fnDemo = list(demo[artistListDemo[0]])

#initialize aggregate structs
#Each field in the demographics will get a vector 
aggregate = dict()
for iF in range(len(fnDemo)):
    aggregate[fnDemo[iF]] = []
    
#The point of this script is that every artist that makes the demographics list is counted one
#So loop through the demographics keys
for iA in range(len(artistListDemo)):
    for iF in range(len(fnDemo)):
        stat = demo[artistListDemo[iA]][fnDemo[iF]];
        #Add to the aggregate once (cause that's the gimmick of this script)
        aggregate[fnDemo[iF]].extend([stat]) 

[fig, axs, numRowsPie, numColsPie] = spotifyAggregate2Pie(aggregate, genreNames, discoveryMethodNames, countryNames)

plt.show()  