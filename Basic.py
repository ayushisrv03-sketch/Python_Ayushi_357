'''myVariableName= 'Ayushi'
MyVariableName= 'Srivastava'
my_variable_name= 'Rashi'
print (myVariableName)'''

#Many to multiple variable
'''x,y,z=1,2,3
print(id(x))
print(id(y))
print(id(z))'''

#one to multiple
'''x=y=z=2
print(id(x))
print(id(y))
print(id(z))'''

#unpacking
'''f=["x","y","z"]
a,b,c=f
print(a)
print(b)
print(c)'''

#global variable
#there are two methods for global variable
#1. Declare it globally 
#2. If initializing a global variable in a specific function, use the keyword global to use it in the whole file
'''
HEAD
x= "awesome"
def myfunc():
    print("Python is "+x)

myfunc()


x= "awesome"
def myfunc():
    print("Python is "+x)

myfunc()'''

#NUMERIC DATA TYPE
'''var1= 1
var2= True
var3= 10.023
var4= 10+3j
print(type(var4))
print(var4)'''

#You can assign strings in single quotes as well as double quotes
'''print('Hello')
print("Hello")'''

#To find the length of a string
'''a="Hello World"
print(len(a))'''

#Replace string
'''a="Hello World"
print(a.replace("H","J"))'''

#Split string
'''a="Hello World"
print(a.split(","))'''

#Using Format instrings
'''age=36
txt=f"My name is John, I am {age}"
print(txt)'''

#Boolean 
'''a=(5>2)
print(a)'''

'''print(bool(-1))'''

#Function returning a boolean value
'''def myfunc():
    return True

if myfunc():
    print("YES!")
else:
    print("NO!")'''

#Sequence Datatype
'''list=['abcd', 786 ,2.23 , 'john' , 70.2]
print (list)
print(type(list))'''

