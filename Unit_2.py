#Taking input in python
'''a=int(input("Enter your age:"))
if(a>=18):
    print("Eligible")
else:
    print("Not Eligible")'''

#Using elseif conditions
'''a=2
if(a%2==0):
    print("Even")
else:
    print("Odd")'''

#shorthand if
'''a=200
b=33
if(a>b): print("a is greater than b")'''

#shorthand if_else
'''a=2
b=300
print("A") if a>b else print("B")'''

'''a=300
b=300
print("A") if a>b else print("=") if a==b else print("B")'''

#Using and operator
'''a=200
b=30
c=500

if a>b and c>a:
    print("both condition true")'''

#using not operator
'''a=33
b=200
if not a>b:
    print("True")'''

#Using pass
'''a=5
b=8
if a>b:
    pass
if b>a:
    print(b)'''

#match statement
'''day =10
match day:
    case 5:
        print("Monday")
    case 6:
        print("Tuesday")
    case 7:
        print("Wednesday")
    case 4:
        print("Thursday")
    case _:
        print("Invalid day")'''

#using multiple cases in match and also use conditions inside case
'''day=5
match day:
    case 1|2|3|4|5 if day==5:
        print("Weekday")
    case _:
        print("Invalid Day")'''

#while loop
'''i=1
while i<6:
    print(i)
    i+=1'''

#number guessing
'''num=3
print("Enter a no. in the range[1 to 10]:")
a=int(input())
if(num==a):
    print("You guessed it right")
else:
    print("You guessed wrong. The number was "+str(num))'''

# break in while loop 
'''i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1'''
#continue in while loop
'''i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)'''

#for loop via list
'''fruits=["Apple","Banana","Cherry"]
for x in fruits:
    print(x)
print(type(fruits))'''

#iteration in for loop
'''for x in "Apple":
    print(x)'''

#break in for loop
'''fruits=["Apple","Banana","Cherry"]
for x in fruits:
    if x=="Banana":
        continue
    print(x)'''

#range in for
'''for x in range(1,10):
    print(x)'''

#start end and step in range
'''for x in range(1,10,2):
    print(x)'''

#using else in while and for loop
'''for x in range(1,6):
    print(x)
else:
    print("Finally")'''

'''i=1
while(i<6):
    print(i+2)
    i+=1
else:
    print("Done")'''

#nested loops in python
'''a=["A","B","C"]
fruits=["Banana","Cherry"]
for x in a:
    for y in fruits:
        print(x,y)'''

#pass statement
'''for x in [0,1,2,3]:
    pass'''

