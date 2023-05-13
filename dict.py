car_0 = {
    "model": "ferrari",
    "color": "Red"
}
car_1 = {
    "model": "Lacetti",
    "color": "White"
}



# print(car_0["color"])

en_uz = {
    "apple": "olma",
    "banana": "banan",
    "strawberry": "qulupnay"
}
# print(en_uz)

# word = input("Input here: ")

# if en_uz[word]:
#     print(en_uz[word])
# else:
#     print("natog'ri")


en_uz["cherry"] = "Gilos"
# print(en_uz.items())

# for key, value in en_uz.items():
#     print(f"key: {key}")
#     print(f"value: {value}\n")

phones = {
    "Mike": "iphone 13",
    "Jonathan": "Galaxy S21",
    "Mo": "iphone 13",
    "Nike": "Mi 42"
}

# for name,phone in phones.items():
#     print(f"{name} has {phone}")

# print(en_uz.values())

#set() - function that deletes repeating values 
#sorted - function sorts from a - z or just nunmbers high to low

# for phone in sorted(phones.values()):
#     print(phone.title())

# for phone in set(phones.values()):
#     print(phone.title())


# set is a variable

toys = {"soccer ball", "Basketball", "car", "Dinosour", "car"} # Doesnt allow reapiting values
# print(toys)

cars = [car_0, car_1]

# for car in cars:
#     print(f"Car is {car['model']} and it's collor is {car['color']}") # have to use ''

# print(cars[0]['model'])

lacettis = []

for n in range(1,4):
    new_car = {
        "model": "lacetti",
        "color": None,
        "price": None,
        "mode": "automatic"
    }
    lacettis.append(new_car)

# for car in lacettis[:3]:
#     car['color'] = 'red'

programmers = {
    "bekhzod": ["python", "php"],
    "shohjaxon": ["Python", "javascript", "c++"],
    "mike": ["c#"]
}

for name, languages in programmers.items():
    print(f"{name.title()} knows the follow coding languages: ")
    for language in languages:
        print(language.upper())