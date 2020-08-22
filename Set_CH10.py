# Set is a collection which is unordered and unindexed. No duplicate members. Set are written with curly brackets {}
# Exercise 1 Add items in Set
x={"Apple","Banana","cherry"}
x.add("Orange")
print(x)

# exercise 2 update multiple items to a set, using update method
x={"Apple","Banana","cherry"}
x.update(["Orange", "Mango", "Grapes"])
print(x)

# Exercise 3 Get the Length of a Set
x= {"apple", "banana", "cherry"}
print(len(x))

# Exercise 4 Remove Item
x={"apple", "banana", "cherry"}
x.remove("banana")
print(x)

#Exercise 4 Discard method
x={"apple", "banana", "cherry"}
x.discard("banana")
print(x)

# Exercise 5 pop method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#Exercise 6 clear Method
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#Exercise 7 Delete the set completely
'''thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)'''
# this will raise an error because the set no longer exists

#Exercise 8 union method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#Exercise 9 update method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Exercise 10 The set() Constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.