# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

birddata = pd.read_csv("bird_tracking.csv", index_col = 0)
bird_names = pd.unique(birddata.bird_name)

import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mercator()

plt.figure(figsize=(10,10))

ax = plt.axes(projection=proj)
ax.set_extent((-25, 20, 52, 20))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=":")

for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    ax.plot(x, y, ".", transform = ccrs.Geodetic(), label = bird_name)
    
plt.legend(loc = "upper left")
plt.savefig("map.pdf")

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))
        
birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)

data = birddata[birddata.bird_name == "Eric"]
times = data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time)/datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []

for (i,t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []
        
plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.savefig("dms.pdf")
        
plt.figure()

data = birddata[birddata.bird_name == "Eric"]
times = data.timestamp
elapsed_time = [time - times[0] for time in times]
plt.plot(np.array(elapsed_time)/datetime.timedelta(days=1))

plt.xlabel("Observation")
plt.ylabel("Elapsed time (days)");
plt.savefig("timeplot.pdf")

plt.figure()
speed = birddata.speed_2d[birddata.bird_name == "Eric"]
ind = np.isnan(speed)
plt.figure(figsize=(8,4))
plt.hist(speed[~ind], bins = np.linspace(0, 30, 20), density = True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency")

plt.figure(figsize=(8,4))
birddata.speed_2d.plot(kind="hist", range=[0,30])
plt.xlabel("2D speed (m/s)")
plt.savefig("hist_pandas.pdf");
