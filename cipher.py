# EE, Caesar Cipher

def caesar_shift(message, shift):
    result = ""

    for char in message:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


choice = input("Do you want to encrypt or decrypt? ").lower()
message = input("Enter your message: ")
shift = int(input("Enter the shift amount: "))

if choice == "decrypt":
    shift = -shift

result = caesar_shift(message, shift)

print("Result:", result)
