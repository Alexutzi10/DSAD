#1. Creati o clasa pe baza fisierului students.csv
#2. Cititi randurile din csv si creati un array de studenti (metoda definita in clasa)
#3. Filtrati studentii in functie de varsta (varsta minima > 19)
#4. Calculati media notelor pentru toti studentii (+std deviation)

import csv

class Student:
    def __init__(self, name, age, avgGrade):
        self.name = name
        self.age = age
        self.avgGrade = avgGrade

    @staticmethod
    def readCsv(filename):
        students = []
        with open(filename, 'r') as file:
            csvReader = csv.reader(file)
            header = next(csvReader)        # sare peste prima linie
            for row in csvReader:
                print(row)                  # verificare pentru datele din CSV
                student = Student(row[1], int(row[2]), float(row[3]))           # Presupunem că coloanele sunt: Nume, Vârstă, Notă
                students.append(student)
        return students
    
    @staticmethod
    def filterStudents(students):
        for student in students:
            if student.age>19:
                print(student.name, student.age, student.avgGrade)
    
    @staticmethod
    def calculateAvg(students):
        avg = sum([student.avgGrade for student in students]) / len(students)
        return avg
    
    @staticmethod
    def calculateStdDev(students):
        avg = Student.calculateAvg(students)
        variance = sum([(student.avgGrade - avg) ** 2 for student in students]) / len(students)
        stdDev = variance ** 0.5
        return stdDev


# Exemplu de utilizare:
print('Cerinta 2:')
filename = r"D:\Facultate\An III Sem I\DSAD\Seminar4\students.csv"
students = Student.readCsv(filename)
print('\n---------------------------\n')
print('Cerinta 3:')
filtered_students = Student.filterStudents(students)
print('\n--------------------------\n')
print("Cerinta 4:")
print(Student.calculateStdDev(students))
