nums = [5,6,7,7,1,9,1111,1,1,5,1,1]
freq_map = {}
for i in range(0, len(nums)): #TC = O(n)
    if nums[i] in freq_map:   #TC = O(1)
       freq_map[nums[i]] +=1  #TC = O(1)
    
    else:
        freq_map[nums[i]] = 1  #TC = O(1)

print(freq_map)
#Overall TC = O(n) + O(1) + O(1) = O(n)
#SC = O(n) since in worst case all elements are distinct and we have to store all elements in dictionary


#Python In-Built FunctionBased Solution
hash_map = {}
n = len(nums)
for i in range(n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) +1 
print(hash_map)
#Overall TC = O(n) and SC = O(n)