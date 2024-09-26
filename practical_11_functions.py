# -*- coding: utf-8 -*-
"""practical 11 functions

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AObqHcDFSTHdzZgRCK8kn0GqqKdchqD5
"""

#Functions
# Reusablity of code
#def.....defines the function structure
#def function_name(arguments):
  #code_to_run
def print_name(name):
 print(name)

print_name("Anita")

def area(radius):
  print(3.14 * radius * radius)
area(4)

def sum(a,b):
  print(a+b)

sum(2,3)

#return
#will return the value specified after it
#can only be used inside a function
#return the cursor to the line where the function was defined
def sum(a,b):
  return a+b
sum(2,3)

#types of arguments
#positional arguements
#default
#keyword
#variable length arguments
   #positional variable length
   #keyword variable length

#positional arguments.....we do not pass the name of the variable(only the value is to pass)

def sub(a,b):
  return a-b
sub(2,3)

#keyword arguments
#when we pass the variable along with the value
def greet(greetings,name):
 print(f'{greetings},{name}')

greet(name="Anita",greetings='Hello')

sub(a=2,b=3)

#default arguments
#when we need to set a default value
def greet(name,greetings="hello"):
 print(f'{greetings},{name}')

greet(name="Anita")

def greet(name,greeting="hey"):
 print(f'{greeting},{name}')

greet(name="Anita",greeting="hi")

#variable length arguments
#length of variable is not fixed which means the number of variables that cane be passed is not fixed.
#posional variable length

def addition(*num):
 return sum(num)

addition(2,5,4,3)

#keyword variable length arguments
#can pass many values while calling the function but in key value pair
#need to pass the variable with double stars(**) while forming the function
def information(**info):
  for key, value in info.items():
    print(f'{key} is {value}')

information(name="Anita",age=20)

def a(**info):
  for key,value in info.items():
    print(f'{key}:{value}')

a(collage='JECRC',location='jagatpura',coarse='bca')

#Types of function
#Built in functions........functions predefined by python & can be used anytime
#len()  print()
#user define functions......define by user using def keyword.
#we form these functions to reuse them anytime.

#scope of variables
#local variable.....used inside the function
'''def hello():
x=5.....local variable'''
#global variable.....can be used outside or inside the function.
'''y=10
def hello():
  x=5
y is a global variable'''

y=10
def my_function():
 x=5
 print(x,y)
my_function()

y=10
def my_function2():
 y=9
 print(y)
my_function2()

print(y)

#conversion
#global keyword
#covert the variable from local to global
def my_function3():
 global y
 y=9
 print(y)
my_function3()

print(y)