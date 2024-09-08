'''
3. Arithmetic Operations in Daily Life
Objective: The aim of this assignment is to get familiarized with basic 
arithmetic operations and understand how they can be applied in everyday 
situations.

Task 1: Grocery Store Math 

Calculate the total cost of three items you'd 
commonly find in a grocery store, given their individual prices. 
For example, what would be the cost of 
bread, peanut butter, and jelly be? Prices don't need to be realistic!

'''
bread = 4.50
peanut_butter = 8.75
jelly = 12.95

total = bread + peanut_butter + jelly
print(total)

'''
Task 2: Bank Interest 

If you have a savings account with a particular 
initial amount and a fixed yearly interest rate, calculate the total 
amount in your account after a year. So if you had $10,000 at a 7% 
interest write code that would tell us the amount at 
the end of the year. For the example the expected outcome would be $10,700.
'''

balance = 10000  # $10,000 initial amount
int_rate = 0.07  # 7%  interest rate
period = 1  # 1 year period

total_amount = balance + (balance * int_rate)
print(total_amount)