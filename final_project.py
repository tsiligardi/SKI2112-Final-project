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



