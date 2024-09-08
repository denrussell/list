''' 
Advanced Slicing Techniques** 
**Objective:** The aim of this assignment is to master the art of slicing in Python lists. 

**Problem Statement:** 
You have a list of daily temperatures for a month, and you'd like to extract specific data from it. 

**Task 1:** Given the list of temperatures:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
Extract the temperatures for the second week (7 days) of the month. Expected Outcome:
83, 85, 86, 87, 88, 89, 90,'''

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:14] #index 8th up to 15th
print(second_week)


# **Task 2:** Extract all the temperatures above 100. 

temp_above_100 = []

if temperatures[0] > 100:
    temp_above_100.append(temperatures[0])
if temperatures[1] > 100:
    temp_above_100.append(temperatures[1])
if temperatures[2] > 100:
    temp_above_100.append(temperatures[2])
if temperatures[3] > 100:
    temp_above_100.append(temperatures[3])
if temperatures[4] > 100:
    temp_above_100.append(temperatures[4])
if temperatures[5] > 100:
    temp_above_100.append(temperatures[5])
if temperatures[6] > 100:
    temp_above_100.append(temperatures[6])
if temperatures[7] > 100:
    temp_above_100.append(temperatures[7])
if temperatures[8] > 100:
    temp_above_100.append(temperatures[8])
if temperatures[9] > 100:
    temp_above_100.append(temperatures[9])
if temperatures[10] > 100:
    temp_above_100.append(temperatures[10])
if temperatures[11] > 100:
    temp_above_100.append(temperatures[11])
if temperatures[12] > 100:
    temp_above_100.append(temperatures[12])
if temperatures[13] > 100:
    temp_above_100.append(temperatures[13])
if temperatures[14] > 100:
    temp_above_100.append(temperatures[14])
if temperatures[15] > 100:
    temp_above_100.append(temperatures[15])
if temperatures[16] > 100:
    temp_above_100.append(temperatures[16])
if temperatures[17] > 100:
    temp_above_100.append(temperatures[17])
if temperatures[18] > 100:
    temp_above_100.append(temperatures[18])
if temperatures[19] > 100:
    temp_above_100.append(temperatures[19])
if temperatures[20] > 100:
    temp_above_100.append(temperatures[20])
if temperatures[21] > 100:
    temp_above_100.append(temperatures[21])

if temperatures[-9] > 100:
    temp_above_100.append(temperatures[-9])
if temperatures[-8] > 100:
    temp_above_100.append(temperatures[-8])
if temperatures[-7] > 100:
    temp_above_100.append(temperatures[-7])
if temperatures[-6] > 100:
    temp_above_100.append(temperatures[-6])
if temperatures[-5] > 100:
    temp_above_100.append(temperatures[-5])
if temperatures[-4] > 100:
    temp_above_100.append(temperatures[-4])
if temperatures[-3] > 100:
    temp_above_100.append(temperatures[-3])
if temperatures[-2] > 100:
    temp_above_100.append(temperatures[-2])
if temperatures[-1] > 100:
    temp_above_100.append(temperatures[-1])



print(temp_above_100)



# **Task 3:** Reverse the list and extract temperatures from the 5th to the 10th day 
# of the reversed list. ---

temperatures.reverse()
print(temperatures)
print(temperatures[4:9])

''' 
zork = 0
for i in temperatures:
    zork = zork + 1
print("Total of days:", zork, "days")
'''