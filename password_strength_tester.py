# EE, password strength

password = input("Enter a password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(c in "!@#$%^&*" for c in password):
    score += 1

if score == 5:
    print("Strong")
elif score >= 3:
    print("Medium")
else:
    print("Weak")
