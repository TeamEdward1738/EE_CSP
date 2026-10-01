# EE, Caesar Cipher

def caesar_shift(message, shift):
    result = ""

    for letter in message:
        if letter.isupper():
            result += chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        elif letter.islower():
            result += chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += letter

    return result


choice = input("Do you want to encrypt or decrypt? ").lower()
message = input("Enter your message: ")
shift = int(input("Enter the shift amount: "))

if choice == "decrypt":
    shift = -shift

result = caesar_shift(message, shift)

print("Result:", result)
