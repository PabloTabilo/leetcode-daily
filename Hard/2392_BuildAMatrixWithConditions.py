from collections import deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def isCycle(cond):
            adj = {i : [] for i in range(k+1)}
            indegree = [0] * (k+1)
            cond = set(tuple(x) for x in cond)
            # to the right / down >> x[0] -> x[1]
            for x in cond:
                adj[x[0]].append(x[1])
                indegree[x[1]] += 1

            dq = deque()
            for i in range(1, k+1):
                if(indegree[i] == 0):
                    dq.append(i)
            
            if(len(dq) == 0):
                return []
            sortLst = []
            while dq:
                node = dq.popleft()
                sortLst.append(node)
                for neigh in adj[node]:
                    indegree[neigh] -= 1
                    if(indegree[neigh] == 0):
                        dq.append(neigh)

            for i in range(1, k+1):
                if(indegree[i] != 0):
                    return []
            return sortLst
        
        sortRow = isCycle(rowConditions)
        sortCol = isCycle(colConditions)

        if(sortRow == [] or sortCol == []):
            return []
        positions = {i : [0,0] for i in range(k+1)}
        for i, v in enumerate(sortRow):
            positions[v][0] = i
        for i, v in enumerate(sortCol):
            positions[v][1] = i
        ans = [[0]*k for i in range(k)]

        for i in range(k+1):
            y, x = positions[i]
            ans[y][x] = i
    
        return ans
        