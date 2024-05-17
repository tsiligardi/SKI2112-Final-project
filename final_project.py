import numpy as np
import pandas as pd
import scipy



def average_speed(total_acceleration,time):
    #To calculate the average speed, we can use the integral-mean theorem:
    #v_avg=1/(t_final-t_initial)*int^(t_final)_(t_initial)(total_acceleration)dt
    v_avg=1/(time[len(time)-1]-time[0])*scipy.integrate.trapezoid(total_acceleration,time)
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
    total_distance=scipy.integrate.trapezoid(velocity,time)
    return total_distance
    



