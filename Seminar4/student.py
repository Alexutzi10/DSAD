#1. Creati o clasa pe baza fisierului students.csv
#2. Cititi randurile din csv si creati un array de studenti (metoda definita in clasa)
#3. Filtrati studentii in functie d evarsta (varsta minima > 19)
#4. Calculati media notelor pentru toti studentii (+std deviation)

import csv

studentsFile = open(r'C:\dev\DSAD\Seminar4\students.csv')
lines = studentsFile.readlines()
studentsFile.close()

class Student():
    def __init__(self, name, age, avgGrade):
        self.name = name
        self.age = age
        self.avgGrade = avgGrade
        
    @staticmethod
    def readCsv(filename):
        students = []
        with open(filename, 'r') as file:
            csvReader = csv.reader(file)        #citeste fisierul
            header = next(csvReader)            #sare peste prima linie
            for row in csvReader:
                print(row)
                student = Student(row[1], int(row[2]), float(row[3]))
                students.append(student)
        return students
    
    def filterStudents(self):
        students = self.createStudents()
        students = [student for student in students if student.age > 19]
        return students
    
    def calculateAvg(self):
        students = self.createStudents()
        avg = sum([student.avgGrade for student in students]) / len(students)
        return avg
    
    def calculateStdDev(self):
        students = self.createStudents()
        avg = self.calculateAvg()
        stdDev = (sum([(student.avgGrade - avg) ** 2 for student in students]) / len(students)) ** 0.5
        return stdDev

student = Student("John1", 20, 9.5)
filename = "students.csv"
student.readCsv(filename)