#from math import factorial
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        num_of_duplicates = 0
        ans = 0
        cnt = dict()
        for r in range(n):
            if nums[r] not in cnt:
                cnt[nums[r]] = 0
            cnt[nums[r]] += 1
            if(cnt[nums[r]] >= 2):
                #oldComb = factorial(cnt[nums[r]]-1) // (factorial(cnt[nums[r]]-1 - 2) * 2)
                #newComb = factorial(cnt[nums[r]]) // (factorial(cnt[nums[r]] - 2)
                oldComb = (cnt[nums[r]]-1) * (cnt[nums[r]]-2) // 2
                newComb = (cnt[nums[r]]) * (cnt[nums[r]]-1) // 2
                num_of_duplicates += (newComb - oldComb)
            while(l <= r and num_of_duplicates >= k):
                ans += (n - r)
                if(cnt[nums[l]] >= 2):
                    #oldComb = factorial(cnt[nums[l]]) // (factorial(cnt[nums[l]] - 2) * 2)
                    #newComb = factorial(cnt[nums[l]]-1) // (factorial(cnt[nums[l]
                    oldComb = (cnt[nums[l]]) * (cnt[nums[l]]-1) // 2
                    newComb = (cnt[nums[l]]-1) * (cnt[nums[l]]-2) // 2
                    num_of_duplicates -= (oldComb - newComb)
                cnt[nums[l]] -= 1
                l += 1
        return ans