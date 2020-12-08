import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import math
import datetime
#reads in data from raw format and then fills in any missing data
df = pd.read_csv("Huron_River_Discharge_Data.csv",parse_dates = True)
df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %H:%M') #converting to datetime fromat so we can index into a specific year
mainDataframe = pd.DataFrame({"Mass Flow (ft^3/s)": list(df["Mass Flow (ft^3/s)"])},
                   index=df["Date"])
correctRange = pd.date_range('2010-01-01 0:0', '2019-12-31 23:59',freq='15T')
print(len(mainDataframe))
mainDataframe= mainDataframe.reindex(correctRange,method = "ffill")
mainDataframe.to_csv("Cleaned_Huron_River_Discharge_Data.csv",index_label = "Date")
print(len(mainDataframe))

