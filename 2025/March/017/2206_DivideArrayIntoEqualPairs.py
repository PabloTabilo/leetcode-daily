class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n : int = len(nums) // 2
        cnt = Counter(nums)
        for n,v in cnt.items():
            if(v % 2 == 1):
                return False
        return True
        