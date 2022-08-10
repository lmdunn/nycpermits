import pandas as pd
from scipy.spatial import distance
from math import sin, cos, sqrt, atan2, radians
import time

#Brooklyn only because this part failed

permits_bk2 = pd.read_csv('boro_data/permits_bk2.csv')
permits_bk3 = pd.read_csv('boro_data/permits_bk3.csv')
nypd_bk = pd.read_csv('big_data/nypd2014_bk.csv') #CHANGE YEAR

def get_distance(point1, point2):
    R = 4182 #miles
    lat1 = radians(point1[0])
    lon1 = radians(point1[1])
    lat2 = radians(point2[0])
    lon2 = radians(point2[1])

    dlon = lon2 - lon1
    dlat = lat2- lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance


# BROOKLYN (BK) 2
t0 = time.time()
print('Processing Brooklyn 2')
permits_bk2.loc[0, 'complaints2014_15'] = 0 #CHANGE YEAR
for i in permits_bk2.index:
    lat = permits_bk2.loc[i, 'latitude']
    long = permits_bk2.loc[i, 'longitude']
    point1 = [lat, long]
    complaint_count = 0
    for n in nypd_bk.index:
        n_lat = nypd_bk.loc[n, 'latitude']
        n_long = nypd_bk.loc[n, 'longitude']
        if (abs(lat - n_lat)<= 1/690) or (abs(lat - n_long)<= 1/400):
            point2 = [n_lat, n_long]
            distance = get_distance(point1, point2)
            if distance <= .1:
                complaint_count += 1
    permits_bk2.loc[i, 'complaints2014_15'] = complaint_count #CHANGE YEAR

permits_bk2.to_csv('permits_complaints2014_bk2.csv') #CHANGE YEAR

print('')
print("Time to run Brooklyn 2:", time.time()-t0)


# BROOKLYN (BK) 3
t0 = time.time()
print('Processing Brooklyn 3')
permits_bk3.loc[0, 'complaints2014_15'] = 0 #CHANGE YEAR
for i in permits_bk3.index:
    lat = permits_bk3.loc[i, 'latitude']
    long = permits_bk3.loc[i, 'longitude']
    point1 = [lat, long]
    complaint_count = 0
    for n in nypd_bk.index:
        n_lat = nypd_bk.loc[n, 'latitude']
        n_long = nypd_bk.loc[n, 'longitude']
        if (abs(lat - n_lat)<= 1/690) or (abs(lat - n_long)<= 1/400):
            point2 = [n_lat, n_long]
            distance = get_distance(point1, point2)
            if distance <= .1:
                complaint_count += 1
    permits_bk3.loc[i, 'complaints2014_15'] = complaint_count #CHANGE YEAR

permits_bk3.to_csv('permits_complaints2014_bk3.csv')

print('')
print("Time to run Brooklyn:", time.time()-t0)