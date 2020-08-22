#Exercise 6 Simple Numbers Program

def pattern(n):
    x = 0
    for i in range(0 , n):
        x += 1
        for j in range(0, i + 1):
            print(x , end=" ")
        print("\r")
pattern(5)

# exercise 7 Half-Pyramid Pattern Program

def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(5)

#Exercise 8 Left Half-Pyramid Pattern Program

def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(5)

# Erxercise 9 Downward Half-Pyramid Pattern Program

def pattern(n):
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

pattern(5)

# Exercise 10 Diamond Shaped Pattern Program
def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(5)
# website were i got this program list https://medium.com/edureka/python-pattern-programs-75e1e764a42f
