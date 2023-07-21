#!/usr/bin/python3

def validate_password(password):
# This checks if the password is at least 8 characters long
    if len(password) < 8:
        return False

# This checks if the password contains at least one uppercase letter, one lowercase letter, and one digit
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if not (has_uppercase and has_lowercase and has_digit):
        return False

# This checks if the password contains spaces
    if ' ' in password:
        return False

    return True