#example of a simple function in python
def greet():
    print("Hello, welcome to Pythom!")

#calling the function
greet()

#example of a function with parameters and a return value:
def add_numbers(num1,num2):
    result=num1+num2
    return result

#calling the function with parameters
sum_result=add_numbers(10,15)
print("sum: ", sum_result)

#using default parameters and keyword arguments:
def describe_pet( petName, animalType='cat'):
    print(f"I have a {animalType} named {petName},")

#calling function with default parameter
describe_pet(petName='Luna')
#calling function with both parameters explicitly
describe_pet(petName='Rex', animalType='dog')

#IMPORTING MODULES

import math
#using a function from the math module
print("The square root of 64 is: ", math.sqrt(64))

#importing specific functions

from math import sqrt, pow
#now no need to use 'math.' prefix
print("The square root of 25 is: ", sqrt(25))
print("2 raised to the power of 6 is: ", pow(2, 6))

#creating and importing your own modules

#lets suppose that you have a file named with a function defined in it 
#example: 
# mymodule.py
def multiply(a,b):
    return a*b

#you can import your module into another python script
#import the entire module
#import mymodule
#result=mymodule.multiply(4,5)
#print("Product: ", result)

#import specific function

#from mymodule import multiply 
#result=multiply(4,5)
#print("Product: ", result)

#MODULE ALIASES
#you can import a module or function under a different name using the keyword
#example:
#import mymodule as mm
#result =mm.multiply(6,7)
#print("Product: ", result)
