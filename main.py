import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

#Import Data
df = pd.read_csv('nyc_crime.csv')

#Clean Data
df.drop(['HADEVELOPT', 'CMPLNT_TO_DT', 'CMPLNT_TO_TM', 'HOUSING_PSA', 'PREM_TYP_DESC', 'JURISDICTION_CODE', 'JURIS_DESC', 'LOC_OF_OCCUR_DESC', 'PARKS_NM', 'STATION_NAME', 'TRANSIT_DISTRICT'], axis=1, inplace=True)
df = df.rename(columns={"BORO_NM": "BOROUGH", "CMPLNT_FR_DT": "DATE", "CMPLNT_FR_TM": "TIME", "LAW_CAT_CD": "OFFENSE LEVEL", "ADDR_PCT_CD": "PRECINT", "PD_DESC": "OFFENSE_NAME"})
df["BOROUGH"].fillna("UNKNOWN", inplace = True) 
df['DATE'] = pd.to_datetime(df['DATE'])
df['RPT_DT'] = pd.to_datetime(df['RPT_DT'], errors='coerce')
df['YEAR'] = df['DATE'].dt.year
df['MONTH'] = df['DATE'].dt.month
df['DAY'] = df['DATE'].dt.day
df = df.sort_values('DATE')

# Crime district gorupy
crime_district = df.groupby(["PRECINT", "OFNS_DESC"])
crime_district = crime_district.count()["CMPLNT_NUM"].unstack()
print(crime_district)