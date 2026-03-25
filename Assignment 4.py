#to study loops in python 
#Assignment 4
#1.WAP to display evevn numbers from 1-10
for i in range(1,11):
  if i%2==0:
     print(i)
  
#2. WAP to add odd numbers from 1-10
sum=0
for j in range(1,10,2):
  sum+=j
print(sum)

#3.WAP a python program to get the fibonacci series between 0 to 50
a=0
b=1
print(a,end="")
print(b,end="")
while i<50:
    i=a+b
    if i>50:
        break
    print(i,end="")
    a=b
    b=i
    
#4.WAP to remove the characters which have odd index values of a given string
y=input ("\n enter the string:")
result=""
for i in range(len(y)):
    if i%2==0:
        result+=y[i]
        print(result)
