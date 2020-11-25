import pandas as pd
from netCDF4 import Dataset
import numpy as np
import csv
import time
import time as stopWatch
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
import math
import datetime
massRate = .15
massFlowData = list()
length = 150 #feet
depth = 18 #feet
area = math.pi *length * depth / 2 #in ft^2
density = 62.423 # in lbs/ft^3
dateArray = list()
##########################################
#Data comes in from the'discharge_huron_river_data.txt' in 15 minute intervals from 2010-01-01 to 2019-12-31

##########################################
with open('discharge_huron_river_data.txt', 'r') as f:
    #data starts from row 29 on
    reader = list(csv.reader(f))[29:]
    for row in reader:
        #first splits the string into areas by \t then data in 4th index, convert to float
        dateArray.append(datetime.datetime.strptime(row[0].split("\t")[2], '%Y-%m-%d %H:%M'))
        massFlowData.append(float(row[0].split("\t")[4]))
        
data = {'Date': dateArray,
        'Mass Flow (ft^3/s)': massFlowData
        }      
        
df = pd.DataFrame (data, columns = ['Date','Mass Flow (ft^3/s)'])        
df.to_csv('Huron_River_Discharge_Data.csv', index = False)         