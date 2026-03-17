import sys

# print("My name is ", sys.argv[1])

# print("My name is GoharAbbas")
# for argv in sys.argv[1:-1]:
#     print("Arguments in Terminals are ", argv)






# try:
#     print("Hello My Name is" ,  sys.argv[1])
# except:
#     print("Your Name is Required to successfully this program")





# if len(sys.argv) > 1:
#     print("Your Name is " + sys.argv[1])
#     sys.exit()
# else:
#     print("Your Name is Required to successfully this program")


# print("Program still working after sys.exit")




# name = input("What is your name: ")
# print("My name is " + name)


for arg in sys.argv[1:-1]:
    print(arg, end=None)