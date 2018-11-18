import matplotlib.pyplot as plt
import os
import geopandas as gpd
import pysal as ps
import pandas as pd

os.chdir('C:/Users/gianmarco/Desktop/UNI/Management Engineering/Transportation Economics Management/Project/shape')
province = gpd.read_file('bergamo_municipality_region.shp')
province = province.drop(0)
province.head()
province.plot()

f, ax = plt.subplots(1, figsize=(13, 13))
ax = province.plot(axes=ax)
f.suptitle('Bergamo')
plt.show()

province.geometry.area
province.geometry.area.hist(bins=50)

bounds = province.bounds
bounds

province = province[((bounds['minx'] < 11) & (bounds['maxx'] > 9) & (bounds['miny'] < 46.2) & (bounds['maxy'] > 45.3))]
province = province[province['POLYGON_NM'] != 'Water bodies']

fig, ax = plt.subplots(figsize=(12,10), subplot_kw={'aspect':'equal'})
province.plot(column='POLYGON_NM', ax=ax)
ax.set_xlim(9, 11)
ax.set_ylim(45.3, 46.2)

roads = gpd.read_file('roads.shp')
roads.plot()
roads = roads.drop(0)
roads.head()

fig, ax = plt.subplots(figsize=(14,14), subplot_kw={'aspect':'equal'})
roads.plot(ax=ax, color="black", linewidth=0.4)
province.plot(column='POLYGON_NM', ax=ax)
ax.set_xlim(9.26, 10.27)
ax.set_ylim(45.4, 46.1)
