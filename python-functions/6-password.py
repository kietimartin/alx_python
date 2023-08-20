#!/usr/bin/python3

def validate_password(password):
    '''Python password validator
    
    Checks for:
    1. length of 8 charachters
    2. one uppercase letter,one lowercase letter & one digit 
    3. Should not have spaces
    
    returns : true if the password passes all tests & false otherwise
    '''
    # Length of password(8 characters or more)
    pass_length = len(password)
    if (pass_length > 8):
        return False
    
    has_upper = any(i.isupper() for i in password)
    has_lower = any(i.islower() for i in password)
    has_digit = any(i.isdigit() for i in password)

    if not (has_digit and has_lower and has_upper == True):
        return False
    
    if ' ' in password:
        return False
    
    return True
