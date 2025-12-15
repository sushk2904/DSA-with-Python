nums = [5,9,1,2,4,15,6,3]
n = len(nums)
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i]+nums[j] == 19:
            print(i,j)


#Optimal Solution
nums1 = [5,9,1,2,4,15,6,3]
n1 = len(nums)
freq= {}
remaining = 0
target =19
for i in range(0,n1):
    remaining = target - nums1[i]
    if remaining in freq:
        print(freq[remaining], i)
    freq[nums1[i]]= i
   
        
