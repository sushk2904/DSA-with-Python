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
    print(result)

def convert2decimal(x:str)->int:

    decimal_number = 0
    power = 0
    index = len(x)-1
    while index >= 0:
        num = int(x[index])*(2**power)
        power+=1
        index-=1
        decimal_number+num
    print(decimal_number)



#AND Gate 
'''and gate gives true only if both are true
and false if one is false'''

#OR gate 
'''or gate gives false only if both are false
and true if one is true'''

#XOR Gate 
