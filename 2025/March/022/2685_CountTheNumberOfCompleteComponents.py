from collections import Counter
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        components = [-1] * n
        adj = {i : [] for i in range(n)}
        for e in edges:
            u : int = e[0]
            v : int = e[1]
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node : int, c : int):
            components[node] = c
            for neigh in adj[node]:
                if(components[neigh] == -1):
                    dfs(neigh, c)
        
        c = 1
        isComplete = dict()
        for i in range(n):
            if(components[i] == -1):
                dfs(i, c)
                isComplete[c] = 0
                c += 1
        #print(f"components = {components}")
        cnt = Counter(components)
        #print(cnt)
        ans = 0
        for node in range(n):
            if(len(adj[node]) == (cnt[components[node]]-1)):
                isComplete[components[node]] += 1
        
        for k, v in cnt.items():
            if(isComplete[k] == v):
                ans += 1
        return ans
        