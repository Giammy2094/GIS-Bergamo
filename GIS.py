#Importing libraries and packages
import matplotlib.pyplot as plt
import os
import geopandas as gpd
import pysal as ps
import pandas as pd

#change directory
os.chdir('C:/Users/gianmarco/Desktop/UNI/Management Engineering/Transportation Economics Management/Project/shape')
#read shapefile
province = gpd.read_file('bergamo_municipality_region.shp')
#drop null
province = province.drop(0)
province.head()
province.plot()

#plot with options
f, ax = plt.subplots(1, figsize=(13, 13))
ax = province.plot(axes=ax)
f.suptitle('Bergamo')
plt.show()


province.geometry.area
province.geometry.area.hist(bins=50)

#set bounds
bounds = province.bounds
bounds

#restricting data
province = province[((bounds['minx'] < 11) & (bounds['maxx'] > 9) & (bounds['miny'] < 46.2) & (bounds['maxy'] > 45.3))]
province = province[province['POLYGON_NM'] != 'Water bodies']

fig, ax = plt.subplots(figsize=(12,10), subplot_kw={'aspect':'equal'})
province.plot(column='POLYGON_NM', ax=ax)
ax.set_xlim(9.39, 11)
ax.set_ylim(45.4, 46.2)

#read road shapefile
roads = gpd.read_file('roads.shp')
roads = roads.drop(0)
roads.head()

bounds = roads.bounds
bounds

roads = roads[((bounds['minx'] < 11) & (bounds['maxx'] > 9) & (bounds['miny'] < 46.2) & (bounds['maxy'] > 45.3))]
roads = roads[roads['id'] != 'Water bodies']

fig, ax = plt.subplots(figsize=(14,14), subplot_kw={'aspect':'equal'})
roads.plot(ax=ax, color="black", linewidth=0.4)
province.plot(column='POLYGON_NM', ax=ax)
ax.set_xlim(9.39, 10.27)
ax.set_ylim(45.4, 46.1)
