"""
1------2
|      |     
|      |
|      |
3------4
\      /
 \    /
    5
 """

n = 5
m = 6
edges = [[1,2], [2,4], [3,4], [1,3], [3,5],[5,4]]
matrix =  [[0 for _ in range(n+1)] for _ in range(n+1)]
print(matrix)

for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1

print(matrix)
#Matrix is quite costly because SC -> O(NxN)


#Now using list based
"""

list = [[],[],[],[],[],[]]

index 0 = []
index 1 = [2,3]
index 2 = [1,4]
index 3 = [4,1,5]
index 4 = [2,3,5]
index 5 = [3,4]

SC -> O(2E)

"""

n = 5
m = 6
edges = [[1,2], [2,4], [3,4], [1,3], [3,5],[5,4]]
#List
lst = [[] for _ in range(n+1)]
#print(lst)
for u,v in edges:
    lst[u].append(v)
    lst[v].append(u)

print(lst)


#Dictionary
n = 5
m = 6
edges = [[1,2], [2,4], [3,4], [1,3], [3,5],[5,4]]
my_dict = {}
for i in range(1, n+1):
    my_dict[i] = []

for u,v in edges:
    my_dict[u].append(v)
    my_dict[v].append(u)
print(my_dict)

