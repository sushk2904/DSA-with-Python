nums = [55,32,-97,99,3,67]
n = len(nums)
largest = 0
for i in range(0,n):
    if i > largest:
        largest = i
print("largest element in the array is:", largest)

'''this code is wrong since if we take largest =0 and all the numbers are in negative
no value will be stored in the largest'''

nums1 = [55,32,-97,99,3,67]
n1 = len(nums1)
largest1 = nums1[0]
for i in range(0,n1):
    if nums1[i] > largest1:
        largest1 = nums1[i]
print("largest element in the array is:", largest1)

#The python way 
nums2 = [55,32,-97,99,3,67]
n2 = len(nums)
largest2 = nums2[0]
for i in range(0,n2):
    
        largest2 = max(largest2,nums2[i])
print("largest element in the array is:", largest2)


#Unique Learning method
nums3 = [55,32,-97,99,3,67]
n3 = len(nums3)
largest3 = float("-inf") #if we have to write positive infinity just remove "-" sign.
for i in range(0,n3):
    largest3 = max(largest3,nums3[i])
    
print("largest element in the array is:", largest3)