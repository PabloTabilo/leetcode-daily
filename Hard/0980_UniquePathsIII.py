class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        start = [0,0]
        end = [0,0]
        steps = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    start[0] = i
                    start[1] = j
                if(grid[i][j] == 2):
                    end[0] = i
                    end[1] = j
                if(grid[i][j] == 0):
                    steps += 1
        # m * n * 4 new moves * (constant insert and deletion) * steps (total available)
        @cache
        def dfs(y, x, vis, steps):
            if(y < 0 or y >= m or x < 0 or x >= n):
                return 0
            k = str(y) + "_" + str(x)
            if(k in vis):
                return 0
            if(steps < 0):
                return 0
            if(grid[y][x] == -1):
                return 0
            if(steps == 0 and y == end[0] and x == end[1]):
                return 1
            if(y == end[0] and x == end[1]):
                return 0
            up = dfs(y-1, x, vis + "," + k, steps - 1)
            down = dfs(y+1, x, vis + "," + k, steps - 1)
            left = dfs(y, x-1, vis + "," + k, steps - 1)
            right = dfs(y, x+1, vis + "," + k, steps - 1)
            return up + down + left + right
        steps += 1
        return dfs(start[0], start[1], "", steps)