'''
Objective:
The aim of this assignment is to delve deeper into list methods and understand the nuances of 
identity operators.

Problem Statement:
You have two lists of student names. One list contains the names of students who have submitted 
their assignments, and the other list contains the names of students who attended the last class.
'''

# Task 1: Given the two list, 
# Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

#submitted.append("Eve")
#submitted.append("Frank")
#attended.append("Bob")
#attended.append("David")

# I used the append above to test for every scenario

if "Alice" in submitted and "Alice" in attended:
    print("Alice did both.")
if "Bob" in submitted and "Bob" in attended:
    print("Bob did both.")
if "Charlie" in submitted and "Charlie" in attended:
    print("Charlie did both.")
if "David" in submitted and "David" in attended:
    print("David did both.")
if "Eve" in submitted and "Eve" in attended:
    print("Eve did both.")
if "Frank" in submitted and "Frank" in attended:
    print("Frank did both.")


# To be more creative and use other functions, I wrote the following:

both = []  # Created a blank list for now

if "Alice" in submitted and "Alice" in attended:
    both.append("Alice")   #  Created an if statement and if True, name would be added to the list.
if "Bob" in submitted and "Bob" in attended:
    both.append("Bob")
if "Charlie" in submitted and "Charlie" in attended:
    both.append("Charlie")
if "David" in submitted and "David" in attended:
    both.append("David")
if "Eve" in submitted and "Eve" in attended:
    both.append("Eve")
if "Frank" in submitted and "Frank" in attended:
    both.append("Frank")

print("Students that did both are: ",", ".join(both))
# Then I printed all students that did both by printing the list that collected them.



# Task 2: Check if the two lists are identical in terms of their content, regardless of order.


# The code below didn't work well...
'''
if (submitted) ==  len(attended):
    print("List contents are: Identical")
else: 
    print("List contents are: NOT Identical")
'''


if sorted(submitted) == sorted(attended):
    print("Identical contents")
else:
    print("Not identical contents.")


# Task 3: Using list methods, remove any student from the attended list 
# who did not submit their assignment.

#submitted = ["Alice", "Bob", "Charlie", "David"]
#attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in attended and "Alice" not in submitted:
    attended.remove("Alice")   #  Used not in function and then remove
if "Bob" in attended and "Bob" not in submitted:
    attended.remove("Bob")
if "Charlie" in attended and "Charlie" not in submitted:
    attended.remove("Charlie")
if "David" in attended and "David" not in submitted:
    attended.remove("David")
if "Eve" in attended and "Eve" not in submitted:
    attended.remove("Eve")
if "Frank" in attended and "Frank" not in submitted:
    attended.remove("Frank")

print(attended)