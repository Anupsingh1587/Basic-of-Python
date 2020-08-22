#Exercise 1 change item from list to tuple and back again to tuple
# Tuples is a collection which is ordered and unchangeable. Allows duplicate members. Tuples are written in round bracket ()
x=("Apple","Banana","cherry")
y=list(x)
y[1]="Kiwi"
x=tuple(y)
print(x)

#Exercise 2
point=(5,9)
print(point[0]) # 5 is in x co-ordinate
print(point[1]) # 9 is in y co-ordinate

point[0]=50
print(point[0]) # It will give an error because tuple doesn't support item assignment






