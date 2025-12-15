nums = [9,2,4,1,5,0,6,3,7]
n = len(nums)
for i in range(0,n+1):
    if i not in nums:
        print(i)  

# TC -- O(n^2)  &    SC -- 0(1)


#Better Solution

nums1 = [9,2,4,1,5,0,6,3,7]
n1 = len(nums)
freq = {}
for i in range(0,n1+1):
    freq[i] = 0

for j in nums1:
    freq[j]=1

for k,v in freq.items():
    if v==0:
        print(k)

#Optimal Solution
nums2= [9,2,4,1,5,0,6,3,7]
n2 = len(nums)
total = 0
for i in range(0,n):
    total = nums[i]+total

missing_num = int((n**2 + n)/2) - total
print(missing_num)
