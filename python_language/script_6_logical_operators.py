a = 10
b = 20
c = -10

if a > 0 or c > 0:
    print("Atleast one numbers is greater than 0")
elif a > 0 and b > 0 and c > 0:
    print("All the numbers are greater than 0")
elif not a == 20:
    print("The number is not equal to 20")
else:
    print("Atleast one number is not greater than 0")

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

# Compare bits with this operators
print(4 & 5) # "And" bitwise operator
print(4 | 5) # "Or" bitwise operator
print(~4)  # "Complement" bitwise operator
print(4 ^ 5)  # "Xor" bitwise operator

if 50 | 100 == 50:
    print("Anything")
elif 50 & 100 == 32:
    print("Something")

########################
# HEXADECIMAL | BINARY # 
#      0      |  0000  # 
#      1      |  0001  # 
#      2      |  0010  # 
#      3      |  0011  # 
#      4      |  0100  # 
#      5      |  0101  # 
#      6      |  0110  # 
#      7      |  0111  # 
#      8      |  1000  # 
#      9      |  1001  # 
#      A      |  1010  # 
#      B      |  1011  # 
#      C      |  1100  # 
#      D      |  1101  # 
#      E      |  1110  # 
#      F      |  1111  # 
########################

a = 50

if a > 50:
    print("a is grater than 50")
elif a < 30:
    print("a is smaller than 30")
else:
    print("a is equal to 30")


math = 90
science = 75
music = 100
if math > science and math < music:
    print(f"Music is the highest grade: {music}")
elif math > science and math > music:
    print(f"Math is the highest grade: {math}")
elif math < science and math > music:
    print(f"Science is the highest grade: {science}")
else:
    print("Other grade is the highest")
