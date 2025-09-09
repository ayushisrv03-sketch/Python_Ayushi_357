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
