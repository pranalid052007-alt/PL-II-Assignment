# to study if, if else, if-elif-else, statement in python
# assignment
#1. WAP to find out greatest of 3 numbers
a=6
b=8
c=4
if a>b and a>c:
    print(a, "is the greatest number")
elif b>a and b>c :
    print(b,"is the greatest number")
else:
    print(c,"is the greatest number")


#2. WAP to find whether given numbers is odd or even
d=8
if d%2==0:
    print(d,"is even number")
else:
    print(d,"is odd number")

#3.WAP to check whether is chracter is uppercase or lowercase
x="Hello World"
if x.islower():
    print("all letters in uppercase")
elif x.isupper():
    print("all letter in upper case")
else:
    print("the letters are in both lower and upper case")

#4.WAP to find whether given input is number or character
y=input ("enter the input")
if y.isdigit():
    print("input is number")
elif y.isalpha():
    print("input is acharacter")
else:
    print("input is a combination of both numbers and character")
