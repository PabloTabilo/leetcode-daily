class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # simulation
        n = len(nums)
        prefix = 0
        ope = 0
        for i in range(n):
            if(i < n-2 and nums[i] == 0):
                nums[i] = 1 - nums[i]
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
                ope += 1
            prefix += nums[i]
        return ope if prefix == n else -1