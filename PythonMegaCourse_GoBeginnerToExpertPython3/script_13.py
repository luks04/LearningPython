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
