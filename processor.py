# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 19:44:19 2025

@author: lucas
"""

import pandas as pd 
from pprint import pprint
import numpy as np 

'''
https://www.virginiaroads.org/datasets/VDOT::crash-data-1/explore?layer=1
https://www.virginiaroads.org/datasets/crashdata-basic-1/explore?location=37.903145%2C-79.499811%2C6.83&showTable=true
'''

######### BASIC SHEET ############

df_basic = pd.read_csv('CrashData_basic.csv')

df_basic['Crash Date'] = pd.to_datetime(df_basic['Crash Date'], errors='coerce')
df_basic['Month'] = df_basic['Crash Date'].dt.month_name()
df_basic['Day_of_Month'] = df_basic['Crash Date'].dt.day
df_basic['Day_Name'] = df_basic['Crash Date'].dt.day_name()

# Map month number to season
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Fall'
    return None

df_basic['Season'] = df_basic['Crash Date'].dt.month.apply(get_season)

# Time stamp is always either 4am or 5am, so 4 hours timestamp doesnt matter
df_basic.drop(['Crash Date', 'Crash Military Time','Work Zone Location','Work Zone Type','MPO Name',
               'Max Speed Diff','Node','Node Offset (ft)'], 
              axis=1, inplace=True)


df_sample = df_basic.head(1000)

'''
print(df_basic['Crash Year'].unique())

for col in df_basic.select_dtypes(include=['object', 'category']).columns:
    if df_basic[col].nunique(dropna=False) <= 50:
        unique_vals = df_basic[col].value_counts(dropna=False)
        print(f"\n📊 Column: {col} ({len(unique_vals)} unique values)")
        pprint(unique_vals.to_dict())

# Crash Years are 2016-2025
# Crash Date and Crash Military time can probably go
# Crash Severity can probably go because the following columns detail what kind of crash and how many people were impacted
'''
'''
📊 Column: Crash Severity (5 unique values)
{'A': 54683, 'B': 220114, 'C': 88011, 'K': 7465, 'O': 758589}

📊 Column: Collision Type (17 unique values)
{'1. Rear End': 339646,
 '10. Deer': 56200,
 '11. Other Animal': 4459,
 '12. Ped': 13221,
 '13. Bicyclist': 76,
 '14. Motorcyclist': 20,
 '15. Backed Into': 6708,
 '16. Other': 34873,
 '2. Angle': 291616,
 '3. Head On': 24573,
 '4. Sideswipe - Same Direction': 94039,
 '5. Sideswipe - Opposite Direction': 17414,
 '6. Fixed Object in Road': 10071,
 '7. Train': 222,
 '8. Non-Collision': 18436,
 '9. Fixed Object - Off Road': 217287,
 'Not Applicable': 1}

📊 Column: Weather Condition (10 unique values)
{'1. No Adverse Condition (Clear/Cloudy)': 941531,
 '10. Blowing Sand, Soil, Dirt, or Snow': 380,
 '11. Severe Crosswinds': 487,
 '3. Fog': 5306,
 '4. Mist': 14427,
 '5. Rain': 146337,
 '6. Snow': 15404,
 '7. Sleet/Hail': 3527,
 '8. Smoke/Dust': 57,
 '9. Other': 1406}

📊 Column: Light Condition (7 unique values)
{'1. Dawn': 31022,
 '2. Daylight': 738074,
 '3. Dusk': 33198,
 '4. Darkness - Road Lighted': 151984,
 '5. Darkness - Road Not Lighted': 169663,
 '6. Darkness - Unknown Road Lighting': 2840,
 '7. Unknown': 2081}

📊 Column: Roadway Surface Condition (11 unique values)
{'1. Dry': 918939,
 '10. Slush': 802,
 '11. Sand, Dirt, Gravel': 1604,
 '2. Wet': 181896,
 '3. Snowy': 10113,
 '4. Icy': 12383,
 '5. Muddy': 163,
 '6. Oil/Other Fluids': 296,
 '7. Other': 1192,
 '8. Natural Debris': 308,
 '9. Water (Standing, Moving)': 1166}

📊 Column: Relation To Roadway (15 unique values)
{'1. Main-Line Roadway': 205157,
 '10. Intersection Related - Within 150 Feet': 115897,
 '11. Intersection Related - Outside 150 Feet': 14122,
 '12. Crossover Related': 3364,
 '13. Driveway, Alley-Access - Related': 14337,
 '14. Railway Grade Crossing': 567,
 '15. Other Crossing (Crossing for Bikes, School, etc.)': 645,
 '2. Acceleration/Deceleration Lanes': 3886,
 '3. Gore Area (b/w Ramp and Highway Edgelines)': 1445,
 '4. Collector/Distributor Road': 1148,
 '5. On Entrance/Exit Ramp': 26010,
 '6. Intersection at end of Ramp': 4518,
 '7. Other location not listed above within an interchange area (median, shoulder , roadside)': 3938,
 '8. Non-Intersection': 476795,
 '9. Within Intersection': 257033}

📊 Column: Roadway Alignment (10 unique values)
{'1. Straight - Level': 841519,
 '10. On/Off Ramp': 13167,
 '2. Curve - Level': 87028,
 '3. Grade - Straight': 105695,
 '4. Grade - Curve': 51849,
 '5. Hillcrest - Straight': 15101,
 '6. Hillcrest - Curve': 4485,
 '7. Dip - Straight': 5532,
 '8. Dip - Curve': 2926,
 '9. Other': 1560}

📊 Column: Roadway Surface Type (6 unique values)
{'1. Concrete': 43729,
 '2. Blacktop, Asphalt, Bituminous': 1078951,
 '3. Brick or Block': 537,
 '4. Slag, Gravel, Stone': 4127,
 '5. Dirt': 864,
 '6. Other': 654}

📊 Column: Roadway Defect (10 unique values)
{'1. No Defects': 1100887,
 '10. Edge Pavement Drop Off': 1254,
 '2. Holes, Ruts, Bumps': 2836,
 '3. Soft or Low Shoulder': 1784,
 '4. Under Repair': 1800,
 '5. Loose Material': 2161,
 '6. Restricted Width': 661,
 '7. Slick Pavement': 14726,
 '8. Roadway Obstructed': 1112,
 '9. Other': 1641}

📊 Column: Roadway Description (5 unique values)
{'1. Two-Way, Not Divided': 443734,
 '2. Two-Way, Divided, Unprotected Median': 317856,
 '3. Two-Way, Divided, Positive Median Barrier': 328142,
 '4. One-Way, Not Divided': 36560,
 '5. Unknown': 2570}

📊 Column: Intersection Type (6 unique values)
{'1. Not at Intersection': 683791,
 '2. Two Approaches': 43022,
 '3. Three Approaches': 144820,
 '4. Four Approaches': 252646,
 '5. Five-Point, or More': 2324,
 '6. Roundabout': 2259}

📊 Column: Traffic Control Type (18 unique values)
{'1. No Traffic Control': 147321,
 '10. Railroad Crossing With Markings and Signs': 320,
 '11. Railroad Crossing With Signals': 99,
 '12. Railroad Crossing With Gate and Signals': 375,
 '13. Other': 4990,
 '14. Ped Crosswalk': 2962,
 '15. Reduced Speed - School Zone': 262,
 '16. Reduced Speed - Work Zone': 1692,
 '17. Highway Safety Corridor': 12759,
 '2. Officer or Flagger': 1706,
 '3. Traffic Signal': 228264,
 '4. Stop Sign': 99861,
 '5. Slow or Warning Sign': 5256,
 '6. Traffic Lanes Marked': 559515,
 '7. No Passing Lines': 51413,
 '8. Yield Sign': 9544,
 '9. One Way Road or Street': 2514,
 'Not Applicable': 9}

📊 Column: Traffic Control Status (6 unique values)
{'1. Yes - Working': 947778,
 '2. Yes - Working and Obscured': 5422,
 '3. Yes - Not Working': 1811,
 '4. Yes - Not Working and Obscured': 421,
 '5. Yes - Missing': 384,
 '6. No Traffic Control Device Present': 173046}

📊 Column: Work Zone Related (3 unique values)
{'1. Yes': 32875, '2. No': 1095984, 'Not Applicable': 3}

📊 Column: Work Zone Location (5 unique values)
{nan: 1095987,
 '1. Advance Warning Area': 5040,
 '2. Transition Area': 4091,
 '3. Activity Area': 22505,
 '4. Termination Area': 1239}

📊 Column: Work Zone Type (6 unique values)
{nan: 1095986,
 '1. Lane Closure': 7373,
 '2. Lane Shift/Crossover': 2422,
 '3. Work on Shoulder or Median': 18861,
 '4. Intermittent or Moving Work': 1902,
 '5. Other': 2318}

📊 Column: School Zone (4 unique values)
{'1. Yes': 11243,
 '2. Yes - With School Activity': 4092,
 '3. No': 1113526,
 'Not Applicable': 1}

📊 Column: First Harmful Event (42 unique values)
{'1. Bank Or Ledge': 20126,
 '10. Other': 4192,
 '11. Jersey Wall': 15507,
 '12. Building/Structure': 2750,
 '13. Curb': 7740,
 '14. Ditch': 22796,
 '15. Other Fixed Object': 8390,
 '16. Other Traffic Barrier': 1541,
 '17. Traffic Sign Support': 969,
 '18. Mailbox': 4602,
 '19. Ped': 13055,
 '2. Trees': 43371,
 '20. Motor Vehicle In Transport': 743242,
 '21. Train': 232,
 '22. Bicycle': 3676,
 '23. Animal': 60197,
 '24. Work Zone Maintenance Equipment': 362,
 '25. Other Movable Object': 3331,
 '26. Unknown Movable Object': 241,
 '27. Other': 1900,
 '28. Ran Off Road': 31124,
 '29. Jack Knife': 365,
 '3. Utility Pole': 17662,
 '30. Overturn (Rollover)': 16175,
 '31. Downhill Runaway': 83,
 '32. Cargo Loss or Shift': 253,
 '33. Explosion or Fire': 230,
 '34. Separation of Units': 83,
 '35. Cross Median': 765,
 '36. Cross Centerline': 1418,
 '37. Equipment Failure (Tire, etc)': 1673,
 '38. Immersion': 103,
 '39. Fell/Jumped From Vehicle': 1235,
 '4. Fence Or Post': 8754,
 '40. Thrown or Falling Object': 402,
 '41. Non-Collision Unknown': 340,
 '42. Other Non-Collision': 3472,
 '5. Guard Rail': 38864,
 '6. Parked Vehicle': 31364,
 '7. Tunnel, Bridge, Underpass, Culvert, etc.': 4422,
 '8. Sign, Traffic Signal': 9685,
 '9. Impact Cushioning Device': 2170}

📊 Column: First Harmful Event Loc (9 unique values)
{'1. On Roadway': 925136,
 '2. Shoulder': 78931,
 '3. Median': 16010,
 '4. Roadside': 80191,
 '5. Gore': 2026,
 '6. Separator': 1379,
 '7. In Parking Lane or Zone': 6908,
 '8. Off Roadway, Location Unknown': 13380,
 '9. Outside Right-of-Way': 4901}

📊 Column: Alcohol? (2 unique values)
{'No': 1065457, 'Yes': 63405}

📊 Column: Animal Related? (2 unique values)
{'No': 1055800, 'Yes': 73062}

📊 Column: Unrestrained? (2 unique values)
{'Belted': 1082360, 'Unbelted': 46502}

📊 Column: Bike? (2 unique values)
{'No': 1123298, 'Yes': 5564}

📊 Column: Distracted? (2 unique values)
{'No': 924330, 'Yes': 204532}

📊 Column: Drowsy? (2 unique values)
{'No': 1098070, 'Yes': 30792}

📊 Column: Drug Related? (2 unique values)
{'No': 1118763, 'Yes': 10099}

📊 Column: Guardrail Related? (2 unique values)
{'No': 1069940, 'Yes': 58922}

📊 Column: Hitrun? (2 unique values)
{'No': 1043484, 'Yes': 85378}

📊 Column: Lgtruck? (2 unique values)
{'No': 1035509, 'Yes': 93353}

📊 Column: Motorcycle? (2 unique values)
{'No': 1110737, 'Yes': 18125}

📊 Column: Pedestrian? (2 unique values)
{'No': 1114674, 'Yes': 14188}

📊 Column: Speed? (2 unique values)
{'No': 905062, 'Yes': 223800}

📊 Column: RoadDeparture Type (4 unique values)
{'NOT_RD': 895982, 'RD_LEFT': 61561, 'RD_RIGHT': 83399, 'RD_UNKNOWN': 87920}

📊 Column: Intersection Analysis (3 unique values)
{'Not Intersection': 579638,
 'Urban Intersection': 248977,
 'VDOT Intersection': 300247}

📊 Column: Senior? (2 unique values)
{'No': 936624, 'Yes': 192238}

📊 Column: Young? (2 unique values)
{'No': 920446, 'Yes': 208416}

📊 Column: Mainline? (2 unique values)
{'No': 29818, 'Yes': 1099044}

📊 Column: Night? (2 unique values)
{'No': 804375, 'Yes': 324487}

📊 Column: VDOT District (9 unique values)
{'1. Bristol': 48743,
 '2. Salem': 97864,
 '3. Lynchburg': 54202,
 '4. Richmond': 219625,
 '5. Hampton Roads': 244286,
 '6. Fredericksburg': 72347,
 '7. Culpeper': 62369,
 '8. Staunton': 82660,
 '9. Northern Virginia': 246766}

📊 Column: Functional Class (8 unique values)
{nan: 14131,
 '1-Interstate (A,1)': 202159,
 '2-Principal Arterial - Other Freeways and Expressways (B)': 33888,
 '3-Principal Arterial - Other (E,2)': 290868,
 '4-Minor Arterial (H,3)': 267654,
 '5-Major Collector (I,4)': 153014,
 '6-Minor Collector (5)': 31940,
 '7-Local (J,6)': 135208}

📊 Column: Facility Type (6 unique values)
{nan: 23711,
 '1-One-Way Undivided': 45404,
 '2-One-Way Divided': 108,
 '3-Two-Way Undivided': 488354,
 '4-Two-Way Divided': 570486,
 '5-Reversible Exclusively (e.g. 395R)': 799}

📊 Column: Area Type (2 unique values)
{'Rural': 283225, 'Urban': 845637}

📊 Column: SYSTEM (5 unique values)
{'NonVDOT primary': 179719,
 'NonVDOT secondary': 209912,
 'VDOT Interstate': 196007,
 'VDOT Primary': 304309,
 'VDOT Secondary': 238915}

📊 Column: Ownership (6 unique values)
{'1. State Hwy Agency': 739231,
 '2. County Hwy Agency': 34455,
 '3. City or Town Hwy Agency': 345626,
 '4. Federal Roads': 2292,
 '5. Toll Roads Maintained by Others': 1794,
 '6. Private/Unknown Roads': 5464}

📊 Column: Planning District (25 unique values)
{'Accomack-Northampton': 7175,
 'Central Shenandoah': 46525,
 'Commonwealth Regional': 12236,
 'Crater': 29754,
 'Crater, Hampton Roads': 870,
 'Cumberland Plateau': 12951,
 'George Washington Regional': 57300,
 'Hampton Roads': 230453,
 'Lenowisco': 10419,
 'Middle Peninsula': 7264,
 'Middle Peninsula, Hampton Roads': 3584,
 'Mount Rogers': 32055,
 'New River Valley': 25007,
 'Northern Neck': 4199,
 'Northern Shenandoah Valley': 32818,
 'Northern Virginia': 246766,
 'Rappahannock - Rapidan': 28740,
 'Region 2000': 32339,
 'Richmond Regional': 131812,
 'Richmond Regional, Crater': 51226,
 'Roanoke Valley-Alleghany': 43217,
 'Roanoke Valley-Alleghany, West Piedmont': 7760,
 'Southside': 12445,
 'Thomas Jefferson': 36314,
 'West Piedmont': 25633}

📊 Column: MPO Name (16 unique values)
{nan: 245497,
 'BRIS': 8638,
 'CVIL': 19611,
 'DAN': 11241,
 'FRED': 48120,
 'HAMP': 230670,
 'HAR': 13137,
 'KING': 1451,
 'LYN': 21007,
 'NOVA': 249636,
 'NRV': 13948,
 'RICH': 177575,
 'ROAN': 35878,
 'SAW': 13770,
 'TCAT': 25228,
 'WINC': 13455}
'''



######## DETAILS SHEET ###########

df_details = pd.read_csv('CrashData_details.csv')

'''
for col in df_details.select_dtypes(include=['object', 'category']).columns:
    if df_details[col].nunique(dropna=False) <= 50:
        unique_vals_details = df_details[col].value_counts(dropna=False)
        print(f"\n📊 Column: {col} ({len(unique_vals)} unique values)")
        pprint(unique_vals_details.to_dict())

set(df_basic['Document Nbr']) == set(df_details['Document_Nbr'])  # shows we can join

print(len(df_details['Vehicle_Maneuver_Type_Cd'].unique()))
print(df_details['Speed_Posted'].unique())   # speed limit
print(df_details['Speed_Max_Safe'].unique())  # max speed recommended for conditions
print(df_details['Vehicle_Year_Nbr'].unique())
'''

df_to_merge = df_details[['Document_Nbr','Speed_Posted','Speed_Max_Safe','Vehicle_Year_Nbr']].copy()

def clean_speed_limit(val):
    try:
        # Convert to string and split by semicolon
        parts = str(val).split(';')

        # Loop through each part to find the first valid integer ≥ 15
        for part in parts:
            part = part.strip()
            if part.isdigit():  # only allow whole numbers
                num = int(part)
                if 15 <= num <= 100:  # reasonable speed limits
                    floored = num - (num % 5)
                    # print(f"✅ Got {num} → floored to {floored}")
                    return floored
        return None
    except Exception:
        return None

# Clean Speed_Posted
df_to_merge['Speed_Posted_Clean'] = df_to_merge['Speed_Posted'].apply(clean_speed_limit)
value_counts = df_to_merge['Speed_Posted_Clean'].value_counts(normalize=True, dropna=True)
speed_values = value_counts.index.to_numpy()
probabilities = value_counts.values
mask = df_to_merge['Speed_Posted_Clean'].isna()
imputed_values = np.random.choice(speed_values, size=mask.sum(), p=probabilities)
df_to_merge.loc[mask, 'Speed_Posted_Clean'] = imputed_values  # ✅ correct column

# Clean Speed_Max_Safe
df_to_merge['Speed_Max_Safe_Cleaned'] = df_to_merge['Speed_Max_Safe'].apply(clean_speed_limit)
value_counts = df_to_merge['Speed_Max_Safe_Cleaned'].value_counts(normalize=True, dropna=True)
speed_values = value_counts.index.to_numpy()
probabilities = value_counts.values
mask = df_to_merge['Speed_Max_Safe_Cleaned'].isna()
imputed_values = np.random.choice(speed_values, size=mask.sum(), p=probabilities)
df_to_merge.loc[mask, 'Speed_Max_Safe_Cleaned'] = imputed_values  # ✅ fixed this!


def extract_vehicle_year_stats(val):
    try:
        parts = str(val).split(';')
        years = []

        for part in parts:
            part = part.strip()
            if part.isdigit():
                year = int(part)
                if 1900 <= year <= 2100:  # sanity check
                    years.append(year)

        if not years:
            return (None, None)

        avg = round(sum(years) / len(years))
        rng = max(years) - min(years)
        return (avg, rng)
    except:
        return (None, None)
    
df_to_merge[['Vehicle_Year_Avg', 'Vehicle_Year_Range']] = df_to_merge['Vehicle_Year_Nbr']\
    .apply(extract_vehicle_year_stats)\
    .apply(pd.Series)
df_to_merge.drop(['Speed_Posted', 'Speed_Max_Safe', 'Vehicle_Year_Nbr'], axis=1, inplace=True)

df_merged = df_basic.merge(
    df_to_merge,
    left_on='Document Nbr',
    right_on='Document_Nbr',
    how='left')
df_merged.drop(columns='Document_Nbr', inplace=True)

df_sample2 = df_merged.head(200)

csv_filename = "df_merged.csv"  
df_merged.to_csv(csv_filename, index=False)
print(f"\nData saved to {csv_filename}")