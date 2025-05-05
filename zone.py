# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 20:51:19 2025

@author: lucas
"""

import pandas as pd 
from math import cos, radians
import numpy as np

df = pd.read_csv('CrashData_trimmed.csv')
df = df.dropna(subset=['x', 'y'])

# y is latitude, x is longitude

# Making 20x20mi zones and 10x10
avg_lat = 37.5
delta_lat = 20 / 69 
delta_lon = 20 / (69 * cos(radians(avg_lat)))

delta_lat_10 = 10 / 69
delta_lon_10 = 10 / (69 * cos(radians(37.5)))

delta_lat_5 = 5 / 69
delta_lon_5 = 5 / (69 * cos(radians(avg_lat)))

# 1 degree lat = 69 miles so 20 mi/69 = the degrees for the 20x20 range
# longitude has a little bit more to the formula to account for longitude lines getting narrower going away from equator

# Target center point (center of VA)
center_x = -78.0249  # longitude
center_y = 37.9268   # latitude

# Find all rows within 20-mile box
mask = (
    (df['x'] >= center_x - delta_lon) & (df['x'] <= center_x + delta_lon) &
    (df['y'] >= center_y - delta_lat) & (df['y'] <= center_y + delta_lat)
)

# This mask setss up finding all the crashes that fall within the box

df_in_radius = df[mask]  # applies the mask to find those crashes

df_in_radius = df[mask] # saving it to a new df

# 20-mile buckets
df['x_bucket'] = (df['x'] / delta_lon).astype(int)
df['y_bucket'] = (df['y'] / delta_lat).astype(int)
df['zone'] = df['x_bucket'].astype(str) + "_" + df['y_bucket'].astype(str)

# 10-mile buckets
df['x_bucket_10'] = (df['x'] / delta_lon_10).astype(int)
df['y_bucket_10'] = (df['y'] / delta_lat_10).astype(int)
df['zone_10'] = df['x_bucket_10'].astype(str) + "_" + df['y_bucket_10'].astype(str)

# 5-mile buckets
df['x_bucket_5'] = (df['x'] / delta_lon_5).astype(int)
df['y_bucket_5'] = (df['y'] / delta_lat_5).astype(int)
df['zone_5'] = df['x_bucket_5'].astype(str) + "_" + df['y_bucket_5'].astype(str)

# Count crashes per zone
df.groupby('zone').size().reset_index(name='crash_count')

# Getting center points
zone_centers = df.groupby('zone').agg({
    'x_bucket': 'first',  # these define the zone's position
    'y_bucket': 'first'
}).reset_index()

# 20-mile zone centroids
zone_centers = df.groupby('zone').agg({'x_bucket': 'first', 'y_bucket': 'first'}).reset_index()
zone_centers['center_x'] = zone_centers['x_bucket'] * delta_lon + delta_lon / 2
zone_centers['center_y'] = zone_centers['y_bucket'] * delta_lat + delta_lat / 2
df = df.merge(zone_centers[['zone', 'center_x', 'center_y']], on='zone', how='left')

# 10-mile zone centroids
zone_10_centers = df.groupby('zone_10').agg({'x_bucket_10': 'first', 'y_bucket_10': 'first'}).reset_index()
zone_10_centers['center_x_10'] = zone_10_centers['x_bucket_10'] * delta_lon_10 + delta_lon_10 / 2
zone_10_centers['center_y_10'] = zone_10_centers['y_bucket_10'] * delta_lat_10 + delta_lat_10 / 2
df = df.merge(zone_10_centers[['zone_10', 'center_x_10', 'center_y_10']], on='zone_10', how='left')

# 5-mile zone centroids
zone_5_centers = df.groupby('zone_5').agg({'x_bucket_5': 'first', 'y_bucket_5': 'first'}).reset_index()
zone_5_centers['center_x_5'] = zone_5_centers['x_bucket_5'] * delta_lon_5 + delta_lon_5 / 2
zone_5_centers['center_y_5'] = zone_5_centers['y_bucket_5'] * delta_lat_5 + delta_lat_5 / 2
df = df.merge(zone_5_centers[['zone_5', 'center_x_5', 'center_y_5']], on='zone_5', how='left')

df_sample = df.head(100)
print(df['center_x_5'].nunique())

csv_filename = "df_zones.csv"  
df.to_csv(csv_filename, index=False)
print(f"\nData saved to {csv_filename}")
