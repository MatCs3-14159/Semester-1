"""4.1 Write a Python program that encrypts and decrypts text files using a substitution cipher.
Your program should ask the user for the name of a text file and whether they would like to encrypt or decrypt.
Once the process is complete, you should write the output to a new text file with a modified name: 
    This program will encrypt and decrypt text files 
    1. Enter (e) to encrypt a password, and (d) to decrypt: e 
    2. Enter the name of a text file to encrypt: hello.txt 
    3. Output written to: encrypted_hello.txt 
Your program should catch exceptions and print helpful error messages.
You should use your solution to Coding Challenge 04 to help you."""
def caesar_cipher(text, shift):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += ch
    return result
try:
    choice = input("Enter (e) to encrypt or (d) to decrypt: ").lower()
    if choice not in ('e', 'd'):
        print("Invalid choice. Enter 'e' or 'd'.")
    else:
        filename = input("Enter the name of a text file: ")
        with open(filename, "r") as infile:
            content = infile.read()
        shift = 12
        if choice == 'd':
            shift = -shift
        output_text = caesar_cipher(content, shift)
        output_filename = ("encrypted_" if choice == 'e' else "decrypted_") + filename
        with open(output_filename, "w") as outfile:
            outfile.write(output_text)
        print("Output written to:", output_filename)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("Unexpected error:", e)
