A = 50
B = 75

# Adding two numbers A+B 
result = A + B

# printing the values of two Numbers  
print("Result of {0} and {1} is {2}" .format(A, B, result))
#here we set the format of the numbers as well
#format() is one of the string formatting methods in Python3, which allows multiple substitutions and value formatting. This method lets us concatenate elements within a string through positional formatting.

x, y, z = 10, 20, 30
print(x, y, z, sep = " -> ")
# Normal string
normal_string = "This is the varaible of the string"
print(normal_string)

# Multi line string
multiple_line_str = """This is the Variable of 
Multiple type string"""
print(multiple_line_str)

# Concat strings
a = "Python"
b = "3"
c = a + b
print(c)

# Formatting string
something = "This is python 3"
print("The output is: %s" %something)
