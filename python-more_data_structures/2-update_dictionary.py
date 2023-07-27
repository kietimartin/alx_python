#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value 
        #value is replaced

    else:
        a_dictionary[key] = value
        # not available then created
        
    return a_dictionary