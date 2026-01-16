nums = [5,1,3,3,7,1,7]
n =  len(nums)
hmap = {}

for i in range(0,n):
    if nums[i] in hmap:
        hmap[nums[i]]+=1
    else:
        hmap[nums[i]]=1

for k,u in hmap.items():
    if u ==1:
        print("the single number is",  k)
"""for key in hmap:
        if hmap[key]==1:
            return key"""



#Optimized Solution
nums1 = [5,1,3,3,7,1,7]
n1 =  len(nums1)
result = 0
for j in range(0,n1):
    result = result ^ nums1[j]

print("the single number using the xor operator is:", result)

