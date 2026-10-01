# EE, password strength

password= input("Enter a password:")

upper = False
lower = False
number= False
symbol = False

for letter in password:
    if letter. isupper():
        upper = True
    if letter. islower():
        lower = True
    if letter. isnumeric():
        number = True
    if letter in "!@#$%^&*":
        symbol = True
score = 0

if len(password)>= 8:
    score += 1
if upper:
    score += 1
if lower:
    score += 1
if number:
    score += 1
if symbol:
    score += 1

if score == 5:
    print("Strong")
elif score >= 3:
    print("Medium")
else:
    print("Weak")
