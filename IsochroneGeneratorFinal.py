# -*- coding: utf-8 -*-
"""
@author: VE17-MOVE
"""

#Import Packages
import json
import gmplot
import requests
import sys
import datetime
import numpy as np
import googlemaps
from IPython.display import display, HTML, Image
from datetime import datetime
import pandas as pd

'''
Function to calculate time from origin to all destinations
Parameters:
origins: the array that contains a single starting location
destinations: the array containing all points within a grid of Venice
time: the amount of time for the isochrone
Return:
isoDestLon: the longitude of destinations that can be reached within 'time'
isoDestLat: the latitude of destinations that can be reached within 'time'
isoTimeArr: the time it took to reach each corresponding 'isoDestLon' and 'isoDestLat'
'''
def points(origins, destinations, time):
    #api_key ='AIzaSyASVGu17zYRLf0GAf_sDmxdtJBqV-qEWeo'
    #api_key = 'AIzaSyD0frCxt2b63ZYlu7Ju_WYkl5CwWcNJP50'    
    #api_key = 'AIzaSyAaoewbgKeBLdG5Qrmlq7iAQ8cIVqDAia8'
    #api_key = 'AIzaSyBMKpT1fLrwO7doRB649h-PFxmJ39cVEm0'
    api_key = 'AIzaSyCIHc81kDh2qJgKQ5-bsVs3Y3DZ3eSC6IU'
    #api_key = 'AIzaSyAqvqz70OJqExzwVvaoC8AveVjVP1T75wU'
    #api_key = 'AIzaSyAE2p2WgWPOGpRiEId0OUbL4XEQHvjA_50'
    #api_key = 'AIzaSyAr5GBLz-zE051aOUjp1sya8LXY_OEA82w'
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    payload = {'origins' : '|'.join(origins),'destinations' : '|'.join(destinations),'mode' : 'transit','key' : api_key}
    r = requests.get(base_url, params = payload)   
    if r.status_code != 200:
        print('HTTP status code {} received, program terminated.'.format(r.status_code))
    else:
        x = json.loads(r.text)
        isoDestLat = []
        isoDestLon = []
        isoTimeArr = []
        isoStopsLat = []
        isoStopsLon = []
        isoStopsTime = []
        routeTime = []
        for isrc, src in enumerate(x['origin_addresses']):
                for idst, dst in enumerate(x['destination_addresses']):
                    row = x['rows'][isrc]
                    cell = row['elements'][idst]
                    if cell['status'] == 'OK':
                        isoTime = int('{}'.format(cell['duration']['value']))
                        if isoTime <= time:
                            lat = destinations[idst].split(',')[0]
                            lon = destinations[idst].split(',')[1]
                            isoDestLat = np.append(isoDestLat,lat)
                            isoDestLon = np.append(isoDestLon,lon)
                            isoTimeArr = np.append(isoTimeArr,isoTime)
                            
                    else:
                        print('{} to {}: status = {}'.format(src, dst, cell['status']))
                        
    return isoDestLon, isoDestLat, isoTimeArr
 
'''
MAIN
'''
if __name__ == '__main__':
    
    #starting location
    origin = '45.438296,12.334241'
    #duration of isochrone
    originTimeMin = 15
    originTime = originTimeMin*60
    #destinations for 'points' function
    isoPoints = ['45.43984,12.31784',
                '45.42668,12.32522',
                '45.42943,12.32658',
                '45.43395,12.34344',
                '45.4175,12.36857',
                '45.439,12.304',
                '45.441,12.304',
                '45.435,12.306',
                '45.437,12.306',
                '45.441,12.306',
                '45.443,12.306',
                '45.425,12.308',
                '45.427,12.308',
                '45.437,12.308',
                '45.439,12.308',
                '45.443,12.308',
                '45.425,12.31',
                '45.427,12.31',
                '45.433,12.31',
                '45.439,12.31',
                '45.441,12.31',
                '45.443,12.31',
                '45.425,12.312',
                '45.427,12.312',
                '45.431,12.312',
                '45.433,12.312',
                '45.435,12.312',
                '45.437,12.312',
                '45.439,12.312',
                '45.441,12.312',
                '45.425,12.314',
                '45.427,12.314',
                '45.431,12.314',
                '45.433,12.314',
                '45.435,12.314',
                '45.437,12.314',
                '45.439,12.314',
                '45.441,12.314',
                '45.425,12.316',
                '45.427,12.316',
                '45.431,12.316',
                '45.433,12.316',
                '45.435,12.316',
                '45.437,12.316',
                '45.439,12.316',
                '45.441,12.316',
                '45.443,12.316',
                '45.425,12.318',
                '45.427,12.318',
                '45.431,12.318',
                '45.433,12.318',
                '45.435,12.318',
                '45.437,12.318',
                '45.439,12.318',
                '45.441,12.318',
                '45.443,12.318',
                '45.445,12.318',
                '45.425,12.32',
                '45.427,12.32',
                '45.431,12.32',
                '45.433,12.32',
                '45.435,12.32',
                '45.437,12.32',
                '45.439,12.32',
                '45.441,12.32',
                '45.443,12.32',
                '45.445,12.32',
                '45.447,12.32',
                '45.425,12.322',
                '45.427,12.322',
                '45.431,12.322',
                '45.433,12.322',
                '45.435,12.322',
                '45.437,12.322',
                '45.439,12.322',
                '45.441,12.322',
                '45.443,12.322',
                '45.445,12.322',
                '45.447,12.322',
                '45.425,12.324',
                '45.431,12.324',
                '45.433,12.324',
                '45.435,12.324',
                '45.437,12.324',
                '45.439,12.324',
                '45.441,12.324',
                '45.443,12.324',
                '45.445,12.324',
                '45.447,12.324',
                '45.423,12.326',
                '45.425,12.326',
                '45.431,12.326',
                '45.433,12.326',
                '45.435,12.326',
                '45.437,12.326',
                '45.439,12.326',
                '45.441,12.326',
                '45.443,12.326',
                '45.445,12.326',
                '45.447,12.326',
                '45.423,12.328',
                '45.425,12.328',
                '45.429,12.328',
                '45.431,12.328',
                '45.433,12.328',
                '45.435,12.328',
                '45.437,12.328',
                '45.439,12.328',
                '45.441,12.328',
                '45.443,12.328',
                '45.445,12.328',
                '45.447,12.328',
                '45.423,12.33',
                '45.425,12.33',
                '45.429,12.33',
                '45.431,12.33',
                '45.433,12.33',
                '45.435,12.33',
                '45.437,12.33',
                '45.439,12.33',
                '45.441,12.33',
                '45.443,12.33',
                '45.445,12.33',
                '45.447,12.33',
                '45.423,12.332',
                '45.425,12.332',
                '45.429,12.332',
                '45.431,12.332',
                '45.433,12.332',
                '45.435,12.332',
                '45.437,12.332',
                '45.439,12.332',
                '45.441,12.332',
                '45.443,12.332',
                '45.445,12.332',
                '45.447,12.332',
                '45.423,12.334',
                '45.425,12.334',
                '45.429,12.334',
                '45.431,12.334',
                '45.433,12.334',
                '45.435,12.334',
                '45.437,12.334',
                '45.439,12.334',
                '45.441,12.334',
                '45.443,12.334',
                '45.445,12.334',
                '45.447,12.334',
                '45.423,12.336',
                '45.425,12.336',
                '45.431,12.336',
                '45.433,12.336',
                '45.435,12.336',
                '45.437,12.336',
                '45.439,12.336',
                '45.441,12.336',
                '45.443,12.336',
                '45.423,12.338',
                '45.425,12.338',
                '45.433,12.338',
                '45.435,12.338',
                '45.437,12.338',
                '45.439,12.338',
                '45.441,12.338',
                '45.443,12.338',
                '45.425,12.34',
                '45.427,12.34',
                '45.433,12.34',
                '45.435,12.34',
                '45.437,12.34',
                '45.439,12.34',
                '45.441,12.34',
                '45.443,12.34',
                '45.427,12.342',
                '45.429,12.342',
                '45.433,12.342',
                '45.435,12.342',
                '45.437,12.342',
                '45.439,12.342',
                '45.441,12.342',
                '45.427,12.344',
                '45.429,12.344',
                '45.435,12.344',
                '45.437,12.344',
                '45.439,12.344',
                '45.441,12.344',
                '45.427,12.346',
                '45.429,12.346',
                '45.435,12.346',
                '45.437,12.346',
                '45.439,12.346',
                '45.445,12.346',
                '45.447,12.346',
                '45.433,12.348',
                '45.435,12.348',
                '45.437,12.348',
                '45.439,12.348',
                '45.445,12.348',
                '45.447,12.348',
                '45.433,12.35',
                '45.435,12.35',
                '45.437,12.35',
                '45.431,12.352',
                '45.433,12.352',
                '45.435,12.352',
                '45.437,12.352',
                '45.431,12.354',
                '45.433,12.354',
                '45.435,12.354',
                '45.437,12.354',
                '45.429,12.356',
                '45.431,12.356',
                '45.433,12.356',
                '45.435,12.356',
                '45.437,12.356',
                '45.427,12.358',
                '45.429,12.358',
                '45.431,12.358',
                '45.433,12.358',
                '45.435,12.358',
                '45.437,12.358',
                '45.439,12.358',
                '45.425,12.36',
                '45.427,12.36',
                '45.429,12.36',
                '45.431,12.36',
                '45.433,12.36',
                '45.435,12.36',
                '45.437,12.36',
                '45.439,12.36',
                '45.425,12.362',
                '45.427,12.362',
                '45.429,12.362',
                '45.431,12.362',
                '45.439,12.362',
                '45.425,12.364',
                '45.427,12.364',
                '45.429,12.364',
                '45.425,12.366',
                '45.427,12.366',
                '45.429,12.366',
                '45.395,12.354',
                '45.397,12.354',
                '45.431,12.354',
                '45.395,12.356',
                '45.397,12.356',
                '45.399,12.356',
                '45.429,12.356',
                '45.431,12.356',
                '45.395,12.358',
                '45.397,12.358',
                '45.399,12.358',
                '45.401,12.358',
                '45.429,12.358',
                '45.431,12.358',
                '45.395,12.36',
                '45.397,12.36',
                '45.399,12.36',
                '45.401,12.36',
                '45.403,12.36',
                '45.411,12.36',
                '45.425,12.36',
                '45.427,12.36',
                '45.429,12.36',
                '45.431,12.36',
                '45.397,12.362',
                '45.399,12.362',
                '45.401,12.362',
                '45.403,12.362',
                '45.405,12.362',
                '45.407,12.362',
                '45.411,12.362',
                '45.425,12.362',
                '45.427,12.362',
                '45.429,12.362',
                '45.431,12.362',
                '45.399,12.364',
                '45.401,12.364',
                '45.403,12.364',
                '45.405,12.364',
                '45.407,12.364',
                '45.409,12.364',
                '45.411,12.364',
                '45.425,12.364',
                '45.427,12.364',
                '45.401,12.366',
                '45.403,12.366',
                '45.405,12.366',
                '45.407,12.366',
                '45.409,12.366',
                '45.411,12.366',
                '45.413,12.366',
                '45.425,12.366',
                '45.427,12.366',
                '45.429,12.366',
                '45.403,12.368',
                '45.405,12.368',
                '45.407,12.368',
                '45.409,12.368',
                '45.411,12.368',
                '45.413,12.368',
                '45.415,12.368',
                '45.417,12.368',
                '45.405,12.37',
                '45.407,12.37',
                '45.409,12.37',
                '45.411,12.37',
                '45.413,12.37',
                '45.415,12.37',
                '45.417,12.37',
                '45.407,12.372',
                '45.409,12.372',
                '45.411,12.372',
                '45.413,12.372',
                '45.415,12.372',
                '45.417,12.372',
                '45.409,12.374',
                '45.411,12.374',
                '45.413,12.374',
                '45.415,12.374',
                '45.417,12.374',
                '45.419,12.374',
                '45.411,12.376',
                '45.413,12.376',
                '45.415,12.376',
                '45.417,12.376',
                '45.419,12.376',
                '45.421,12.376',
                '45.413,12.378',
                '45.415,12.378',
                '45.417,12.378',
                '45.419,12.378',
                '45.421,12.378',
                '45.423,12.378',
                '45.425,12.378',
                '45.415,12.38',
                '45.417,12.38',
                '45.419,12.38',
                '45.421,12.38',
                '45.423,12.38',
                '45.425,12.38',
                '45.427,12.38',
                '45.417,12.382',
                '45.419,12.382',
                '45.421,12.382',
                '45.423,12.382',
                '45.425,12.382',
                '45.427,12.382',
                '45.429,12.382',
                '45.419,12.384',
                '45.421,12.384',
                '45.423,12.384',
                '45.425,12.384',
                '45.427,12.384',
                '45.429,12.384',
                '45.431,12.384',
                '45.419,12.386',
                '45.421,12.386',
                '45.423,12.386',
                '45.425,12.386',
                '45.427,12.386',
                '45.429,12.386',
                '45.431,12.386',
                '45.421,12.388',
                '45.423,12.388',
                '45.425,12.388',
                '45.427,12.388',
                '45.429,12.388',
                '45.431,12.388',
                '45.46,12.259',
                '45.462,12.259',
                '45.464,12.259',
                '45.466,12.259',
                '45.468,12.259',
                '45.47,12.259',
                '45.472,12.259',
                '45.474,12.259',
                '45.46,12.261',
                '45.462,12.261',
                '45.464,12.261',
                '45.466,12.261',
                '45.468,12.261',
                '45.47,12.261',
                '45.472,12.261',
                '45.474,12.261',
                '45.458,12.263',
                '45.46,12.263',
                '45.462,12.263',
                '45.464,12.263',
                '45.466,12.263',
                '45.468,12.263',
                '45.47,12.263',
                '45.472,12.263',
                '45.474,12.263',
                '45.476,12.263',
                '45.458,12.265',
                '45.46,12.265',
                '45.462,12.265',
                '45.464,12.265',
                '45.466,12.265',
                '45.468,12.265',
                '45.47,12.265',
                '45.472,12.265',
                '45.474,12.265',
                '45.476,12.265',
                '45.456,12.267',
                '45.458,12.267',
                '45.46,12.267',
                '45.462,12.267',
                '45.464,12.267',
                '45.466,12.267',
                '45.468,12.267',
                '45.47,12.267',
                '45.472,12.267',
                '45.474,12.267',
                '45.476,12.267',
                '45.454,12.269',
                '45.456,12.269',
                '45.458,12.269',
                '45.46,12.269',
                '45.462,12.269',
                '45.464,12.269',
                '45.466,12.269',
                '45.468,12.269',
                '45.47,12.269',
                '45.472,12.269',
                '45.474,12.269',
                '45.476,12.269',
                '45.454,12.271',
                '45.456,12.271',
                '45.458,12.271',
                '45.46,12.271',
                '45.462,12.271',
                '45.464,12.271',
                '45.466,12.271',
                '45.468,12.271',
                '45.47,12.271',
                '45.472,12.271',
                '45.474,12.271',
                '45.454,12.273',
                '45.456,12.273',
                '45.458,12.273',
                '45.46,12.273',
                '45.462,12.273',
                '45.464,12.273',
                '45.466,12.273',
                '45.468,12.273',
                '45.47,12.273',
                '45.472,12.273',
                '45.454,12.275',
                '45.456,12.275',
                '45.458,12.275',
                '45.46,12.275',
                '45.462,12.275',
                '45.466,12.275',
                '45.468,12.275',
                '45.47,12.275',
                '45.472,12.275',
                '45.462,12.277',
                '45.464,12.277',
                '45.466,12.277',
                '45.468,12.277',
                '45.47,12.277',
                '45.472,12.277',
                '45.462,12.279',
                '45.464,12.279',
                '45.466,12.279',
                '45.468,12.279',
                '45.47,12.279',
                '45.455,12.344',
                '45.455,12.346',
                '45.457,12.346',
                '45.461,12.346',
                '45.453,12.348',
                '45.459,12.348',
                '45.461,12.348',
                '45.453,12.35',
                '45.455,12.35',
                '45.457,12.35',
                '45.459,12.35',
                '45.461,12.35',
                '45.453,12.352',
                '45.455,12.352',
                '45.457,12.352',
                '45.459,12.352',
                '45.461,12.352',
                '45.453,12.354',
                '45.455,12.354',
                '45.457,12.354',
                '45.459,12.354',
                '45.461,12.354',
                '45.457,12.356',
                '45.459,12.356',
                '45.461,12.356',
                '45.455,12.358',
                '45.457,12.358',
                '45.459,12.358',
                '45.431,12.368',
                '45.433,12.368',
                '45.433,12.37',
                '45.462,12.257',
                '45.464,12.257',
                '45.466,12.257',
                '45.468,12.257',
                '45.47,12.257',
                '45.472,12.257',
                '45.474,12.257',
                '45.476,12.257',
                '45.476,12.259',
                '45.476,12.261',
                '45.474,12.273',
                '45.474,12.275',
                '45.447,12.35',
                '45.474,12.255',
                '45.474,12.253',
                '45.472,12.255',
                '45.472,12.253',
                '45.470,12.255',
                '45.470,12.253',
                '45.476,12.255',
                '45.468,12.255']
    
        
    #Arrays to store final results
    #Necessary due to limit of 25 calls at once with API
    isoDestLonFull = []
    isoDestLatFull = []
    isoTimeArrFull = []
    isoStopsLatFull = []
    isoStopsLonFull = []
    isoStopsTimeFull = []
    routeTimeFull = []
    
    #Loop to call 'points' with 25 destinations at a time
    w=0
    while(w < len(isoPoints)):
        
        if ((w+24) < len(isoPoints)):        
            isoDestLon, isoDestLat, isoTimeArr = points([origin], isoPoints[w:w+24], originTime)
        else:
            isoDestLon, isoDestLat, isoTimeArr = points([origin], isoPoints[w:len(isoPoints)-1], originTime)
        
        isoDestLatFull = np.append(isoDestLatFull,isoDestLat)
        isoDestLonFull = np.append(isoDestLonFull,isoDestLon)
        isoTimeArrFull = np.append(isoTimeArrFull,isoTimeArr)
        w += 25
    
        
    '''
    The Following commented code can produce isochrones with potential subway systems.
    The code will need to be modified depending on the subway route and time of isochrone.
    The 'times' variable below can be used to view useful times for code.
    After code is properly updated, uncomment to run for isochrone with potential subway system.
    
    With an api key without limits, the for loops that delete from isoPoints can be removed.
    '''
    '''
    #potential stops for subway system
    stops = ['45.43984,12.31784',
            '45.42668,12.32522',
            '45.42943,12.32658',
            '45.43395,12.34344',
            '45.4175,12.36857']
    
    #convert arrays to numpy arrays, calculate necessary travel times for stops, stored in 'times'        
    isoPoints = np.asarray(isoPoints, dtype=np.dtype('U25'))   
    isoDestLatFull = np.asarray(isoDestLatFull, dtype=np.dtype('U25'))
    isoDestLonFull = np.asarray(isoDestLonFull, dtype=np.dtype('U25'))
    isoTimeArrFull = np.asarray(isoTimeArrFull, dtype=np.dtype('U25'))       
    times = []
    for i in range(0,len(stops)):
        m = np.where(isoDestLatFull==stops[i].split(',')[0])
        times = np.append(times,isoTimeArrFull[m])
        isoDestLatFull = np.delete(isoDestLatFull,m)
        isoDestLonFull = np.delete(isoDestLonFull,m)
        isoTimeArrFull = np.delete(isoTimeArrFull,m)
    
    
    for i in range(0,len(isoDestLatFull)):
        m = np.where(isoPoints==(isoDestLatFull[i]+','+isoDestLonFull[i]))
        isoPoints = np.delete(isoPoints,m)
    
    w=0
    while(w < len(isoPoints)):
        
        if ((w+24) < len(isoPoints)):        
            isoDestLon, isoDestLat, isoTimeArr = points(['45.43395,12.34344'], isoPoints[w:w+24], 447)
        else:
            isoDestLon, isoDestLat, isoTimeArr = points(['45.43395,12.34344'], isoPoints[w:len(isoPoints)-1], 447)
        
        for i in range(0,len(isoTimeArr)):
            isoTimeArr[i] = isoTimeArr[i]+originTime-447
        isoDestLatFull = np.append(isoDestLatFull,isoDestLat)
        isoDestLonFull = np.append(isoDestLonFull,isoDestLon)
        isoTimeArrFull = np.append(isoTimeArrFull,isoTimeArr)
        w += 25
        
    for i in range(0,len(isoDestLatFull)):
        m = np.where(isoPoints==(isoDestLatFull[i]+','+isoDestLonFull[i]))
        isoPoints = np.delete(isoPoints,m)
    
    w=0
    while(w < len(isoPoints)):
        
        if ((w+24) < len(isoPoints)):        
            isoDestLon, isoDestLat, isoTimeArr = points(['45.42668,12.32522'], isoPoints[w:w+24], 255)
        else:
            isoDestLon, isoDestLat, isoTimeArr = points(['45.42668,12.32522'], isoPoints[w:len(isoPoints)-1], 255)
        
        for i in range(0,len(isoTimeArr)):
            isoTimeArr[i] = isoTimeArr[i]+originTime-255
        isoDestLatFull = np.append(isoDestLatFull,isoDestLat)
        isoDestLonFull = np.append(isoDestLonFull,isoDestLon)
        isoTimeArrFull = np.append(isoTimeArrFull,isoTimeArr)
        w += 25    
    
    for i in range(0,len(isoDestLatFull)):
        m = np.where(isoPoints==(isoDestLatFull[i]+','+isoDestLonFull[i]))
        isoPoints = np.delete(isoPoints,m)
        
    w=0
    while(w < len(isoPoints)):
        
        if ((w+24) < len(isoPoints)):        
            isoDestLon, isoDestLat, isoTimeArr = points(['45.42943,12.32658'], isoPoints[w:w+24], 255)
        else:
            isoDestLon, isoDestLat, isoTimeArr = points(['45.42943,12.32658'], isoPoints[w:len(isoPoints)-1], 255)
        
        for i in range(0,len(isoTimeArr)):
            isoTimeArr[i] = isoTimeArr[i]+originTime-255
        isoDestLatFull = np.append(isoDestLatFull,isoDestLat)
        isoDestLonFull = np.append(isoDestLonFull,isoDestLon)
        isoTimeArrFull = np.append(isoTimeArrFull,isoTimeArr)
        w += 25  
        
    for i in range(0,len(isoDestLatFull)):
        m = np.where(isoPoints==(isoDestLatFull[i]+','+isoDestLonFull[i]))
        isoPoints = np.delete(isoPoints,m)     
    
    w=0
    while(w < len(isoPoints)):
        
        if ((w+24) < len(isoPoints)):        
            isoDestLon, isoDestLat, isoTimeArr = points(['45.43984,12.31784'], isoPoints[w:w+24], 165)
        else:
            isoDestLon, isoDestLat, isoTimeArr = points(['45.43984,12.31784'], isoPoints[w:len(isoPoints)-1], 165)
        
        for i in range(0,len(isoTimeArr)):
            isoTimeArr[i] = isoTimeArr[i]+originTime-165
        isoDestLatFull = np.append(isoDestLatFull,isoDestLat)
        isoDestLonFull = np.append(isoDestLonFull,isoDestLon)
        isoTimeArrFull = np.append(isoTimeArrFull,isoTimeArr)
        w += 25
    '''   
    
    
    #convert lat and lons to floats for plotting
    lats = [float(i) for i in isoDestLatFull.tolist()]
    lons = [float(i) for i in isoDestLonFull.tolist()]
    
    #where to to center geo-plot
    gmap = gmplot.GoogleMapPlotter(45.438017,12.329965, 16)
    
    #draw grid for isochrones
    x=0.002/2
    for i in range(0,len(lats)):
        alpha = (originTime - float(isoTimeArrFull[i]))/originTime
        lat = lats[i]
        lon = lons[i]
        polylats = lat+x,lat+x,lat-x,lat-x
        polylons = lon-x,lon+x,lon+x,lon-x
        gmap.polygon(polylats, polylons, edge_color = 'red', edge_alpha = None, edge_width = None, face_color='red', face_alpha=alpha, clickable = True)
    
    #display origin
    x=0.002/3  
    lat = float(origin.split(',')[0])
    lon = float(origin.split(',')[1])
    polylats = lat+x,lat,lat-x,lat
    polylons = lon,lon+x,lon,lon-x
    gmap.polygon(polylats, polylons, edge_color = 'blue', edge_alpha = None, edge_width = 5, face_color='blue', face_alpha=None, clickable = True)  
    
    #produce geo-plot and save
    gmap.draw("IsochroneTest.html")