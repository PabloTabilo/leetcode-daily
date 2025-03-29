import math
class Solution: 
    def maximumScore(self, nums: List[int], k: int) -> int:
        # primeScore, pos
        # Original:      [19,12,14,6,10,18]
        # dominantLeft:  [19,12,12,12,12,12]
        # fromLeft:      [ 0, 1, 2, 3, 4, 5]
        # dominantRight:  [12,12,14,6,10,18]
        # fromRight:      [5, 4, 3, 2, 1, 0]
        # (18, 1)
        # (19, 1)
        # (12, 5 + 5 + 1)
        # (14, 3 + 1)
        # (6, 2 + 1)
        # (10, 1 + 1)
        # k times
        # 0,0: [19] 
        # 0,1: [19 12] [12]
        # 0,2: [19 12 14] [12 14] [14]
        # 0,3: [19 12 14 6] [12 14 6] [14 6] [6]
        # 0,4: [19 12 14 6 10] [12 14 6 10] [14 6 10] [6 10] [10]
        # 0,5: [19 12 14 6 10 18] [12 14 6 10 18] [14 6 10 18] [6 10 18] [10 18] [18]
        n = len(nums)
        cntPrimes = [0] * n
        for i in range(n):
            mx = nums[i]
            for j in range(2, int(math.sqrt(mx)) + 1):
                if(mx % j == 0):
                    cntPrimes[i] += 1
                    while(mx % j == 0):
                        mx /= j
            if(mx >= 2):
                cntPrimes[i] += 1
        
        dominantLeft = [-1] * n
        stk = []
        for i in range(n):
            while stk and cntPrimes[stk[-1]] < cntPrimes[i]:
                stk.pop()
            dominantLeft[i] = stk[-1] if stk else -1
            stk.append(i)

        dominantRight = [n] * n
        stk = []
        for i in range(n-1, -1, -1):
            while stk and cntPrimes[stk[-1]] <= cntPrimes[i]:
                stk.pop()
            dominantRight[i] = stk[-1] if stk else n
            stk.append(i)
        
        h = [ (-nums[i], (i - dominantLeft[i] )*(dominantRight[i] - i) ) for i in range(n)]
        heapify(h)
        #print(h)
        ans = 1
        MOD = 10**9 + 7
        def mod_expo(base, expo, mod):
            # 2^6 = 64
            # 1st
            # b = 2 * 2
            # e = 6 / 2 = 3
            # 2nd
            # a = 1 * 4
            # e = 2
            # b = 4 * 4
            # e = 1
            # 3th
            # a = 4 * 16
            # e = 0
            # b = 16 * 16
            ans = 1
            while expo:
                if(expo % 2 == 1):
                    ans = ((ans % mod) * (base % mod)) % mod
                base = ((base % mod) * (base % mod)) % mod
                expo //= 2
            return ans
        while k > 0 and h:
            #print(f"k = {k}, h = {h}")
            v, op = heappop(h)
            v *= -1
            times = min(k, op)
            #print(f"v, op = {v}, {op}")
            #print(f"times = {times}")
            ans = ((ans % MOD) * (mod_expo(base=v, expo=times, mod=MOD) % MOD)) % MOD
            k -= times
            #print(f"k = {k}")
        return ans
