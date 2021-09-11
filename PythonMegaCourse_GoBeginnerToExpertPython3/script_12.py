dictionary = {
    "car": "BMW",
    "model": 2019
}

print(dictionary)

print("----------------------------------------------------------------")

other_dictionary = dict(
    first_name = "Frank",
    second_name = "Jr"
)

print(other_dictionary)

print("----------------------------------------------------------------")

print("Original dictionary", dictionary)
aux = {
    "car": "Ford Mustang"
}
dictionary.update(aux)
print("Updated dictionary", dictionary)

print("----------------------------------------------------------------")

print("Original dictionary", dictionary)
more_data = {
    "cc": 4200
}
print(len(dictionary))
dictionary.update(more_data)
print(len(dictionary))
print("Updated dictionary", dictionary)

print("----------------------------------------------------------------")

cars = {
    "BMW": 2012,
    "Honda": 2019,
    "Ford": 2020
}

print(cars)
del cars["Honda"]
print(cars)

if "Ford" in cars:
    print("Yes, it is available")
else:
    print("No, it is not available in the cars dictionary")

cars.clear()
print(cars)
del cars
# print(cars) -> NameError: name 'cars' is not defined
