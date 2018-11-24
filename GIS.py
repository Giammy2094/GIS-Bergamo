#Importing libraries and packages
import matplotlib.pyplot as plt
import os
import geopandas as gpd
import pysal as ps
import pandas as pd
from shapely.geometry import Point

#change directory
os.chdir('C:/Users/gianmarco/Desktop/UNI/Management Engineering/Transportation Economics Management/Project/shape')
#read shapefile
province = gpd.read_file('bergamo_municipality_region.shp')
#drop null
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
ax.set_xlim(9.39, 10.27)
ax.set_ylim(45.4, 46.1)

#read roads shapefile
roads = gpd.read_file('roads.shp')
roads.head()

#set roads bounds
roads_bounds = roads.bounds
roads_bounds

roads = roads[((roads_bounds['minx'] < 11) & (roads_bounds['maxx'] > 9) & (roads_bounds['miny'] < 46.2) & (roads_bounds['maxy'] > 45.3))]
roads = roads[roads['id'] != 'Water bodies']

#plot roads on province
fig, ax = plt.subplots(figsize=(14,14), subplot_kw={'aspect':'equal'})
roads.plot(ax=ax, color="black", linewidth=0.4)
province.plot(column='POLYGON_NM', ax=ax)
ax.set_xlim(9.39, 10.27)
ax.set_ylim(45.4, 46.1)

#read water shapefile
water = gpd.read_file('water.shp')
water.head()

#set water bounds
water_bounds = water.bounds
water_bounds

water = water[((water_bounds['minx'] < 11) & (water_bounds['maxx'] > 9) & (water_bounds['miny'] < 46.2) & (water_bounds['maxy'] > 45.3))]
water = water[water['id'] != 'Water bodies']

#plot road, water on province
fig, ax = plt.subplots(figsize=(100,100), subplot_kw={'aspect':'equal'})
roads.plot(ax=ax, color='black', linewidth=0.4)
water.plot(ax=ax, color='blue')
province.plot(column='POLYGON_NM', ax=ax)
ax.set_xlim(9.39, 10.27)
ax.set_ylim(45.4, 46.1)

#read railways shapefile
rail = gpd.read_file('railways.shp')
rail.head()

#set railways bounds
rail_bounds = rail.bounds
rail_bounds

rail = rail[((rail_bounds['minx'] < 11) & (rail_bounds['maxx'] > 9) & (rail_bounds['miny'] < 46.2) & (rail_bounds['maxy'] > 45.3))]
rail = rail[rail['id'] != 'Water bodies']
rail.head()

bridge_point = Point(9.692472, 45.693500)
bridge_point_series = gpd.GeoSeries([bridge_point])
bridge_bounds = bridge_point_series.bounds
bridge_bounds
bridge_point_series = bridge_point_series[((bridge_bounds['minx'] < 11) & (bridge_bounds['maxx'] > 9) & (bridge_bounds['miny'] < 46.2) & (bridge_bounds['maxy'] > 45.3))]
#plot rail, road and water on province
fig, ax = plt.subplots(figsize=(110,110), subplot_kw={'aspect':'equal'})
province.plot(column='POLYGON_NM', ax=ax)
roads.plot(ax=ax, color='black', linewidth=0.4)
rail.plot(ax=ax, color='orange',linewidth=0.6)
bridge_point_series.plot(ax=ax, color='red')
water.plot(ax=ax, color='blue')
ax.set_xlim(9.39, 10.27)
ax.set_ylim(45.4, 46.1)
