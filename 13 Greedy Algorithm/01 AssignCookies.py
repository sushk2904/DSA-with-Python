greed = [8,2,1,6,4]
s = [7,2,2,1,4,3]

n = len(greed)
m = len(s)

greed.sort()
s.sort()

left = 0
right = 0
count = 0

while left < n and right < m:
    if greed[left] <= s[right]:
        count += 1
        left +=1
    right+=1

print(count)
