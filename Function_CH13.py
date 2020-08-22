# GLobal Vs Local Variable
#Exercise 1
total=0
def mult(a,b):
    print("a: ",a)
    print("b: ",b)

    total=a*b
    print("total inside the function: ",total)
    return total
n=mult(5,6)
print("Total: ",n)
print("Total outside function: ",total)

#Exercise 2 Default arguments in function
''' Means, if you are not going to send me a second arguments then this is called to be a default arguments'''
def sum(a,b=7):
    print("a: ", a)
    print("b: ", b)

    total=a+b
    print("Total inside the function:",total)
    return total
n=sum(5,) # or we can define it (5,8)
print("Total outside the function1: ",n)
print("Total outside the function2: ",total)

# My Logic Exercise 1
total=0
def sum(a,b):
    print("a: ",a)
    print("b: ",b)
    total=a+b
    return total
print("Total outside the function: ",total)

# Exercise 2
c=8
d=9
total=c+d
def sum(a=6,b=7):
    print("a: ", a)
    print("b: ", b)
    print("c: ",c)
    total=a+b+c
    print("Total inside the function:",total)
    return total
n=sum()
print("Total outside the function1: ",n)
print("Total outside the function2: ",total)

# Exercise 3
e=8
f=9
def sum(a=6,b=7):
    print("a: ", a)
    print("b: ", b)
    print("c: ",c)
    total=a+b+f
    print("Total inside the function:",total)
    return total
n=sum(e,f)
#print("Total outside the function1: ",n)
#print("Total outside the function2: ",total)


