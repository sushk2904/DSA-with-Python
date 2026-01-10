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
    result = result [::-1]

def convert2decimal(x:str)->int:

    decimal_number = 0
    power = 0
    index = len(x)-1
    while index >= 0:
        num = int(x[index])*(2)



#AND Gate 

#OR gate 