class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # 1 1 5 5 5 5 5 1 1 >> not valid
        cnt = dict()
        d = -1
        cntd = 0
        n = len(nums)
        for x in nums:
            if(x not in cnt.keys()):
                cnt[x] = 0
            cnt[x]+=1
            if(cntd < cnt[x]):
                cntd = cnt[x]
                d = x
        
        prefixCnt = 0
        for i in range(n-1):
            prefixCnt += (1 if nums[i] == d else 0)
            right = cntd - prefixCnt

            if(prefixCnt >= ((i+1)//2 + 1) and right >= ( (n-1-i) // 2 + 1)):
                return i
        return -1