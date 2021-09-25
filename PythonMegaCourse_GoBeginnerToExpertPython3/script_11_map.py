def map_to_something(element):
    value = f"The element formatted as str: {str(element)}"
    return value


maped_variable = map(map_to_something, ("PHP", "Java", "Python"))

print(maped_variable)
print(list(maped_variable))
