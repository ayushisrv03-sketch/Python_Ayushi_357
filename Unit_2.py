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

#list
'''list1=["rohan",1,3,5]
print(list1)'''
# list is ordered,changeable and allows duplicates as well
'''list1=["rohan",1,3,5,"rohan"]
print(list1)
print(len(list1))'''

#list() constructor
'''l=list(("rohan",1,2,3,"rohan"))
print(l)'''

#access item in list
'''l=list(("rohan",1,2,3,"rohan"))
print(l[4])'''

#negative indexing
'''l=list(("rohan",1,2,3,"rohan"))
print(l[-2])'''

'''l=list(("rohan",1,2,3,"rohan"))
print(l[1:5])'''

#check if item exists
'''l=list(("rohan",1,2,3,"rohan","apple"))
if "apple" in l:
    print("yes")
if "banana" in l:
    print("yes")
else:
    print("No")'''

#change list item
'''l=list(("rohan",1,2,3,"rohan","apple"))
l[0]="ram"
print(l)'''
#changing list item in a range
'''l=list(("rohan",1,2,3,"rohan","apple"))
l[1:3]=["ram"]*2
print(l)'''

#using insert function
'''l=list(("rohan",1,2,3,"rohan","apple"))
l.insert(2,"ayushi")
print(l)'''

#using append function
'''l=list(("rohan",1,2,3,"rohan","apple"))
l.insert(2,"ayushi")
l.append("hey")
print(l)'''

#using remove function
'''l=list(("rohan",1,2,3,"rohan","apple"))
l.insert(2,"ayushi")
l.append("hey")
l.remove(2)
print(l)'''

#extending a list
'''l=list(("rohan",1,2,3,"rohan","apple"))
l.insert(2,"ayushi")
l.append("hey")
l.remove(2)
list2=["rohan"]
l.extend(list2)
print(l)'''

#using pop function
'''l=["rohan", 1, "ayushi", 3, "rohan", "apple", "hey", "rohan"]
l.pop(-2)
print(l)'''

#deleting a list
'''l=["rohan", 1, "ayushi", 3, "rohan", "apple", "hey", "rohan"]
del(l)
print(l)'''

#Clearing the list items
'''l=["rohan", 1, "ayushi", 3, "rohan", "apple", "hey", "rohan"]
l.clear()
print(l)'''

#Printing the items of the list
'''l=["rohan", 1, "ayushi", 3, "rohan", "apple", "hey", "rohan"]
for x in l:
    print(x)'''

#Looping through the index
'''l=["rohan", 1, "ayushi", 3, "rohan", "apple", "hey", "rohan"]
for i in range(len(l)):
    print(l[i])'''

#Using a while loop
'''i=0
l=["rohan", 1, "ayushi", 3, "rohan", "apple", "hey", "rohan"]
while i<len(l):
    print(l[i])
    i+=1'''

#Looping using list comprehension
'''l=["apple","banana","cherry"]
[print(x) for x in l]'''

#Lowercase to uppercase
'''l=["apple","banana","cherry","mango","kiwi"]
[print(x.upper()) for x in l]'''

#Searching
'''l=["apple","banana","cherry","mango","kiwi"]
x="banana"
[print("YES") if x in l else print("NO")]'''

#Sorting with key
'''l=["apple","banana","cherry","mango","kiwi"]
l.sort(key=str.lower)
print(l)'''

#Sorting
'''l=["apple","banana","cherry","mango","kiwi"]
l.sort(reverse=True)
print(l)'''

#Reverse
'''l=["apple","banana","cherry","mango","kiwi"]
l.reverse()
print(l)'''

#Copying a list
'''a=["apple","banana","lychee"]
mylist=a.copy()
print(mylist)'''
#Using the list method
'''a=["apple","banana","lychee"]
mylist=list(a)
print(mylist)'''
#using the slice operator(:)
'''a=["apple","banana","lychee"]
mylist=a[:]
print(mylist)'''

#Join lists
'''a=["apple","banana","lychee"]
b=[1,2,3]
c=a+b
print(c)'''
#another way
'''a=["a","b","c"]
b=[1,2,3]
for x in b:
    a.append(x)

print(a)'''

#extend
'''a=["a","b","l"]
b=[1,2,3]
a.extend(b)
print(a)'''

#TUPLE
#TUPLE => used to store multiple items in a single variable
#      => ordered and unchangable (immutable)
#      => To change the tuple convert it into list 
#      => TUPLE CONSTRUCTOR =>  tuple()

#INITIALIZATION OF TUPLE
'''mytuple=("Ayushi","Avinash", "Aman","Ravi","Akash","Shivi","Yuvi")'''
#ACCESSING ELEMENTS OF TUPLE
'''print(mytuple[1])
print(mytuple[-1])
if "Ayushi" in mytuple:
    print ("Yes Ayushi is present")
else:
    print (f"No Ayushi is not present")'''
#METHOD 1 to add elements in tuple
'''L=list(mytuple)
L[4]="Ayush"
L.append("Rakesh")
mytuple=tuple(L)
print (mytuple)'''
#METHOD 2 to add element in tuple
'''y=("Abhi",)
mytuple+=y
print (mytuple)'''

#Printing elements of tuple
'''tuple1=("apple","banana","cherry","orange","kiwi","melon","mango")
print(tuple1[2:5])
tuple1=("apple","banana","cherry","orange","kiwi","melon","mango")
print(tuple1[2:])
print(tuple1[-4:-1])'''

#Check if item exists
'''tuple1=("apple","banana","cherry","orange","kiwi","melon","mango")
if "apple" in tuple1:
    print("YES")
else:
    print("NO")'''

#Change tuple values-> tuples are immutable and adding using append
'''tuple1=("apple","banana","cherry","orange","kiwi","melon","mango")
y=list(tuple1)
y.append("ayushi")
tuple1= tuple(y)
print(tuple1)'''

#PACKING AND UNPACKING IN TUPLE
'''tup=("ayushi","hello")
a,b=tup
print(a)
print(b)'''