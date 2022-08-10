import pandas as pd
from scipy.spatial import distance
from math import sin, cos, sqrt, atan2, radians
import time

permits_man = pd.read_csv('permits_man.csv')
nypd2014_man = pd.read_csv('nypd2014_man.csv')

def get_distance(point1, point2):
    R = 4182 #miles
    lat1 = radians(point1[0])  #insert value
    lon1 = radians(point1[1])
    lat2 = radians(point2[0])
    lon2 = radians(point2[1])

    dlon = lon2 - lon1
    dlat = lat2- lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance

# note: the latitude and longitude I'm using are in decimals NOT minutes, so I do the same here
# these are set at a tenth of a mile to start, with 1 degree late = 69 miles and 1 degree longitude = 40 miles
max_delt_lat = 1/690
max_delt_long = 1/400

permits_man.loc[0, 'complaints2014_15'] = 0

t0 = time.time()
for i in [0]:
    lat = permits_man.loc[i, 'latitude']
    long = permits_man.loc[i, 'longitude']
    point1 = [lat, long]
    #date = permits.loc[i, 'job_start_date']
    complaint_count = 0
    for n in nypd2014_man.index:
        n_lat = nypd2014_man.loc[n, 'latitude']
        n_long = nypd2014_man.loc[n, 'longitude']
        if (abs(lat - n_lat)<= max_delt_lat) or (abs(lat - n_long)<= max_delt_long):
            point2 = [n_lat, n_long]
            distance = get_distance(point1, point2)
            if distance <= .1:
                complaint_count += 1
    permits_man.loc[i, 'complaints2014_15'] = complaint_count

print('')
print("Time to run", time.time()-t0)

permits_man.to_csv('permits_complaints2014_man.csv')