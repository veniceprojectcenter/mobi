# -*- coding: utf-8 -*-
"""
@author: VE17-MOVE
"""

#Import Packages
import pandas as pd
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import numpy as np
import random
import datetime
#Change credentials before running, you will need free plotly account to view interactive plots online
plotly.tools.set_credentials_file(username='michaelpanicci', api_key='tzVByU0RwXNbG0rlPZhj')


'''
Function that adds specific plots to the global variable 'paramsR'
Parameters:
lat: array of latitudes
lng: array of longitudes
size: size of marker
text: text on hover of marker
name: name of array in legend
color: color of markers
opacity: opacity of markers
Return:
paramsR: the array of 'Scattermapbox' objects
'''
paramsR=[]
def SMB(lat,lng,size,text,name,color,opacity):
    
    paramsR = [Scattermapbox(
                lat=lat,
                lon=lng,
                mode='markers',
                marker=Marker(
                    size=size,
                    color = color,
                    opacity = opacity
                ),
                text = text,
                name = name)]
        
    return paramsR


'''
Function that plots the final 'paramsR' variable, containing all the desired datasets to plot.
'''
def plot2(params):
    
    mapbox_access_token = 'pk.eyJ1IjoibWljaGFlbHBhbmljY2kiLCJhIjoiY2o5ZWFvdmg5MjByZDMzcGE5c3Y5Mnp1OCJ9.-bQPmJB8GoDVoKAQH9_eWA'

    data = Data(params)
    
    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat='45.438043',
                lon='12.335956'
            ),
            pitch=0,
            zoom=12
        ),
    )
    
    fig = dict(data=data, layout=layout)
    py.iplot(fig, filename= str(datetime.datetime.now()))


#Local files with data these file paths will change. 
#The specific data files used can be found in folder called 'Data' 
#located in the folder that this code is in on the Google Drive.
filenameStores = "C:\BoatParking\Stores.xlsx"
filenameSpots = "C:\BoatParking\RiveData.xlsx"
filenameOH = "C:\BoatParking\OneHour.xlsx"

#Pandas dataframes
df = pd.read_excel(filenameStores)
df1 = pd.read_excel(filenameSpots)
df2 = pd.read_excel(filenameOH)

#parameters for rive
minCanalLength = 5
condition =''

df1 = df1[df1['Width (meters)']>minCanalLength]
df1 = df1[df1['General Condition']!=condition]

#parse store data
cat = set(df['store_type'])
catList = list(cat)
paramsR=[]
params = []
a='10'
b='250'
c='30'
for eachCat in cat:
    a = str(a)
    clr = 'rgb('+a+','+a+','+a+')'
    #paramsR = SMB(df[df['store_type']==eachCat]['lat'],df[df['store_type']==eachCat]['lng'],20,df[df['store_type']==eachCat]['store_type'],np.random.randn(500))
    paramsR = SMB(df[df['store_type']==eachCat]['lat'],df[df['store_type']==eachCat]['lng'],20,df[df['store_type']==eachCat]['store_type'],df[df['store_type']==eachCat]['store_type'][df[df['store_type']==eachCat]['store_type'].index[0]],'rgb(250,0,0)',0.2)
    params = np.append(params, paramsR)    
    a = int(a)    
    a+=5
paramsR = SMB(df1['lat'],df1['lng'],10,'Rive','Rive','rgb(0,34,206)',0.45)
params = np.append(params, paramsR)

#generate suggested spots
finalSpotLat = []
finalSpotLng = []
x=0
dis =0.001
for eachSpotLat, eachSpotLng in zip(df1['lat'],df1['lng']):
    w=0
    print(x)
    for eachStoreLat, eachStoreLng in zip(df['lat'],df['lng']):
        if (eachStoreLat >= eachSpotLat-dis) and (eachStoreLat <= eachSpotLat+dis) and (eachStoreLng >= eachSpotLng-dis) and (eachStoreLng <= eachSpotLng+dis):
            w+=1            
            if w == 3:
                finalSpotLat = np.append(finalSpotLat, eachSpotLat)
                finalSpotLng = np.append(finalSpotLng, eachSpotLng)
                x+=1
                break


finalSpotLat1 = finalSpotLat
finalSpotLng1 = finalSpotLng
length = len(finalSpotLng1)
dis = 0.0015
x=0
for eachSpotLat, eachSpotLng in zip(finalSpotLat,finalSpotLng):
    r=0    
    while r < length:
        if (eachSpotLat >= finalSpotLat1[r]-dis) and (eachSpotLat <= finalSpotLat1[r]+dis) and (eachSpotLng >= finalSpotLng1[r]-dis) and (eachSpotLng <= finalSpotLng1[r]+dis):
            if (eachSpotLat != finalSpotLat1[r] and eachSpotLng != finalSpotLng1[r]):
                index = np.argwhere(finalSpotLat1==eachSpotLat)
                finalSpotLat1 = np.delete(finalSpotLat1, index)
                finalSpotLng1 = np.delete(finalSpotLng1, index)
                length = len(finalSpotLng1)
                print(length)
                break
        r+=1
        
finalSpotLat = []
finalSpotLng = []
x=0        
dis =0.001
for eachSpotLat, eachSpotLng in zip(df1['lat'],df1['lng']):
    w=0
    print(x)
    for eachStoreLat, eachStoreLng in zip(df['lat'],df['lng']):
        if (eachStoreLat >= eachSpotLat-dis) and (eachStoreLat <= eachSpotLat+dis) and (eachStoreLng >= eachSpotLng-dis) and (eachStoreLng <= eachSpotLng+dis):
            w+=1            
            if w == 10:
                finalSpotLat = np.append(finalSpotLat, eachSpotLat)
                finalSpotLng = np.append(finalSpotLng, eachSpotLng)
                x+=1
                break


finalSpotLat2 = finalSpotLat
finalSpotLng2 = finalSpotLng
length = len(finalSpotLng2)
dis = 0.0005
x=0
for eachSpotLat, eachSpotLng in zip(finalSpotLat,finalSpotLng):
    r=0    
    while r < length:
        if (eachSpotLat >= finalSpotLat2[r]-dis) and (eachSpotLat <= finalSpotLat2[r]+dis) and (eachSpotLng >= finalSpotLng2[r]-dis) and (eachSpotLng <= finalSpotLng2[r]+dis):
            if (eachSpotLat != finalSpotLat2[r] and eachSpotLng != finalSpotLng2[r]):
                index = np.argwhere(finalSpotLat2==eachSpotLat)
                finalSpotLat2 = np.delete(finalSpotLat2, index)
                finalSpotLng2 = np.delete(finalSpotLng2, index)
                length = len(finalSpotLng2)
                print(length)
                break
        r+=1
 
finalSpotLat3 = np.append(finalSpotLat1,finalSpotLat2)
finalSpotLng3 = np.append(finalSpotLng1,finalSpotLng2)                  

              
#limit suggested spots with introduction of Vento di Venezia docks      
docks = ['45.467104,12.284777',
'45.467411,12.284828',
'45.485408,12.252098',
'45.473380,12.263497',
'45.500757,12.335451',
'45.520581,12.370567',
'45.418404,12.258327',
'45.428848,12.334001',
'45.429737,12.324248',
'45.425624,12.315810',
'45.423309,12.326329',
'45.425668,12.331083',
'45.453294,12.355547',
'45.436520,12.377720',
'45.431953,12.368386',
'45.446065,12.335484',
'45.428273,12.379821',
'45.427198,12.379906',
'45.405797,12.361765',
'45.372184,12.336597',
'45.346262,12.313227',
'45.346064,12.312942',
'45.255401,12.298125',
'45.322024,12.317847',
'45.272449,12.300691',
'45.349759,12.319091',
'45.495775,12.411691',
'45,488898,12.411282',
'45.459640,12.410600',
'45.445375,12.391496',
'45.472949,12.451034']


dis=0.003
docksLat=[]
docksLon=[]
length = len(finalSpotLng3)
for eachDock in docks:
    lat = eachDock.split(',')[0]
    docksLat = np.append(docksLat, lat)
    lat = float(lat)
    lon = eachDock.split(',')[1]
    lon = float(lon)
    docksLon = np.append(docksLon, lon)
    for eachSpotLat, eachSpotLng in zip(finalSpotLat3,finalSpotLng3):
            if (eachSpotLat >= lat-dis) and (eachSpotLat <= lat+dis) and (eachSpotLng >= lon-dis) and (eachSpotLng <= lon+dis):
                    index = np.argwhere(finalSpotLat3==eachSpotLat)
                    finalSpotLat3 = np.delete(finalSpotLat3, index)
                    finalSpotLng3 = np.delete(finalSpotLng3, index)

paramsR = SMB(docksLat,docksLon,10,'Vento di Venezia Docks','Vento di Venezia Docks','rgb(200,0,200)',1)
params = np.append(params, paramsR)

paramsR = SMB(finalSpotLat3,finalSpotLng3,10,'Possible New Spots','Possible New Spots','rgb(33,199,0)',1)
params = np.append(params, paramsR)

#plot stores, rive, Vento di Venezia Docls, and final suggested spots 
plot2(params)