from Student import Student

#student1 = Student("Jim", "Business", 3.0, False)
#student2 = Student("Pam", "Comp Sci", 4.0, True)

students = [
    Student("Jim", "Business", 3.0, False),
    Student("Pam", "Comp Sci", 4.0, True)
]

#print(student1.name)

#print(student2.on_honor_roll())

for student in students:
    print ("Name: " + student.name)
    print ("Major: " + student.major)
    print ("GPA: " + str(student.gpa))
    print ("On probation: " + str(student.is_on_probation))
    print ("On honor roll: " + str(student.on_honor_roll()))
