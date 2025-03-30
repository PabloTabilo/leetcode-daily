import math
import bisect
class ConvexHull:
    def __init__(self):
        self.lines = []
        self.intersections = []
    
    def add_line(self, m, b):
        while self.lines:
            m_last, b_last = self.lines[-1]
            x = (b - b_last) / (m_last - m) if m_last != m else -math.inf
            if self.intersections and x <= self.intersections[-1]:
                self.lines.pop()
                self.intersections.pop()
            else: 
                break
            
        if not self.lines:
            self.intersections.append(-math.inf)
        else:
            m_last, b_last = self.lines[-1]
            x = (b - b_last) / (m_last - m)
            self.intersections.append(x)
        self.lines.append((m, b))
    
    def query(self, x):
        i = bisect.bisect_right(self.intersections, x) - 1
        m, b = self.lines[i]
        return m * x + b

class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        prefixSumNums = [0] * n
        prefixCost = [0] * n
        k = k
        for i in range(n):
            prefixSumNums[i] = nums[i] + (prefixSumNums[i-1] if (i-1)>=0 else 0)
            prefixCost[i] = cost[i] + (prefixCost[i-1] if (i-1)>=0 else 0)
        
        INF = 10**18
        # dp[i][r], i num of subarray and r : from 0 to r
        dp = [[INF] * (n+1) for _ in range(n+1)]
        for r in range(n):
            dp[1][r] = (prefixSumNums[r] + k*1) * prefixCost[r]
        ans = dp[1][n-1]
        for j in range(2, n+1):
            c = ConvexHull() # the cost is monotonically xd
            cand = j-1
            for r in range(j-1, n):
                while cand <= r:
                    m = -prefixCost[cand-1]
                    b = dp[j-1][cand-1]
                    c.add_line(m, b)
                    cand += 1
                x = prefixSumNums[r] + k * j # this is constant
                best = c.query(x)
                dp[j][r] = x * prefixCost[r] + best
            ans = min(ans, dp[j][n-1])
        return ans