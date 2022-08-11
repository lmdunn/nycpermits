import pandas as pd
from scipy.spatial import distance
from math import sin, cos, sqrt, atan2, radians
import time

permits = pd.read_csv('random_points.csv')
nypd = pd.read_csv('nypd_min.csv')

def get_distance(point1, point2):
    R = 4182 #miles
    lat1 = radians(point1[0])
    lon1 = radians(point1[1])
    lat2 = radians(point2[0])
    lon2 = radians(point2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance


# note: the latitude and longitude I'm using are in decimals NOT minutes, so I do the same here
# these are set at a tenth of a mile to start, with 1 degree late = 69 miles and 1 degree longitude = 40 miles
#max_delt_lat = 1/690
#max_delt_long = 1/400
#hard coded to save time


t0 = time.time()
for i in permits.index:
    t1 = time.time()
    print(f'Index {i} started')
    lat = permits.loc[i, 'latitude']
    long = permits.loc[i, 'longitude']
    point1 = [lat, long]
    complaint_count = 0
    for n in nypd.index:
        #if permits.loc[i, 'borough'] == nypd.loc[n, 'boro_nm']:
        n_lat = nypd.loc[n, 'latitude']
        n_long = nypd.loc[n, 'longitude']
        if (abs(lat - n_lat)<= 1/690) or (abs(lat - n_long)<= 1/400):
            point2 = [n_lat, n_long]
            distance = get_distance(point1, point2)
            if distance <= .1:
                complaint_count += 1
    permits.loc[i, 'total_complaints'] = complaint_count
    print(f"For index {i}, the complaint count was {complaint_count}")
    print(f"Permit {i} finished at {time.time()}, after {time.time()-t1}, {time.time()-t0} since the start of the code.")

permits.to_csv('random_points_nypd.csv')
print('')
print("Time to run", time.time()-t0)