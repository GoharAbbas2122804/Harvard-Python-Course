name = input("what is your name ")
print(f"hello {name} ")
print("how many records you want to enter in the file ")


records_list = []
lenght = int(input("enter the number of records you want to enter in the file : "))


for _ in range(lenght):
    records_list.append(input("enter the record : "))

with open("records.txt", "a") as file:
    for record in sorted(records_list):
        file.write(record + "\n")
        
print("********************************")
print("file created successfully")
print("********************************")


with open("records.txt", "a") as file:
    stamp = (input("Add a Stamp to Save Records: "))
    file.write(stamp + "\n")
 



print("**************")
ans = input("DO you want to Read Data from the file: Y/N")
if(ans == 'y' or ans == 'Y'):
    print("*******Ok Reading Data From the File*******")
    with open("records.txt" , "r") as file:
        # data = file.readlines()
        for record in file:
            print(record.rstrip())
else:
    print("Exiting The Program") 