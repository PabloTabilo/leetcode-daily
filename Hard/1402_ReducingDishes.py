class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        #@cache
        #def fn(i, t):
        #    if(i >= n):
        #        return 0
        #    if(t > n):
        #        return 0
        #    notTake = fn(i+1, t)
        #    take = satisfaction[i] * t + fn(i+1, t+1)
        #    return max(notTake, take)
        dp = [[0]*(n+2) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for t in range(n, 0, -1):
                notTake = dp[i+1][t]
                take = satisfaction[i] * t + dp[i+1][t+1]
                dp[i][t] = max(notTake, take)
        return dp[0][1]