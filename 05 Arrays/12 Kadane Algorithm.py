nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
maxm= float("-inf")
for i in range(0,n):
    total=0
    for j in range(i,n):
        total = total + nums[j]
        maxm = max(maxm, total)
print("the maximum subarray sum", maxm)

#Optimal Solution/Kadane's Algo
nums1=[-2,1,-3,4,-1,2,1,-5,4]
n= len(nums)
maxm1 = float("-inf")
total1 = 0
for i in range(0,n):
    total = total + nums[i]
    maxm1 = max(total, maxm1)
    if total < 0:

        total = 0

print("the maximum subarray sum using kadane's algo:", maxm1)