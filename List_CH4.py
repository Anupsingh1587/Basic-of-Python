'''Exercise 1 read the item for the list'''
Item1="Bread"
Item2="Pasta"
Item3="Fruits"
Item4="Vegitables"
print(Item1)
print(Item1[0])

'''Exercise 2 '''
Items=["Anup", "Puja", "Indar", "Malti"]
print(Items)
print(Items[0])
'''The difference in Row number 7 & 12 is, from the row 7 string we are just calling Index value [0] 
were as from row 12 we are just calling the Items of row 10 Assigning the index [0] to it.'''

'''Exercise 3 to change the value of the index List 10'''
Items[0]="Ashish"
print(Items)

'''Exercise 4 to check the range of value in index'''
print(Items[0:2])

'''Exercise 5 to check the last elements i the index'''
print(Items[-1])

'''Exercise 6 to check append function in the list means add new item in the list'''
Items.append("Preeti")
print(Items)

'''Exercise 7 Use of Insert function in the list'''
Items=["Anup", "Puja", "Indar", "Malti"]
Items.insert(1,"Preeti")
print(Items)

'''Exercise 8 Join two items of the list'''
Item7=["Puna", "Jaipur","Lucknow"]
Item8=["Maharashtra","Rajasthan","Uttar pradesh"]
Item9=Item7+Item8
print(Item9)

'''Exercise 9 Lenth function in list'''
Item7=len(Item7)
print(Item7)

'''Exercise 10 to read elements in list'''
Items=['Anup', 'Puja', 'Indar', 'Malti']
Items= 'Had' in Items
print(Items)

Item7=["Puna", "Jaipur","Lucknow"]
Item7="Puna" in Item7
print(Item7)
