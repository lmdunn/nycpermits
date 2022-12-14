import pandas as pd
from scipy.spatial import distance
from math import sin, cos, sqrt, atan2, radians
import time

#I'm naming this by borough without year in order to
#make it as easy as possible to duplicate this code for later years

#file paths are written for folders uploaded to a remote server and will need to be changed
#if this is run on the computer

permits_man = pd.read_csv('data_permits_by_boro/permits_man.csv')
nypd_man = pd.read_csv('data_nypd_by_year/2015/nypd2015_man.csv') #CHANGE YEAR

permits_bx = pd.read_csv('data_permits_by_boro/permits_bx.csv')
nypd_bx = pd.read_csv('data_nypd_by_year/2015/nypd2015_bx.csv') #CHANGE YEAR

permits_si = pd.read_csv('data_permits_by_boro/permits_si.csv')
nypd_si = pd.read_csv('data_nypd_by_year/2015/nypd2015_si.csv') #CHANGE YEAR

permits_qn = pd.read_csv('data_permits_by_boro/permits_qn.csv')
nypd_qn = pd.read_csv('data_nypd_by_year/2015/nypd2015_qn.csv') #CHANGE YEAR

permits_bk = pd.read_csv('data_permits_by_boro/permits_bk.csv')
nypd_bk = pd.read_csv('data_nypd_by_year/2015/nypd2015_bk.csv') #CHANGE YEAR

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

# note: the latitude and longitude I'm using are in decimals NOT minutes, so I do the same here
# these are set at a tenth of a mile to start, with 1 degree late = 69 miles and 1 degree longitude = 40 miles
# max_delt_lat = 1/690
# max_delt_long = 1/400
# to make the code run a little faster I hard coded these variables


# MANHATTAN (MAN)
t0 = time.time()
print('Processing Manhattan')
permits_man.loc[0, 'complaints2015_16'] = 0 #CHANGE YEAR
for i in permits_man.index:
    t1 = time.time()
    lat = permits_man.loc[i, 'latitude']
    long = permits_man.loc[i, 'longitude']
    point1 = [lat, long]
    complaint_count = 0
    for n in nypd_man.index:
        n_lat = nypd_man.loc[n, 'latitude']
        n_long = nypd_man.loc[n, 'longitude']
        if (abs(lat - n_lat)<= 1/690) or (abs(lat - n_long)<= 1/400):
            point2 = [n_lat, n_long]
            distance = get_distance(point1, point2)
            if distance <= .1:
                complaint_count += 1
    permits_man.loc[i, 'complaints2015_16'] = complaint_count #CHANGE YEAR
    print(f"Manhattan permit {i} finished at {time.time()}, after {time.time()-t1}, {time.time()-t0} since the start of the Manhattan code.")

permits_man.to_csv('permits_complaints2015_man.csv', index = False) #CHANGE YEAR

print('')
print("Time to run Manhattan:", time.time()-t0) #


# THE BRONX (BX)
t0 = time.time()
print('Processing the Bronx')
permits_bx.loc[0, 'complaints2015_16'] = 0 #CHANGE YEAR
for i in permits_bx.index:
    t1 = time.time()
    lat = permits_bx.loc[i, 'latitude']
    long = permits_bx.loc[i, 'longitude']
    point1 = [lat, long]
    complaint_count = 0
    for n in nypd_bx.index:
        n_lat = nypd_bx.loc[n, 'latitude']
        n_long = nypd_bx.loc[n, 'longitude']
        if (abs(lat - n_lat)<= 1/690) or (abs(lat - n_long)<= 1/400):
            point2 = [n_lat, n_long]
            distance = get_distance(point1, point2)
            if distance <= .1:
                complaint_count += 1
    permits_bx.loc[i, 'complaints2015_16'] = complaint_count #CHANGE YEAR
    print(f"Bronx permit {i} finished at {time.time()}, after {time.time()-t1}, {time.time()-t0} since the start of the Bronx code.")

permits_bx.to_csv('permits_complaints2015_bx.csv', index = False) #CHANGE YEAR

print('')
print("Time to run the Bronx:", time.time()-t0) #CHANGE BOROUGH


# STATEN ISLAND (SI)
t0 = time.time()
print('Processing Staten Island')
permits_si.loc[0, 'complaints2015_16'] = 0 #CHANGE YEAR
for i in permits_si.index:
    t1 = time.time()
    lat = permits_si.loc[i, 'latitude']
    long = permits_si.loc[i, 'longitude']
    point1 = [lat, long]
    complaint_count = 0
    for n in nypd_si.index:
        n_lat = nypd_si.loc[n, 'latitude']
        n_long = nypd_si.loc[n, 'longitude']
        if (abs(lat - n_lat)<= 1/690) or (abs(lat - n_long)<= 1/400):
            point2 = [n_lat, n_long]
            distance = get_distance(point1, point2)
            if distance <= .1:
                complaint_count += 1
    permits_si.loc[i, 'complaints2015_16'] = complaint_count #CHANGE YEAR
    print(f"Staten Island permit {i} finished at {time.time()}, after {time.time()-t1}, {time.time()-t0} since the start of the Staten Island code.")

permits_si.to_csv('permits_complaints2015_si.csv', index = False) #CHANGE YEAR

print('')
print("Time to run Staten Island:", time.time()-t0)


# QUEENS (QN)
t0 = time.time()
print('Processing Queens')
permits_qn.loc[0, 'complaints2015_16'] = 0 #CHANGE YEAR
for i in permits_qn.index:
    t1 = time.time()
    lat = permits_qn.loc[i, 'latitude']
    long = permits_qn.loc[i, 'longitude']
    point1 = [lat, long]
    complaint_count = 0
    for n in nypd_qn.index:
        n_lat = nypd_qn.loc[n, 'latitude']
        n_long = nypd_qn.loc[n, 'longitude']
        if (abs(lat - n_lat)<= 1/690) or (abs(lat - n_long)<= 1/400):
            point2 = [n_lat, n_long]
            distance = get_distance(point1, point2)
            if distance <= .1:
                complaint_count += 1
    permits_qn.loc[i, 'complaints2015_16'] = complaint_count #CHANGE YEAR
    print(f"Queens permit {i} finished at {time.time()}, after {time.time()-t1}, {time.time()-t0} since the start of the Queens code.")

permits_qn.to_csv('permits_complaints2015_qn.csv', index = False) #CHANGE YEAR

print('')
print("Time to run Queens:", time.time()-t0)


# BROOKLYN (BK)
t0 = time.time()
print('Processing Brooklyn')
permits_bk.loc[0, 'complaints2015_16'] = 0 #CHANGE YEAR
for i in permits_bk.index:
    t1 = time.time()
    lat = permits_bk.loc[i, 'latitude']
    long = permits_bk.loc[i, 'longitude']
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
    permits_bk.loc[i, 'complaints2015_16'] = complaint_count #CHANGE YEAR
    print(f"Brooklyn permit {i} finished at {time.time()}, after {time.time()-t1}, {time.time()-t0} since the start of the Brooklyn code.")


permits_bk.to_csv('permits_complaints2015_bk.csv', index = False) #CHANGE YEAR

print('')
print("Time to run Brooklyn:", time.time()-t0)