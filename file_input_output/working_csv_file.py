import csv
students = []

with open("students.csv") as file:
    # for records in file:
    #     name , address = records.rstrip().split(",")
    #     student = {"name" : name , "address" : address}
    #     students.append(student)

    # by using the csv module and its provided functions
    for records in file:
        reader = csv.reader(file)
        for name , address in reader:
            students.append({"name": {name} , "address" : {address}}) 

print(students)

# lambda is an anonymous function means a function that has no name , a pythonic way to use lambda , for sorting an object 
# we have to give a key , that's why are we using this lambda 
for student in sorted(students , key = lambda student : student["name"]):
    print(f"{student["name"]} lives in {student["address"]}")