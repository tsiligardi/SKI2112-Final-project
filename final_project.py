import numpy as np
import pandas as pd
import scipy
import math
import matplotlib.pyplot as plt


#testing
data=pd.read_csv('test.csv')
latitude = data["Latitude"].to_numpy()[1:]#Exclude first data point, since it is 0
longitude = data["Longitude"].to_numpy()[1:]
ax=data["ax"].to_numpy()
ay=data["az"].to_numpy()
az=data["az"].to_numpy()
a_tot=np.sqrt(ax**2+ay**2+az**2)
time=data['time'].to_numpy()
speed=data['Speed (m/s)'].to_numpy()

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
    total_distance = 0
    for i in range(len(latitude)-1):
        d = getDistance(latitude[i],longitude[i],latitude[i+1],longitude[i+1])
        total_distance += d
    return(total_distance)
        
 

def average_speed(total_acceleration,time):
    #To calculate the average speed, we can use the integral-mean theorem:
    #v_avg=1/(t_final-t_initial)*int^(t_final)_(t_initial)(total_acceleration)dt
    v_avg=1/(time[len(time)-1]-time[0])*scipy.integrate.simpson(total_acceleration,time)
    return v_avg


def get_velocity(total_acceleration,time):
    #for a small interval dt
    #v(t_2)=a(t_1)*dt+v(t_1)
    v=np.zeros(len(total_acceleration))
    for i in range((len(total_acceleration)-1)):
        v[i+1]=(total_acceleration[i]*(time[i+1]-time[i]))+v[i]
    return v

def get_total_distance(velocity,time):
    #One way to calculate the total distance, is by taking the integral of the velocity
    total_distance=scipy.integrate.simpson(velocity,time)
    return total_distance


