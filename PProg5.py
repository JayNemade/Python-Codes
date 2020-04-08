#FUNCTIONS

#A basic function
def helloWorld():
	print("Hello World! from a function")


helloWorld()	

#Parameters in function

def sum(a,b):
   print(a+b)


sum(12,23)

#Default values in functions

def country(country = "India"):
      print("I am from " + country)


country('Norway')
country()

#return statement

def multiple_5(x):
	return 5 * x

print(multiple_5(12))

#Lambda

"""Lambda is a small anonymous function in python
allows multiple argumments and one expression"""

x = lambda a: a+10

print(x(5))

#lamda is best used anynonymously in functions 

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))