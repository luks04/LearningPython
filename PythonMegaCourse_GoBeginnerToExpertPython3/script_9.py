vowels = ["a", "e", "i", "o", "u"]

for vowel in vowels:
    print(vowel)

i = 1
while i < 10:
    print(i)
    i += 1

def showEmployee(name, salary = 2000):
    print("Employee", name, "salary is:", salary)



showEmployee("bob", 2000)

showEmployee("bob")