# EE, Caesar Cipher

def caesar_shift(message, shift):
    result = ""

    for chr in message:
        if chr.isupper():
            result += chr((ord(chr) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(chr) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += chr

    return result


choice = input("Do you want to encrypt or decrypt? ").lower()
message = input("Enter your message: ")
shift = int(input("Enter the shift amount: "))

if choice == "decrypt":
    shift = -shift

result = caesar_shift(message, shift)

print("Result:", result)
