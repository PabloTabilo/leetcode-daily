class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])

        lst = []
        for i in range(m):
            for j in range(n):
                if(grid[0][0] % x != grid[i][j] % x):
                    return -1
                lst.append(grid[i][j])
        
        lst.sort()
        sz = m*n
        prefix = [0] * sz
        prefix[0] = lst[0]
        for i in range(1, sz):
            prefix[i] = prefix[i-1] + lst[i]
        
        suffix = [0] * sz
        suffix[sz-1] = lst[sz-1]
        for i in range(sz-2, -1, -1):
            suffix[i] = suffix[i+1] + lst[i]
        
        op = 1000000000
        for i in range(sz):
            left = prefix[i-1] if (i-1) >= 0 else 0
            right = suffix[i+1] if (i+1) < sz else 0

            #print(f"left = {left}, lst[i] = lst[{i}] = {lst[i]}, right = {right}")

            lop = abs(lst[i]*i - left) // x
            rop = abs(lst[i]*(sz-i-1) - right) // x

            #print(f"lop = {lop}, rop = {rop}")

            op = min(op, lop+rop)
        
        return op