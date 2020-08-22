#Exercise 6 Greater than and equal too
y=6
x=input("Enter the number: ")
z=int(x)
if y>=z:
    print("True")
else:
    print("False")

# Exercise 7 Less than and equal too
y=6
b=input("Enter the number: ")
c=int(b)
if y<=c:
    print("True")
else:
    print("False")

# Exercise 8 and Operator
e=3
f=2
g=4
h=5

if e>f and g>h:
    print("True")
else:
    print("False")
# Exercise 9 Or Operator

if e>f or g>h:
    print("True")
else:
    print("False")

# Exercise 10 Multiple condition
Indian=["Samosa","Daal", "Naan"]
Chinese=["Egg Role", "Pot Sticker", "Fried Rice"]
Italian=["Pizza","Pasta","risatto"]

dish=input("Enter the dish name: ")

if dish in Indian:
    print("Indian")
elif dish in Chinese:
    print("Chinese")
elif dish in Italian:
    print("Italian")
else:
    print("Not In My Data base: ", dish)

