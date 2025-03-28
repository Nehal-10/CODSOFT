# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 18:51:03 2025

@author: Nehal_Jain
"""

import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special):
   
    characters = ''
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    

    if not characters:
        raise ValueError("At least one character type must be selected.")
    

    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    
    length = int(input("Enter the desired length for the password: "))
    

    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    try:
      
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
        print("Your generated password is:", password)
    except ValueError as e:
        print(e)

# Run the program
if __name__ == "__main__":
    main()
