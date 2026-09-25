# EE, Loops Notes

# code that will repeat over and over again
import random


count=1

while count <=10:
    print(count)
    count+=1

goose = random.randint(1,11)
ducks = 1

while True:
    print('duck')  
    if ducks == goose:
        break
    ducks+=1
print("GOOSE!!!!")

siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]

print(siblings[2])

print(siblings)

siblings.append("Jayshree")
siblings.insert(3,"Vienna")

print(siblings)

#remove from list
print(siblings.pop(3))
print(siblings)

# for loops
for number in range (1,11,2):
    print(number)

for sibling in siblings:
    print(sibling + " LaRose")
