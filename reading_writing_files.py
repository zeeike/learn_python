#Only read the info, change w to write, a to append, r+ read and write
employee_file = open("employees.txt","w") 

#Only true if r or r+ is set
#print(employee_file.readable())

#Print all info in file
#print(employee_file.read())

#Readlines puts into into a list
#print(employee_file.readlines()[1])

#for employee in employee_file.readlines():
 #   print(employee)
    
#Write a new line to the file
employee_file.write("\nSteve - IT")

#for employee in employee_file.readlines():
#    print(employee)

#Close the file at the end
employee_file.close()
