from collections import deque
import bisect
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        k = len(queries)
        n = len(grid)
        m = len(grid[0])
        ans = [0] * k
        prefixCnt = [0] * k
        grid = grid
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        qpos = [(v, i) for i, v in enumerate(queries)]
        qpos.sort(key = lambda i : i[0])
        q = deque()
        q.append((0,0))
        for i in range(k):
            v = qpos[i][0]
            # this was calculate
            if((i-1) >= 0 and v == qpos[i-1][0]):
                continue
            notDuplicate = set()
            while q:
                y, x = q.popleft()
                c = grid[y][x]
                if(c == -1):
                    continue
                elif(c >= v):
                    notDuplicate.add((y, x))
                    continue
                prefixCnt[i] += 1
                grid[y][x] = -1
                for mo in directions:
                    ny = y + mo[0]
                    nx = x + mo[1]
                    if(ny < 0 or nx < 0 or ny >= n or nx >= m):
                        continue
                    if(grid[ny][nx] == -1):
                        continue
                    if(grid[ny][nx] >= v):
                        notDuplicate.add((ny, nx))
                    else:
                        q.append((ny, nx))
            for y, x in notDuplicate:
                q.append((y, x))
        for i in range(len(prefixCnt)):
            prefixCnt[i] += prefixCnt[i-1] if (i-1) >= 0 else 0
        for i in range(len(qpos)):
            x = qpos[i]
            ans[x[1]] = prefixCnt[i]
        return ans