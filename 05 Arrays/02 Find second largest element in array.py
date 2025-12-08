#The solution I came up with
nums = [55,32,97,-55,45,32,88,21]
n = len(nums)
largest = nums[0]
for i in range(0, n):
    if nums[i]>largest:
        largest = nums[i]

nums.remove(largest)

n1 = len(nums)
sec_largest = float("-inf")

for i in range(0,n1):
    if nums[i]>sec_largest:
        sec_largest = nums[i]

print("second largest is", sec_largest)

#Brute Force Solution by sir 
numsbf = [55,32,97,-55,45,32,88,21]
numsbf.sort()
print("second largest is",numsbf[-2])

#Better Solution
nums1 = [55,32,97,-55,45,32,88,21]
n1 = len(nums1)
largest1 = float("-inf")
sec_largest1 = float("-inf")
for i in range(0, n1):
    if nums1[i]>largest1:
        largest1 = nums1[i]

for i in range(0,n1):
    if nums1[i]>sec_largest1 and nums1[i] != largest1: #not equal to largest since the largest value can be repeated again then it will be updated in the largest value
        sec_largest1 =nums1[i]
print("second largest is", sec_largest1)


#Optimal Solution
nums2 = [55,32,97,-55,45,32,88,21]
largest2 = float("-inf")
sec_largest2 = float("-inf")
n2 =len(nums2)
for i in range(0,n2):
    if nums2[i]>largest2:
        sec_largest2 = largest2
        largest2 = nums2[i]
    elif nums2[i]>sec_largest2 and nums2 != largest2:
        sec_largest2 = nums2[i]
print("second largest is", sec_largest2)

