#Bit Manipulation
"""1. Convert to Binary"""
def convert2binary(num:int)->str:

    result = ""
    while num > 0:
        if num % 2 == 1:
            result+="1"
        else:
            result+="0"
        num//2