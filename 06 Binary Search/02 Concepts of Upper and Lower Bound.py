#Concepts of Upper and Lower Bound
target = 2
nums =[1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(nums)
lb = -1
low, high = 0, n-1
while low<=high:
    mid = (low+high)//2
    if nums[mid]>=target: #This is the most important thing to learn that >= target wali condition use hogi
        lb = mid
        high = mid-1
    else:
        low = mid+1

print(lb)

#Concept of Upper Bound
target1 = 2
nums1 =[1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n1 = len(nums1)
ub = -1
low1, high1 = 0, n1-1
while low1 <= high1:
    mid1 =  (low1+high1)//2
    if nums1[mid1]>target1:
        ub = mid1
        high1 = mid1 -1
    else:
        low1 = mid1+1
print(ub)