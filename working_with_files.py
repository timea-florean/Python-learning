#create a file!
#example of reading from a file
#make sure that you write something in the file
try:
    with open('example.txt', 'r') as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("File not found")

#example of writing to a file
#writing to a file, overwriting existing content
with open('example.txt', 'w')as file:
    file.write("Hello, Python user!\n")
    file.write("Writing to files is essential")

#appending to a file without overwriting it
with open('example.txt', 'a')as file:
    file.write("\n Hi, Python user! Nice to meet you!\n")

#working with CSV files
import csv 
#writing to a CSV file 
with open('example.csv','w',newlie='')as file:
    writer=csv.writer(file)
    writer.writerow(["Name: ", "Age: "])
    writer.writerow(["Alice", 25])
    writer.writerow(["Alex",20])

#reading form a CSV file
with open('example.csv', 'r')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#working with JSON files:

import json

data={
    "name ": "John", "age":25, "city":"New York"
}
#writing JSON to a file
with open('data.json', 'w')as file:
    json.dump(data, file)
#reading JSON from a file
with open('data.json', 'r')as file:
    data=json.load(file)
    print(data)

#example of safely handling File Paths and reading large files
import os
file_path=os.path.join('path','to', 'your','file.txt')
try:
    with open(file_path, 'r')as file:
        while True:
            line=file.readline()
            if not line:
                break
            print(line.strip())#using strip to remove the newline character
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error occured!!! {e}")
