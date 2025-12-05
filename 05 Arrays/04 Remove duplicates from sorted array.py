#Brute Force Solution
nums = [1,1,1,1,2,3,4,4,7,9,9,9,10]
n = len(nums)
freq_map = {}
for i in range(0,n):
    freq_map[nums[i]] = 0

j = 0
for k in freq_map:
    nums[j] = k
    j+=1
print("Count of unique elements",j, "the new updated array is",nums)

#Optimal Solution
nums1 = [1,1,1,1,2,3,4,4,7,9,9,9,10]
n1 = len(nums1)
if n1 == 1:
    print("Count of unique elements",n1, "the new updated array is",nums1)
i1 = 0
j1 = i+1
while n1>j1:
    if nums[j1]!=nums[i1]:
        i1+=1
        nums1[i1], nums[j1] = nums[j1], nums1[i1]