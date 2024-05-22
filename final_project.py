import numpy as np
import pandas as pd
import scipy
import math
import matplotlib.pyplot as plt

# Testing
# test_data='Test_data/bike Beek station.csv'
# data=pd.read_csv(test_data)
# latitude=data["Latitude"].to_numpy()
# longitude=data['Longitude'].to_numpy()
# speed=data['Speed (m/s)'].to_numpy()
# time=data["time"].to_numpy()
# ax=data["ax"].to_numpy()
# ay=data["ay"].to_numpy()
# az=data["az"].to_numpy()
# a=np.sqrt(ax**2+ay**2+az**2)


def getDistance(lat1,lon1,lat2,lon2):
    # This uses the haversine formula, which remains a good numberical computation,
    # even at small distances, unlike the Shperical Law of Cosines.
    # This method has ~0.3% error built in.
    R = 6371 # Radius of Earth in km

    dLat = math.radians((lat2) - (lat1))
    dLon = math.radians((lon2) - (lon1))
    lat1 = math.radians((lat1))
    lat2 = math.radians((lat2))

    a = math.sin(dLat/2) * math.sin(dLat/2) + \
        math.cos(lat1) * math.cos(lat2) * math.sin(dLon/2) * math.sin(dLon/2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    d = R * c 

    return d

def gps_distance(latitude,longitude):
    #removing zeros from latitude and longitude data
    latitude=np.trim_zeros(latitude)
    longitude=np.trim_zeros(latitude)
    total_distance = 0
    for i in range(len(latitude)-1):
        d = getDistance(latitude[i],longitude[i],latitude[i+1],longitude[i+1])
        total_distance += d
    return(total_distance)
    

def average_speed(total_distance,total_time):
    return (total_distance/total_time)

def return_stats(data):
    #get some statistical values
    av=np.average(data)
    data=np.trim_zeros(data)
    max_val = np.max(data)
    median_val = np.median(data)
    sd=np.std(data)
    val_85 = max_val*0.85
    return(av,max_val,median_val,sd,val_85);








