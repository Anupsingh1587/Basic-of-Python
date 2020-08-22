# Dictionary is a collection which is unordered , changeable and indexed. NO duplicate numbers.
# Dictionaries are written in the curly brackets and they have key and values

#Exercise 1
dict={"Brand":"Ford","Model":"Mustang","Year":"1964"}
x=dict["Model"]
y=dict["Brand"]
z=dict["Year"]
print(x)
print(y)
print(z)


#Or
'''d={"Brand":"Ford","Model":"Mustang","Year":"1964"}
z=d
z=(input("Enter the Name: "))
print("Name is : ", z)'''

d={"Anup":9654644865,"Puja":7325730239,"mom":9654892306}
print(d) #print the key and value together

print(d["Anup"]) #print the value of anup

d["papa"]=9432146789 #Too add the value papa in dictionary
print(d)

del d["papa"]# Too delete the value of papa from d
print(d)

d={"Anup":9654644865,"Puja":7325730239,"Mom":9654892306}
for key in d:
    print("key:", key,    "Value:", d[key])

d.clear()
print(d)
















