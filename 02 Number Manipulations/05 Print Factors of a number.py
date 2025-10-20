
num = 27     
#Brute Force Solution                         
result = []                         #SC = O(k) where k is number of factors
for i in range(1, num +1):          #TC = O(n)
    if num % i == 0:                #TC = O(1)
        result.append(i)            #TC = O(1)
print(result)

#HERE THE TC = O(n) and other two TC = O(1) will not affect overall TC because O(n) is the highest order term.


#Better Solution 
result_1 = []
for i in range(1, num//2 +1):
    if num % i == 0:
        result_1.append(i)
result_1.append(num)   #Appending the number itself as it is also a factor
print(result_1)


#Optimal Solution
from math import isqrt
num_1 = 36
result_2 = []
for i in range(1, int(isqrt(num_1))+1):
    if num % i == 0:
        result_2.append(i)
        if i != num // i:
            result_2.append(num // i)
print(sorted(result_2))
#TC = O(sqrt(n)) + O(n logn) and SC = O(k) where k is number of factors