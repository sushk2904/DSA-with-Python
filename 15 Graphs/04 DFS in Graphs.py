def dfs(node, result, visited, adj):
    visited[node] =  1
    result.append(node)
    for i in adj[node]:
        if visited[i] == False:
            dfs(i)
    
    print(adj)
dfs(9, [], 1, [[],[2,8],[1,3,4],[2],[2,5],[4,6],[5,7],[6,8],[1,7,9], [8],],)

"""The program isn't working i tried running even fixing it"""
