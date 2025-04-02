class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        @cache
        def fn(y, x1, x2):
            if(y >= n):
                return 0
            mx = 0
            for x1n in range(x1-1, x1+2):
                for x2n in range(x2-1, x2+2):
                    if(x1n < 0 or x2n < 0 or x1n >= m or x2n >= m or x1n == x2n):
                        continue
                    local = grid[y][x1n] + grid[y][x2n]
                    nxt = fn(y+1, x1n, x2n)
                    mx = max(mx, local + nxt)
            return mx
        ans = grid[0][0] + grid[0][m-1]
        return ans + fn(1,0,m-1) 