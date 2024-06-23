'''4. Deep Dive into Python Lists** 

**Objective:** The aim of this assignment is to integrate various list operations and methods 
to solve a complex problem. 

**Problem Statement:** You're organizing a school event, and you have lists containing student names, 
their grades, and the activities they're interested in. 

**Task 1:** Given the lists:
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
Filter out students who have grades below 80. Print the `name`, `grade` and `activiy`. 
Expected Outcome "Jane", 78, "Art" 
'''

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]


if grades[0] < 80:
    print(students[0], grades[0], activities[0])
           
if grades[1] < 80:
    print(students[1], grades[1], activities[1])
        
if grades[2] < 80:
    print(students[2], grades[2], activities[2])
    
if grades[3] < 80:
    print(students[3] , grades[3] , activities[3])
    



'''**Task 2:** For the remaining students, add students name in a new list named `students_approved`. 
Expected Outcome: students_approved = ["John", "Doe", "Smith"]'''

students_approved = []

if grades[0] > 80:
    students_approved.append(students[0])
             
if grades[1] > 80:
    students_approved.append(students[1])
        
if grades[2] > 80:
    students_approved.append(students[2])
    
if grades[3] > 80:
    students_approved.append(students[3])



'''**Task 3:** Print the list `students_approved` '''

print(students_approved)