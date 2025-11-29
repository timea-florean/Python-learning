#exception handling --> building robust python applications
#what are exceptions?
#exceptions = special objects that the program creates when it encounters an error
#when an error occurs, python creates an exception object

#example of an exception:

numbers= [1,2,3,4]
try:
    print(numbers[4]) #so basically this will raise an index error because index 3 does not exist
except IndexError as e:
    print("Error: ", e)

#example of handling multiple exceptions:
#handling multiple exceptions with multiple except blocks
try: 
    #this block will try to execute this code
    value=int(input("Please enter a number: "))
    result=10/value
except ValueError:
    #executed if a value error occurs during the try block
    print("You must enter a valid integer!")
except ZeroDivisionError:
    #executed if a zero division error occurs
    print("Division by zero is not allowed!")
else:
    #executed if no exceptions occur
    print("The result is: ", result)
finally:
    #always executed, regardless f whether an exception occured or not
    print("This block is always executed :))")

#example of raising an exception
def checkAge(age):
    if age<0:
        raise ValueError("Age cannot be negative!")
    elif age<18:
        print("You are not old enough.")
    else:
        print("You are welcome!")

try: 
    user_age=int(input("Enter your age: "))
    checkAge(user_age)
except ValueError as e: 
    print("Error: ", e)

#now lets take an example of a custom exception

class NegativeAgeError(Exception):
#Exception raised when the age is negative
    def __init__(self, age):
        self.message = f"Age {age} is not valid. Age cannot be negative."
        super().__init__(self.message)
def check_age(age):
    if age < 0:
        raise NegativeAgeError(age)
    print(f"Age {age} is valid.")
try:
    check_age(-5)
except NegativeAgeError as e:
    print(e)