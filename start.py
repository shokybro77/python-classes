import math;

# print("15-problem")

# S = 13
# pi = 3.14

# R = math.sqrt(S/pi)
# print(R)

# print("16-problem")

# x1 = 4
# x2 = 16

# ans = x2 - x1
# print(ans)

# print("17-problem")

# a = 4
# b = 7
# c = 14

# ac = c - a
# bc = c - b

# total = ac + bc
# length = ac - bc
# print(total, length)


# Lists

fruits = ["Banana", "Apple", "Pineapple", "YourMom"]
fruit = "strawberry"
fruits.append(fruit)
print(fruits)

# It will sort in alphabetical order
fruits.sort()
print(fruits)

# Sort method will sort list for you
numbers = [2, 32, 112, 324, 2, 1, 4, 5,8, 2,]
print(numbers)
numbers.sort()
print(numbers)

# To get the last number
print(numbers[-1])


# Reverse sort
numbers.sort(reverse=True)
print(numbers)

# Reverse order of list

fruits.reverse()
print(fruits)

# To find the length of the list (counting in coding starts at 0)
print(len(numbers))

# Find the range of list

numbers = list(range(1, 13))
print(numbers)

# to get toq sonlar you need to do list(0, 10 ,2)

# Will give you the biggest number on the list
print(max(numbers))
# Will give you the lowest number on the list
print(min(numbers))
# Will give you the total (Adding all of the numbers)
print(sum(numbers))

# to cut a list 
print(numbers[0:3])
print(numbers[:4])

# To copy a list
my_fruits = fruits[:]
print(my_fruits)


# Tuples - A constant lists

toys = ("teddy", "car", "pistol", "ball")

print(toys)

# For loop

mehmonlar = ["Ali", "Kamol", "Shohjaxon", "Murod"]

for mehmon in mehmonlar:
    print(f"Salom {mehmon}!") # You can use f print to put variables in string


sonlar = list(range(1,11))
kvadratlar = []

for son in sonlar:
    kvadratlar.append(son ** 2)

print(kvadratlar)

mehmonlar = []

# for n in range(5):
    # mehmonlar.append(input(f"{n+1}-do'stingizni kiriting"))

# print(mehmonlar)


# OR == ||, AND == &&



# if statements

son = 42

if son >= 0:
    print("The number is positive")
elif son <= 0:
    print("The number is Negetive")
else:
    print("The number is 0")


print("Apple" in fruits) # Wethear that element is in the list