def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello") 

greet("es")
greet("ehjoej")

n = 5
while n > 0:
    print(n)
    n = n - 1
print(n)
print("Blast off!")

for i in [5,4,3,2,1]:
    print(i)
print("Blast off!")

friends = ["John", "Chris", "Fernando", "Mark", "Bernard"]
for i in friends:
    print("Hello", i)

largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print("After", largest_so_far)


found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        break
    print(found,value)
print("There's a 3 in there.")

