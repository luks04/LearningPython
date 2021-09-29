import re

if not re.search("Frank", "Mark and Julia were talking yesterday"):
    print("Frank was not there")

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

# Check password strength
password = input("Enter string to test: ")
if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
    print(">>> Congrats, it is a secure password")
else:
    print(">>> Really? Too easy!")
