import numpy as np
import pandas as pd
import scipy
import math
import matplotlib.pyplot as plt


def moving_median_keep_ends(signal, window=3):
    assert window % 2 != 0, "Give an odd number for the window"
    smoothed = np.zeros_like(signal)
    for i, point in enumerate(signal):
        if i < window // 2 + 1:
            smoothed[i] = np.median(signal[: i + window // 2 + 1])
        elif len(smoothed) - i < window // 2 + 1:
            smoothed[i] = np.median(signal[i - window // 2 - 1:])
        else:
            smoothed[i] = np.median(signal[i - window // 2 - 1:i + window // 2 + 1 ])
    return smoothed

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
    median_val = np.median(data)
    p95= np.percentile(data,95)
    return(median_val,p95);


#Rasmussen et al., Improved methods to deduct trip legs and mode from travel surveys using wearable GPS devices: 
#A case study from the Greater Copenhagen area, 2015
def mode_of_transport(p95_speed,p95_acc,median_speed):
        if (median_speed>=8.5):
            return 'car'
        elif (median_speed >=6):
            if p95_acc>0.32:
          
                if p95_speed>=8.5:
                    return 'bus'
                else:
                    return 'car'
            elif p95_speed>=8.5:
                return 'car'
            else:
                return 'bike'
        elif (median_speed>=2):
            if p95_acc>=0.32:
                if (p95_speed>2.5 and p95_speed<8.5):
                    return 'car'
                else:
                    return 'bus'
            elif p95_acc>=0.14:
                if p95_speed>=8.5:
                    return 'bus'
                else: 
                    return 'bike'
            elif p95_speed<2.5:
                return'walk'
            else:
                return 'bike'
        else:
            if p95_acc>=0.32:
                return 'car'
            elif p95_speed>=8.5:
                return'bike'
            else:
                return'walk'
                
        
# Testing
# test_data='Test_data/test2.csv'
# data=pd.read_csv(test_data)
# latitude=data["Latitude"].to_numpy()
# longitude=data['Longitude'].to_numpy()
# speed=data['Speed (m/s)'].to_numpy()
# time=data["time"].to_numpy()
# ax=data["ax"].to_numpy()
# ay=data["ay"].to_numpy()
# az=data["az"].to_numpy()
# a=np.sqrt(ax**2+ay**2)


# median_acc,p95_acc=return_stats(a)
# median_speed,p95_speed=return_stats(speed)
# print(mode_of_transport(p95_speed, p95_acc, median_speed))
   
# plt.plot(a)




