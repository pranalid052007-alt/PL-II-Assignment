#To study Set operations and Dictionary traversing
#Assignment 8
#1. WAP to sort a dictionary by value
car = {"brand": "Ford", "model": "Mustang", "year": 1964, "colors": ["red", "white", "blue"]}
print(car)
car1 = dict(sorted(car.items()))
print(car1)

#2. WAP to check if a given key already exists in a dictionary
fruits = {"Apple" : 5, "Banana" : 7, "Cherry" : 2, "Strawberry" : 8, "Mango" : 6, "Grapes" : 5}
if "Banana" in fruits:
    print("Banana is present.")
else:
    print("Banana is not present.")

#3. WAP to merge two Python dictionaries
print("Dict 1: ", car)
print("Dict 2: ", fruits)
print("Combined dict: ",car | fruits)

#4. WAP to add an item in a tuple.
t = (1,2,4,5,6,7,8)
print(t)
l = list(t)
l.append(78)
t1 = tuple(l)
print(t1)

#5. WAP to create a tuple with different data types
x = (2, 3.4, "five", False, [7,5])
print(x)

#6. WAP to sum all the items in a list
l = [2,6,9,3,0,3,7,4]
print(l)
print(sum(l))

#7. WAP to get the largest number from a list.
l = [2,6,9,3,0,3,7,4]
print(l)
print(max(l))

#8. WAP to add member(s) in a set.
s= set()
s.add(1)
s.add(786)
s.add("SETS")
s.add("Blue")
print(s)

#9. WAP to reverse the order of the items in the array
m = ["apple", 6, 4.5, 90, "T", 876]
print(m)
n = m[::-1]
print(n)

#10. WAP to create an array of 5 integers and display the array items. Access individual element through indexes.
b = [2,3,4,6,7]
print("Array: ", b)
for i in range(0,len(b)):
    print("Element at index ", i, ": ", b[i])
