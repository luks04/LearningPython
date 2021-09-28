print("\n####################################################################")
print("########################## STR FORMAT ##############################")
print("####################################################################\n")

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

print("\n\n####################################################################")
print("######################### NUMBER FORMAT ############################")
print("####################################################################\n")

################################## 
# DECIMAL | HEXADECIMAL | BINARY # 
#    0    |      0      |  0000  # 
#    1    |      1      |  0001  # 
#    2    |      2      |  0010  # 
#    3    |      3      |  0011  # 
#    4    |      4      |  0100  # 
#    5    |      5      |  0101  # 
#    6    |      6      |  0110  # 
#    7    |      7      |  0111  # 
#    8    |      8      |  1000  # 
#    9    |      9      |  1001  # 
#   10    |      A      |  1010  # 
#   11    |      B      |  1011  # 
#   12    |      C      |  1100  # 
#   13    |      D      |  1101  # 
#   14    |      E      |  1110  # 
#   15    |      F      |  1111  # 
################################## 

print("Binary format        -> 0b### -> ", 0b1001)
print("Hexadecimal format   -> 0x### -> ", 0xF2B33)
print("Octal format         -> 0o### -> ", 0o12307)