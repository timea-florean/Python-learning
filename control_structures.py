age=20
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

score=75
if score>=90:
    print("Grade A")
elif score>=80:
    print("Grade B")
elif score>=70:
    print("Grade C")
else:
    print("Grade D or Lower")

#iterating over a list 
#using a for loop
fruits=["apple", "banana", "cherry"]
for fruit in fruits:
    print("Current fruit:", fruit)

    
#using a while loop to count to 5
count=1;
while count<=5:
    print("count: ", count)
    count+=1

#example of nested loops
#nested for loops to irerate over a grid layout
for i in range(1, 4):
    for j in range(1,4):
        print(f'{i}, {j}', end=' ')
    print() #new line after each row

#using nested loops and conditionals to find the first even number in each list
list_of_lists= [[1,3,5],[2,4,6],[9,7,5],[10,8,6]]

for sublist in list_of_lists:
    for number in sublist:
        if number%2==0:
            print("First even number in list: ", number)
            break #breaks out of the inner loop

#print numbers from 1 to 10, skip numbers divisible by 3
for i in range(1, 20):
    if(i%3==0):
        #skip the rest of the code inside the loop for current iteration
        continue 
    print(i)


