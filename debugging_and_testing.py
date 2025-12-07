#Debugging techniques
#1.print statement debugging

def calculate_sum(numbers):
    total=0
    for number in numbers:
        total+=number
        print(f"Added {number}, total now {total}") #debug print
    return total
print(calculate_sum([2,3,5,6]))

#2.using assertions
def calculate_average(numbers):
    assert len(numbers)>0, "List of numbers is empty."
    total=sum(numbers)
    return total/len(numbers)
print(calculate_average([2,3,4,5]))

#interactive debugging

import pdb
def calculate_sum1(numbers):
    pdb.set_trace() #start the debugger here
    total=0
    for number in numbers:
        total+=number
    return total
print(calculate_sum1([2,3,4,5]))
