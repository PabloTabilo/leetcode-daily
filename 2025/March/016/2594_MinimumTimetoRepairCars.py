import heapq
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1
        r = 100000000000000 # 100 * 10^6 * 10^6
        ans = 0
        while l < r:
            mid = l + (r - l) // 2
            cnt = 0
            #print(f"l = {l}, mid = {mid}, r = {r}")
            for rank in ranks:
                cnt += int(math.sqrt(mid / rank))
            #print(f"cnt = {cnt}, cars = {cars}")
            if(cnt >= cars):
                r = mid
            else:
                l = mid + 1
        return l