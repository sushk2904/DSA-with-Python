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
x = 0
y = x+1
while y<n1:
    if nums1[y]!=nums1[x]:
        x+=1
        nums1[x], nums1[y] = nums1[y], nums1[x]
    y+=1
print("Count of unique elements",x+1, "the new updated array is",nums1)