import numpy as np
import pandas as pd

list1 = [1, 2, 3, 4, 5]

# Convert list to numpy array
array1 = np.array(list1)
print(array1)

list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array2 = np.array(list2)
print(array2)


# Add +2 to each element of the array1
print(array1+2)


# Reshape the array1 to 5x1
array1Reshape = array1.reshape(5, 1)
print(array1Reshape)


#Data frame
data = {'Name': ['Tom', 'Jerry', 'Mickey', 'Donald'], 
        'Age': [20, 21, 22, 23],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
print(data)
df = pd.DataFrame(data)
print(df)


#Selecting columns
print(df['City'])


#Selecting rows
print(df.loc[1])


#Data filtering
print(df[df['Age'] > 21])


#Data sorting
print(df.sort_values('Age'))
# print(df.sort_values(by='Age'))


#Data grouping
print(df.groupby('City')['Age'].mean())