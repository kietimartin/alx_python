# !/usr/bin/python3

def multiple_returns(sentence):
    first = sentence[0]
    length = len(sentence)


    if length == 0:
        return ("length: 0 - First character: None")
    
    else:
        return (len(sentence), sentence[0])

