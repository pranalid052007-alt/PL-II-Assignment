#To study list access using membership operators
#Assignment 6
#1. WAP to create a list and demonstrate membership operators (in, not in) to check element presence
a = ["Happy", 45, True, "9.56", 2.5]
print(a)
if "Happy" in a:
    print("Happy is present in the list.")
if 3.2 not in a:
    print("3.2 is not present in the list.")

#2. WAP to perform indexing, negative indexing, and sclicing operations on a given list
b = [1,2,3,4,5,6]
print(b)
print(b[3])
print(b[-2:])
print(b[1:4])

#3. WAP to update, append, insert, and delete elements from a list using built-in methods
c = ["apple", "banana", "cherry"]
print(c)
c.append("orange")
print(c)
c.insert(2,"strawberry")
print(c)
del c[0]
print(c)

#4. WAP to demonstrate basic list operations like concatenation, repetition, length, maximum, and minimum functions
d = ["Happy", 45, True, "9.56", 2.5]
e = [1,2,3,4,5,6]
print(d)
print(e)
print("Concatenation: ", d + e)
print("Repetition of e: ", e*3)
print("Length of d: ", len(d))
print("Maximum in e: ", max(e))
print("Minimum in e: ", min(e))

