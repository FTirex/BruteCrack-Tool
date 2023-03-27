import requests
import hashlib
import base64
import itertools

# Define character set for brute-force attack
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

# Define hash cracking function
def hash_cracking():
    # Get user input for password length
    password_length = int(input("Enter password length: "))

    # Get user input for password hashes
    print("Select an option:")
    print("1. Enter hashes manually")
    print("2. Import hashes from a file")
    hash_input_option = input("Option: ")

    if hash_input_option == '1':
        hash_input = input('Enter a comma-separated list of password hashes: ')
        password_hashes = hash_input.split(',')
    elif hash_input_option == '2':
        file_path = input("Enter the path of the file containing the password hashes: ")
        with open(file_path, 'r') as f:
            password_hashes = [line.strip() for line in f]
    else:
        print("Invalid option selected")
        return
    
    # Generate all possible password guesses
    password_guesses = itertools.product(characters, repeat=password_length)

    # Hash password guesses and compare to original hashes
    for password_guess in password_guesses:
        password_guess_str = ''.join(password_guess)

        # Try cracking MD5 hashed passwords
        md5_hash = hashlib.md5(password_guess_str.encode('utf-8')).hexdigest()
        if md5_hash in password_hashes:
            print(f'MD5 Password cracked: {password_guess_str}')

        # Try cracking SHA-1 hashed passwords
        sha1_hash = hashlib.sha1(password_guess_str.encode('utf-8')).hexdigest()
        if sha1_hash in password_hashes:
            print(f'SHA-1 Password cracked: {password_guess_str}')

        # Try cracking SHA-256 hashed passwords
        sha256_hash = hashlib.sha256(password_guess_str.encode('utf-8')).hexdigest()
        if sha256_hash in password_hashes:
            print(f'SHA-256 Password cracked: {password_guess_str}')

        # Try cracking SHA-512 hashed passwords
        sha512_hash = hashlib.sha512(password_guess_str.encode('utf-8')).hexdigest()
        if sha512_hash in password_hashes:
            print(f'SHA-512 Password cracked: {password_guess_str}')

        # Try cracking Base64 encoded passwords
        base64_encoded_password = base64.b64encode(password_guess_str.encode('utf-8')).decode('utf-8')
        if base64_encoded_password in password_hashes:
            print(f'Base64 Password cracked: {password_guess_str}')

# Call the hash cracking function to start the program
hash_cracking()
