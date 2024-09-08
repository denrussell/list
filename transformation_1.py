'''
1. Python List Transformation
Objective:
The aim of this assignment is to practice advanced list operations and transformations.

Problem Statement:
You've been given a list of numerical grades from a class exam. 
You need to process and analyze these grades.

'''

'''
Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
Sort the grades in descending order and display the sorted list.

'''
'''
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()   # First I sorted them out in ascending order
sort_grades = grades    # I named the sorted list
sort_grades.reverse()   # Then I reversed the order
reverse_grades = sort_grades    # I named the sorted reversed list

print(reverse_grades)   # Printed
'''
# The code above was my initial solution but I simplified it below:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()   # First I sorted them out in ascending order
grades.reverse()    # Then I simply reversed it
print ("Grades in descending order:",grades)   # Then print. 

# The important thing to remember here is the order (sort then reverse)



# Task 2: Calculate the average grade and display it.

# print (len(grades))  # Checking the number of items on the list

list_qty = len(grades)  # I named the quantity on the list
list_sum = sum(grades)  # I named the sum of all the items added together

# print (list_sum)  # Checking if the sum function exists and correct

avg_grade = list_sum/list_qty   # Average is the sum of all items divided by the total number of items
print("The average grade is:",avg_grade)




# Task 3: Replace any grade below 80 with the value Failed.

print(grades)
# checking the list to know which ones are < 80 and locating their index positions
# then I replaced them with the string value Failed.

if grades[0] < 80: 
    grades[0] = ("Failed")
if grades[1] < 80:
    grades[1] = ("Failed")
if grades[2] < 80: 
    grades[2] = ("Failed")
if grades[3] < 80:
    grades[3] = ("Failed")
if grades[4] < 80: 
    grades[4] = ("Failed")
if grades[5] < 80:
    grades[5] = ("Failed")
if grades[6] < 80: 
    grades[6] = ("Failed")
if grades[7] < 80:
    grades[7] = ("Failed")
if grades[8] < 80: 
    grades[8] = ("Failed")
if grades[9] < 80:
    grades[9] = ("Failed")



print(grades)
# I initially wrote these ones below...
#grades[-3] = "Failed"
#grades[-2] = "Failed"
#grades[-1] = "Failed"
#print(grades)
'''   
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
for i in grades:
    if i < 80:
        print("Grade is",i,"= Failed")
        '''