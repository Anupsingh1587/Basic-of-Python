#Exercise 1
c=8
d=9
def sum(a=6,b=7):
    print("a: ", a)
    print("b: ", b)
    print("c: ",c)
    total=a+b+c
    print("Total inside the function:",total)
    return total
n=sum(c,d)
print("Total outside the function1: ",n)

#Exercise 2
c=8
d=9
def sum(a=6,b=7):
    print("a: ", a)
    print("b: ", b)
    print("c: ",c)
    total=a+b+c+d
    print("Total inside the function:",total)
    return total
n=sum()
print("Total outside the function1: ",n)
