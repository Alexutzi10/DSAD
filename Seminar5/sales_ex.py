import numpy as np
import pandas as pd


#Reading from sales2 csv file
data = pd.read_csv('C:/dev/DSAD/Seminar5/sales2.csv')


#Putting data into a data frame
df = pd.DataFrame(data)


#Cerinta 1: filtering by sales with the value greater than 200
print(df[df['Sales'] > 200])


#Cerinta 2: sorting by sales
print(df.sort_values('Sales'))


#Cerinta 3: grouping by region and calculating the average sales
print(df.groupby('Region')['Sales'].mean())