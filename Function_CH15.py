c=30
d=40
def sum(a=10,b=20):
    print("a: ",a)
    print("b: ",b)
    total=a+b
    print("Total inside the body: ",total)
    return total
n=sum()
print("Total outside the body: ",n)

def mult(c,d):
    print("c: ",c)
    print("d: ",d)
    print("n: ",n)
    total=c*d+n
    print("Multiple of two variable: ",total)
    return total
m=mult(c,d)
print("value of m: ",m)

def sub():
    total=m-n
    print("Total value after subraction: ",total)
    return total
s=sub()
print("Total value after substraction: ",s)






