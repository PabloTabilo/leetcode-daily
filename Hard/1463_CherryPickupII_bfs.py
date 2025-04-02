from collections import deque
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        tot = grid[0][0] + grid[0][m-1]
        x1, x2, = 0, m-1
        d = deque()
        d.append((0, x1, x2))
        ans = 0
        states = {i : {(-1,-1) : -1} for i in range(n)}
        states[0][(x1,x2)] = tot
        while d:
            y, x1, x2 = d.popleft()
            tot = states[y][(x1,x2)]
            y += 1
            if(y >= n):
                continue
            l1 = grid[y][x1-1] if (x1-1) >= 0 else 0
            d1 = grid[y][x1]
            r1 = grid[y][x1+1] if (x1+1) < m else 0

            l2 = grid[y][x2-1] if (x2-1) >= 0 else 0
            d2 = grid[y][x2]
            r2 = grid[y][x2+1] if (x2+1) < m else 0

            for add1, x1n in [(l1, x1-1), (d1, x1), (r1, x1+1)]:
                for add2, x2n in [(l2, x2-1), (d2, x2), (r2, x2+1)]:
                    if(x1n < 0 or x2n < 0 or x1n >= m or x2n >= m or x1n == x2n):
                        continue
                    x = (x1n, x2n)
                    v = tot+add1+add2
                    if y in states and x in states[y]:
                        if(states[y][x] < v):
                            states[y][x] = v
                        continue
                    d.append((y, x1n, x2n))
                    states[y][x] = v
        ans = 0
        for k, v in states[n-1].items():
            ans = max(ans, v)
        return ans