#Function
# Exercise 1 find the total of two list using function

Anup_exp_list=[2100,2000,1900,1800]
Puja_exp_list=[3100,3000,2900,2800]
total=0
for item in Anup_exp_list:
    total=total+item
print("total of Anup exp list: ", total)
total=0
for item in Puja_exp_list:
    total=total+item
print("total of Puja exp list: ", total)

#Exercise 2
def calculate_total (exp):
    total=0
    for item in exp:
        total=total+item
    return total
Anup_exp_list=[2100,2000,1900,1800]
Puja_exp_list=[3100,3000,2900,2800]

Anup_total=calculate_total(Anup_exp_list)
Puja_total=calculate_total(Puja_exp_list)

print("Anup total expenses: ",Anup_total)
print("Puja total expenses: ",Puja_total)

# Exercise 3 Sum of two numbers using function
def sum(a,b):
    total=a+b
    return total
n=sum(5,6)
print("Total:", n)

# Exercise 4 Sum of two numbers by different method
def sum(a,b):
    print("a: ", a)
    print("b: ", b)
    total=a+b
    print("Total Inside function: ", total)
    return total
z=sum(7,8)
print("Total outside the function: ",z)

