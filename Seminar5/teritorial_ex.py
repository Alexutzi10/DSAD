import numpy as np
import pandas as pd
from functions import *


#Creating a table based on the csv file
table = pd.read_csv('C:/dev/DSAD/Seminar5/Teritorial_2022.csv', index_col=0)
print(table)


#Creating a list of the variables
variable = list(table)
numeric_variables = variable[3:]


#Cleaning the data
x = table[numeric_variables].values
nan_replace(x)
print(x)