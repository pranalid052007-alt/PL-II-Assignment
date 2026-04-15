#To study Tuple using in-built functions
#Assignment 7
#1. WAP to create a tuple and perofrm basic operations like length, concatenation, repetition, and membership
t = (1,2,3,4,5,6)
m = ("height", "length", "breadth", "radius")
print("Tuple 1: ", t)
print("Tuple 2: ", m)
print("Length of Tuple 1: ", len(t))
print("Concatenation operation: ", t + m)
print("Repetition operation on Tuple 2: ", m * 2)
if 2 in t:
    print("2 is present in Tuple 1.")

#2. WAP to demonstrate indexing, negative indexing, slicing, and iteration on a tuple
b = (9,5,7,3,45)
print(b)
print(b[3])
print(b[-2:])
print(b[1:4])

#3. WAP to show that tuples are immutable and demonstrate tuple deletion using del
a = (2,5,2,7,2,8)
print(a)
del a[3] # TypeError: 'tuple' object doesn't support item deletion
del a

#4. WAP to apply built-in functions like len(), max(), min(), and tuple() on a given sequence
c = (0,9,8,7,6.5,4,3,2,1)
print("Tuple: ",c)
l = [5,3,8,5,9,2,8]
print("List: ",l)
print("Maximum in Tuple: ", max(c))
print("Minimum in Tuple: ", min(c))
print("Length of Tuple: ", len(c))
print("List as tuple: ", tuple(l))




