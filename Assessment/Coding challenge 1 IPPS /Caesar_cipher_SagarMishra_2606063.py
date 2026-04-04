"""
    Project name: Caesar_cipher_2606063.py
    Author: Sagar Mishra
    Student ID: 2606063
    Description: Caeser Cipher encryption and decryption program
"""

import os


def welcome():
    """
        Display the welcome message to the user  and show what the program does
    """
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")

def enter_message():
    """
        Prompt the user to enter a mode, message and shift number.

        Returns:
            tuple: (mode, message, shift)
    """
    while True:
        mode = input ("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ("e","d"):
            break
        print("Invalid Mode")

    message = input (
        f"What message would u like to {'encrypt' if mode == 'e' else 'decrypt'}: "
        ).upper()

    while True:
        shift = input ("What is the shift number: ")
        if shift.isdigit():
            shift = int(shift) % 26
            break
        print("Invalid Shift")

    return mode, message, shift

def encrypt(message, shift):
    """
        This part encrypts the message

        Arguments:
            message (str): plain text meaage 
            shift (int): shift number

        Returns:
            str: Encrypted message
    """
    encrypted_message = ""

    for ch in message:
        if ch.isalpha():
            encrypted_message += chr((ord(ch) + shift - 65) % 26 + 65)
        else:
            encrypted_message += ch

    return encrypted_message

def decrypt(message, shift):
    """
        This part decrypts the message

        Arguments:
            message (str): plain text meaage 
            shift (int): shift number

        Returns:
            str: Decrypted message
    """
    decrypted_message = ""

    for ch in message:
        if ch.isalpha():
            decrypted_message += chr((ord(ch) - shift - 65) % 26 + 65)
        else:
            decrypted_message += ch

    return decrypted_message

def process_file(filename, mode, shift):
    """
       Process the file line by line and encrypt/decrypt each line.

       Arguments:
           filename (str): Input file
           mode (str): 'e' or 'd'
           shift (int): shift number

        Returns:
            result (list): Processed messages
    """
    result = []
    try:
        with open(filename,"r", encoding = "utf-8") as file:
            for line in file:
                line = line.strip().upper()
                if mode == "e":
                    result.append(encrypt(line,shift))
                else:
                    result.append(decrypt(line,shift))
        return result
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
        return []
    except UnicodeDecodeError:
        print(f"Error: Cannot read '{filename}' (encoding issue).")
        return []

def is_file(filename):
    """
        Checks if the file exists 
    """
    return os.path.isfile(filename)

def write_messages(messages):
    """
        Creates a file result.txt and writes the processed result in it.

        Argument:
            messages (list): List of string
    """
    try:
        with open("results.txt", "w", encoding = "utf-8") as file:
            for message in messages:
                file.write(message + "\n")
    except PermissionError:
        print("Error: Cannot write to file.")
    except OSError as e:
        print(f"Unexpected error while writing file: {e}")

def message_or_file():
    """
        Asks wether to process input from console or file

        Returns:
            tuple : (mode, message or None, filename or None, shift)
    """
    while True:
        mode = input ("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ("e","d"):
            break
        print("Invalid Mode")

    while True:
        choice = input ("Would you like to read from a file (f) or the console (c)? ").lower()
        if choice in ("f","c"):
            break
        print("Invalid Choice")

    message = None
    filename = None

    if choice == "f":
        while True:
            filename = input ("Enter a filename: ")
            if is_file(filename):
                break
            print("Invalid Filename")
    else:
        while True:
            message = input (
                f"What message would you like to {'encrypt' if mode == 'e' else 'decrypt'}: "
                ).upper()
            if message:
                break
            print("Message cannot be empty.")

    while True:
        shift = input ("What is the shift number: ")
        try:
            shift = int (shift) % 26
            break
        except ValueError:
            print("Invalid Shift")

    return mode, message, filename, shift

def main():
    """
        Main program sequence loop.
    """
    welcome()
    while True:
        mode, message, filename, shift = message_or_file()

        if filename:
            result = process_file(filename, mode, shift)
            write_messages(result)
            print("Output written to file results.txt")
        else:
            if mode == "e":
                print(encrypt(message, shift))
            else:
                print(decrypt(message, shift))

        while True:
            again = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
            if again in ("y","n"):
                break
            print("Invalid Input")

        if again == "n":
            print("Thanks for using the program, goodbye!")
            break

if __name__ == "__main__":
        main()
