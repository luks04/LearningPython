def filter_function(element):
    try:
        if(element is not None):
            return element
    except Exception as error:
        print(error)


filtered_variable = filter(filter_function, (None, "PHP", "Java", None, 500, 0.33, "Python", [23, 24, 25], None))

print(filtered_variable)
print(list(filtered_variable))
