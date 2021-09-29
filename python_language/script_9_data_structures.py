from collections import deque
#from binarytree import Node
import random

#########################################################################
############################## TUPLES ###################################
#########################################################################
print("============================ TUPLES ====================================\n")

tuple_1 = ()
tuple_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple_3 = ("Python", "Ruby", "Java", "PHP")
print(tuple_1)
print(tuple_2)
print(tuple_3)
print(tuple_3[0])
print(tuple_3[1])
print(tuple_3[2])
print("tuple_3: ", tuple_3)
del tuple_3
# print("tuple_3: ", tuple_3) -> NameError: name 'tuple_3' is not defined
print("----------------------------------------------------------------")
print(tuple_2[1:4])
print(tuple_2[:4])
print(tuple_2[5:])
print(tuple_2[:])

#########################################################################
############################### LISTS ###################################
#########################################################################
print("\n\n============================ LISTS ====================================\n")

my_list = []
my_list.append("Some")
my_list.append("Word")
my_list.append("Yes")
print(my_list)
my_list[1] = "Anything"
print(my_list)
my_list.remove("Anything")
print(my_list)
print("----------------------------------------------------------------")

print("----------------------------------------------------------------")
num_list = [x for x in range(20) if x % 2 == 0]
print("List from for loop inside [] -> ", num_list)

number_list = [x for x in range(20) if x % 2 == 0 if x % 5 == 0]
print("List from for loop inside [] -> ", number_list)

number_str_list = ['Good' if x % 3 == 0 else "Bad" for x in range(10)]
print("List from for loop inside [] -> ", number_str_list)

# Truncate a matrix using list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(3)]
print("Truncate a matrix using list comprehension -> ", transpose)
print("----------------------------------------------------------------")

print("----------------------------------------------------------------")
my_other_list = list()
my_other_list.append(1)
my_other_list.append(4)
my_other_list.append(19)
print(my_other_list)
print("----------------------------------------------------------------")

print("----------------------------------------------------------------")
example_list = ["Python", "Ruby", "Java"]
if "Java" in example_list:
    print("Yes")
else:
    print("No")
print("----------------------------------------------------------------")

print("----------------------------------------------------------------")
for item in example_list:
    print(item)
print("----------------------------------------------------------------")

print("----------------------------------------------------------------")
american_countries = ["Brazil", "Chile", "Canada"]
europe_countries = ["Germany", "England", "UK"]
print(american_countries)
print(europe_countries)
print(american_countries + europe_countries)

merged_countries = list()
merged_countries.extend(american_countries)
merged_countries.extend(europe_countries)
print("----------------------------------------------------------------")

print("----------------------------------------------------------------")
print(merged_countries)
random.shuffle(merged_countries)
print(merged_countries)
print("----------------------------------------------------------------")


#########################################################################
########################## LISTS AS STACKS ##############################
#########################################################################

print("\n\n============================ LISTS AS STACKS ====================================\n")
# Using list as a Stack
example_list.append("PHP")
print(example_list)
last_item = example_list.pop()
print(example_list, "-> Last item: ", last_item)
last_item = example_list.pop()
print(example_list, "-> Last item: ", last_item)
last_item = example_list.pop()
print(example_list, "-> Last item: ", last_item)

#########################################################################
############################## QUEUES ###################################
#########################################################################
print("\n\n============================ QUEUES ====================================\n")

# Using list as a Queue
queue = deque(['Python', 'Ruby', 'Java', 'PHP'])
print(queue)
queue.append('JavaScript')
print(queue)
first_item = queue.popleft()
print(first_item, "-> First item: ", first_item)
print("----------------------------------------------------------------")

#########################################################################
############################ DICTIONARIES ###############################
#########################################################################
print("\n\n============================ DICTIONARIES ====================================\n")

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

my_dictionary = {1: "Rojo", 2: "Azul", 3: "Morado"}
print(my_dictionary)
print(my_dictionary[2])
print(my_dictionary.keys())

my_dictionary.items()

def dictionary_from_arrays_example():
    array1 = ['A', 'B', 'C', 'D']
    array2 = [10, 20, 30, 40]
    tuple_list = zip(array1, array2)
    dictionary = dict(tuple_list)
    print(dictionary)

dictionary_from_arrays_example()

#########################################################################
################################ SETS ###################################
#########################################################################
print("\n\n============================ SETS ====================================\n")

my_set = {1, 2, 3, 4, 5, 6}
print(my_set)

print("----------------------------------------------------------------")

aux_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9]
example_set = set(aux_list) # Ignore duplicates
print(example_set)
print(len(example_set))

print("----------------------------------------------------------------")
s1 = set()
s1.add("a")
s1.add("b")
s1.add("c")
s1.add("d")
s1.add("d")
s1.add("d")
print(s1)

s2 = {"A", "B", "C"}
s1.update(s2)
print(s1)

#########################################################################
############################ BINARY TREES ###############################
#########################################################################
print("\n\n============================ BINARY TREES ====================================\n")

#root = Node(3)
#root.left = Node(5)
#root.right = Node(9)

#print("Binary tree", root)