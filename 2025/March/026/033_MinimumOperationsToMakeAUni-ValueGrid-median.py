class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])
        # get one or two medians
        vals = []
        for i in range(m):
            for j in range(n):
                vals.append(grid[i][j])
        
        vals.sort()
        sz = m*n
        med0 = vals[sz//2]
        med1 = -1
        isPossible0 = True
        isPossible1 = False
        op1 = 1000000000
        if(sz % 2 == 0):
            med1 = vals[sz//2 - 1]
            isPossible1 = True
            op1 = 0
        
        #print(f"med0 = {med0}, med1 = {med1}")
        
        op0 = 0
        
        for v in vals:
            if(med0 != -1 and isPossible0 and (abs(v - med0) == 0 or abs(v - med0) >= x) and abs(v-med0)%x == 0):
                op0 += (abs(v - med0) // x)
            else:
                isPossible0 = False
            
            if(med1 != -1 and isPossible1 and (abs(v - med1) == 0 or abs(v - med1) >= x) and abs(v-med1)%x == 0):
                op1 += (abs(v - med1) // x)
            else:
                isPossible1 = False
            if(not isPossible0 and not isPossible1):
                return -1
        
        return min(op0, op1)
        