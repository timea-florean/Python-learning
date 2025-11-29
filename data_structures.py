#LISTS IN PYTHON

#creating a list
fruits=["apple", "kiwi", "banana", "cherry","mango"]
print("Original list: ", fruits)

#adding an element to the end of the list
fruits.append("orange")
print("The list after appending: ", fruits)

#inserting an element at a specific position
fruits.insert(1,"lemon")
print("The list after the insertion: ", fruits)

#removing an element
fruits.remove("banana")
print("The list after removing: ", fruits)

#accessing elements

for fruit_name in fruits:
    print("Fruit: ", fruit_name)
#OR
for index in range(len(fruits)):
    print(f"Fruit at index: {index} = {fruits[index]}")
#OR
print("First fruit: ", fruits[0])
print("Last fruit: ", fruits[-1])

#slicing a list 
print("First two fruits: ", fruits[0:2])

#TUPLES
#example:
#creating a tuple
colors=("red","purple", "blue")
print("Original tuple: ", colors)

#accesing tuple elements
print("First color: ",colors[0])
#tuples are immutable, so i cannot change their elements
#but i cam use the as keys in dictionaries where lists cannot
color_preferences={colors: "Anna's favorite colors"}
print(color_preferences)

#SETS
#example
#creating a set 
numbers={1,2,2,2,3,4,4,5}
print("Original Set: ", numbers) #duplicates will be automatically removed
#adding an element to a set
numbers.add(6)
print("after adding: ", numbers)

#removing an element
numbers.remove(1)
print("after removing: ", numbers)

#checking membership
print("Is 3 in numbers", 3 in numbers)

#operations: union, intersection, difference
a={1,2,3}
b={3,4,5,6}
print("Union: ", a|b)
print("Intersection: ",a&b)
print("Difference: ",a-b)

#DICTIONARIES
#example:
#creating a dictionary
person ={"name": "John ", "age": 30, "city": "New York"}
print("Original dictionary: ", person)

#accessing values by key 
print("Name: ", person["name"])

#adding a new key-value pair
person["job"]="Programmer"
print("After adding: ", person)

#removing a key-value pair
del person["age"]
print("After deletion: ", person)

#using the get method to avoid KeyError
print("Age: ", person.get("age", "Not available"))

#iterating over keys and values
for key, value in person.items():
    print(key, ":",value)