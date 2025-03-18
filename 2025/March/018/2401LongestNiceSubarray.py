class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        possible = 0
        sz = 0
        ans = 0
        n = len(nums)
        for r in range(n):
            while((possible & nums[r]) > 0):
                possible ^= nums[l]
                l += 1
            sz = r - l + 1
            ans = max(ans, sz)
            possible ^= nums[r]
        return ans
        