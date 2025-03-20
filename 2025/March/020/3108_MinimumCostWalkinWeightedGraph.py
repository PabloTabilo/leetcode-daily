class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        root = [-1] * n
        rank = [0] * n
        val = [-1] * n
        
        def find(x):
            while(root[x] != -1):
                x = root[x]
            return x
        
        def union(u, v, w):
            r1 = find(u)
            r2 = find(v)
            if(r1 != r2):
                if(rank[r1] < rank[r2]):
                    r1, r2 = r2, r1
                
                rank[r1] += 1 + rank[r2]
                root[r2] = r1
            
            if(val[r1] == -1):
                val[r1] = w
            else:
                val[r1] = val[r1] & w
            
            if(val[r2] != -1):
                val[r1] = val[r1] & val[r2]

        for e in edges:
            u : int = e[0]
            v : int = e[1]
            w : int = e[2]
            union(u, v, w)

        ans = []
        for q in query:
            u : int = q[0]
            v : int = q[1]

            r1 = find(u)
            r2 = find(v)

            if(r1 == r2):
                ans.append(val[r1])
            else:
                ans.append(-1)
        return ans