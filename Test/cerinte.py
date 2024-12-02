import pandas as pd
import numpy as np


#Cerinta 1: eliminati duplicatele din lista si returnati numarul de elemente unice
nums = [1, 1, 2]
def remove_duplicates(nums):
    return len(set(nums))

print('---------Cerinta 1---------')
print(remove_duplicates(nums))



#Cerinta 2: extrageti din array-ul urmator elementele pare si apoi afisati rezultatul ridicat la puterea a 2a
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def even_elem(arr):
    return [x**2 for x in arr if x%2==0]

print('\n---------Cerinta 2---------')
print(even_elem(arr))


# Cerinta 3: Pe baza tuplurilor de mai jos calculati urmatoarele: 
students = [
    ("Alice", 85, 92, 88),
    ("Bob", 78, 90, 83),
    ("Charlie", 95, 87, 92)
]

#a. scorul mediu al fiecarui student
def average_scorePerStudent(students):
    return {student[0]: sum(student[1:])/3 for student in students}

print('\n---------Cerinta 3---------')
print(average_scorePerStudent(students))

#b. gasiti studentul cu scorul cel mai mare
def max_studentScore(students):
    return max(students, key=lambda x: sum(x[1:]))

print(max_studentScore(students))

#c. creati o lista noua de tupluri care sa contina numele studentilor si scorul lor cel mai mare
def max_scorePerStudent(students):
    return [(student[0], max(student[1:])) for student in students]

print(max_scorePerStudent(students))



# Cerinta 4: Se dau urmatoarele 2 dictionare: 
sales_data = {
    "apple": 2,
    "banana": 3,
    "orange": 1
}

prices = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.7
}

#a. Calculati costul total al elementelor din dictionar.
def total_cost(sales_data, prices):
    return round(sum([sales_data[item]*prices[item] for item in sales_data]), 2)

print('\n---------Cerinta 4---------')
print(total_cost(sales_data, prices))

#b. Creati un dictionar nou unde cheia este numele produsului iar valoarea este reprezentata de costul total
def total_cost(sales_data, prices):
    return {item: round(sales_data[item]*prices[item], 2) for item in sales_data}

print(total_cost(sales_data, prices))



#Cerinta 5: Pe baza urmatoarelor 2 dictionare, rezolvati cerintele:
sales_Data = {
    'Product': ['A', 'B', 'C'],
    'Sales': [100, 150, 200]
}

cost_data = {
    'Product': ['A', 'B', 'C'],
    'Cost': [50, 75, 100]
}

#a. Creati 2 dataframe-uri din cele 2 dictionare
sales_df = pd.DataFrame(sales_Data)
cost_df = pd.DataFrame(cost_data)
print('\n---------Cerinta 5---------')
print(sales_df)
print(cost_df)

#b. Faceti merge intre cele 2 dataframe-uri pe baza coloanei Product
merged_df = pd.merge(sales_df, cost_df, on='Product')
print(merged_df)

#c. Calculati profitul pentru fiecare produs (profitul se va calcula scazand costul)
merged_df['Profit'] = merged_df['Sales'] - merged_df['Cost']
print(merged_df)



#Cerinta 6: Creati 2 clase in python. Demonstrati cu ajutorul acestora conceptul de mostenire si mai apoi conceptul de polimorfism creand o metoda suprascrisa(ovveride) si apeland aceasta metoda. 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'I am an animal'
    

class Dog(Animal):
    def speak(self):
        return 'I am a dog'
    
print('\n---------Cerinta 6---------')
print(Animal('Rex').speak())
print(Dog('Ares').speak())