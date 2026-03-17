import csv

lenght = int(input("Lenghts of records: "))
with open("written.csv" , "a") as file:
    for _ in range(lenght):
        name = input("what is your name: ")
        rollno = input("what is your rollno")
        writer = csv.writer(file)
        writer.writerow([name , rollno ])