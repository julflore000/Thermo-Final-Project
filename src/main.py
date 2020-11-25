import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import math
import datetime


footToMeter = 0.3048000 # m/ft
footCubeToMeter = footToMeter ** 3 #m^3/ft^3
length = 150 * footToMeter #feet to meters
depth = 18 * footToMeter #feet to meters
area = math.pi *length * depth / 2 #in m^2
density = 997 # in kg/m^3
outputSpeedPercent = .5 #the lower the better
##########################################
#Data comes in from the'discharge_huron_river_data.csv' in 15 minute intervals from 2010-01-01 to 2019-12-31

##########################################
df = pd.read_csv("Huron_River_Discharge_Data.csv",parse_dates = True)
df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M') #converting to datetime fromat so we can index into a specific year
year = 2010
timeGap = 15 * 60 #15 minutes converted to seconds for each of the csv entries
wattHourConversion = 60 * 60 #how many seconds are in 1 hour
massFlowData = list() #main list for data coming in
while year < 2020:
    start_date = pd.to_datetime('01/01/%s' % (year)) #setting up dates for getting data from january 1st to december 31st
    end_date = pd.to_datetime('12/31/%s 23:59' % (year))

    dischargeData = df[df.Date.between(start_date, end_date)]['Mass Flow (ft^3/s)'] #reading in data
    dischargeData = np.array(dischargeData) * footCubeToMeter#in m^3/s
    inputVelocityData = dischargeData / area #now in m/s
    massFlowData =  dischargeData  * density #now in kg/s
    outputVelocityData = inputVelocityData * outputSpeedPercent #out going velocity not sure what a common speed reduction is but using 50%
    workGenerated = .5 * massFlowData * ((inputVelocityData **2) - (outputVelocityData**2)) #in joules / second or watts
    energyGenerated = workGenerated * timeGap #(converting to joules generated for each 15 minute period)
    wattHourGenerated = workGenerated * wattHourConversion  #converting to what each watt hour (joules) would be for the discharge rate on that period, average is the average Wh for plant
    plt.plot(wattHourGenerated/1000,label=year) #converting to kWh
    print("Year: %s \t Total energy generated: %s (kJ), Average watts for 15 minute period: %s, Average kWh: %s" % (year, np.sum(energyGenerated) / (1000), (np.average(workGenerated)),np.average(wattHourGenerated)/1000))
    year += 1
plt.title("Energy generated from 2010-2019: with an output velocity percent of %s for each 15 minute increment" % (outputSpeedPercent))
plt.ylabel("Kilo Watts hour (kWh or kilo Joules)")
plt.xlabel("15 minute increment locations")
plt.legend()
plt.show()

#the graph shows what the expected watt hour generation would be for the run of river plant for each 15 minute discharge period