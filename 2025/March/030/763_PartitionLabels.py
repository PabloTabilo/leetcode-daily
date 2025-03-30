class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        lastTime = [-1] * 26
        for i in range(n):
            c = s[i]
            idx = ord(c) - ord('a')
            lastTime[idx] = i
        ans = []
        l = 0
        while(l < n):
            cl = s[l]
            idx_l = ord(cl) - ord('a')
            j = lastTime[idx_l]
            r = l
            while(r < n and r < j):
                cr = s[r]
                idx_r = ord(cr) - ord('a')
                last_r = lastTime[idx_r]
                if(j < last_r):
                    j = last_r
                r += 1
            sz = r - l + 1
            ans.append(sz)
            l = r + 1
        return ans