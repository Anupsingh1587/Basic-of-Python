# For Loop
# Exercise 1 Old Or Traditional Method for for loop

exp=[2340,2500,2100,3100,2980]
total=exp[0]+exp[1]+exp[2]+exp[3]+exp[4]
print(total)

#Exercise 2 New technique

total=0
for item in exp:
    total=total+item
    print(total)

#Exercise 3 Range of numbers

for i in range(1,11):
    print(i)


#Exercise 4 Square Root of range

for i in range(1,11):
    print(i*i)

#Exercise 5 Cube Root of range

for i in range(1,11):
    print(i**i)

#Exercise 6 Monthly Expenses

exp=[2340,2500,2100,3100,2980]
total=0
for i in range(len(exp)):
    print("month:",(i+1),"expense:",exp[i])
    total=total+exp[i]
print("total expense is:", total)

#Or difference
zxp=[2341,2500,2100,3100,2980]
total=0
for i in range(len(zxp)):
    print("month:",(i+1),"expense:",zxp[i])
    total=zxp[i]
print("total expense is:", total)

#Or difference
exp=[2340,2500,2100,3100,2980]
total=0
for i in range(len(exp)):
    print("month:",(i+1),"expense:",exp[i])
total=total+exp[i]
print("total expense is:", total)

# Exercise 7 For loop And Break

key_location="chair"
location=["garage","living room","chair","sofa"]
for i in location:
    if i==key_location:
        print("key is found in:",i)
        break
    else:
        print("key is not found:",i)

#Or
key_location=input("Enter the name of the location:")
location=["garage","living room","chair","sofa"]
for i in location:
    if i==key_location:
        print("key is found in:",i)
        break #break is used when your goal is achived
    else:
        print("key is not found:",i)

#Exercise 8 For loop and continue

fruits=["banana","apple","cherry"]
for x in fruits:
    if x=="apple":
        continue #if the "if condition" is satisfied it will jump back to for loop and excute the other statement in the list means it will drop the true statement
    print(x)

# Exercise 9 while loop
i=1
while i<=5:
    print(i)
    i=i+1

#or
i = 1
while i < 6:
  print(i)
  i += 1

#or

i = 1
while i < 6: # while condition will take only one condition until it find its statement gets true once done it will print the result
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Exercise 10 else in for loop
for i in range(6):
    print(i)
else:
    print("finally finished")


# Exercise 11 Nested loop

colour=["red","blue","green"]
fruits=["Apple","banana","Cherry"]
for x in colour:
    for y in fruits:
        print(x,y)

# Exercise 12 pass statement
''' For loop cannot be empty, 
but if you for some reason have a for loop with no content, 
put in the pass statement to avoid getting an error'''

for x in [0,1,2]:
    pass






