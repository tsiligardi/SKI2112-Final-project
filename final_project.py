import numpy as np
import pandas as pd
import scipy
import math
import matplotlib.pyplot as plt


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
    

def remove_outliers(data,thr=1.5):
    #removing outlier using IQR ranges
    Q1=np.percentile(data, 25)
    Q3=np.percentile(data, 75)
    IQR=Q3-Q1
    return data[(data >= Q1-thr*IQR) & (data<Q3+IQR)]

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
                
def transport_no_acc(p95_speed,median_speed):
        if (median_speed>=8.5):
            return 'car'
        elif (median_speed >=6):
            if p95_speed>=8.5:
                return 'bus or car'
            else:
                return 'car or bike'
        elif (median_speed>=2):
            if p95_speed >= 8.5:
                return 'bus'
            elif p95_speed>=2.5:
                return 'car or bike'
            else:
                return 'walk'
        else:
            if p95_speed<2.5:
                return'walk'
            else:
                return 'bike'   
        
#Testing
# test_data='Test_data/walkie.csv'
# data=pd.read_csv(test_data)
# latitude=data["Latitude"].to_numpy()
# longitude=data['Longitude'].to_numpy()
# speed=data['Speed (m/s)'].to_numpy()
# time=data["time"].to_numpy()
# ax=data["ax"].to_numpy()
# ay=data["ay"].to_numpy()
# az=data["az"].to_numpy()
# a=np.sqrt(ax**2+ay**2)

# a_filter=remove_outliers(a)
# speed_filter=remove_outliers(speed)
# median_acc,p95_acc=return_stats(a_filter)
# median_speed,p95_speed=return_stats(speed_filter)
# print(mode_of_transport(p95_speed, p95_acc, median_speed))
# print(transport_no_acc(p95_speed, median_speed))
   




