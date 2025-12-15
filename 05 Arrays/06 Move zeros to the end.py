nums= [1,0,2,4,3,0,0,3,5,1]
n = len(nums)
for i in range(0,n):
    if nums[i]==0:
        nums.pop(i)
        nums.append(0)
print(nums) 
'''Classic problem of python since At i = 1:
nums[1] = 0 → pop it
list becomes: [1, 2, 4, 3, 0, 0, 3, 5, 1, 0]
Notice now the next 0 shifted to index 4,
BUT the loop increments i = 2 → so index 4 is skipped later.
That’s why your output becomes:
[1, 2, 4, 3, 0, 3, 5, 1, 0, 0]'''

#Brute Force 

















#Optimal Soln
nums2 = [1,2,0,4,3,0,0,3,5,1]
n2 = len(nums2)

if n2 ==1:
    print("length is 1 ")
i=0
while i<n2:
    if nums2[i]==0:
        break
    i+=1
if i==n2:
    print("No zeros are there")

j= i+1

while n2>j:
    
    if nums2[j]!= 0:
        nums2[i], nums2[j]=nums2[j], nums2[i]
        i+=1
    j+=1

print(nums2)