# EE, String Notes
first_name = 'Elsie'
last_name = 'ewell'
# concatenation=> add two string together
name= first_name+" "+ last_name
# escape char lets the program ignore the next characheter in string
print(f'{first_name}told the class "you can\'t drive my car."')

user = input("Please tell me your name\n:").strip().title()

print(f"New user recognized\nWelcome {user}")

sentence= "The quick brown fox jumped over the lazy dog"



print(sentence)

print(sentence.replace("dog", name))