import heapq
class Solution:
    def putMarbles(self, w: List[int], k: int) -> int:
        n = len(w)
        endSums = [w[i]+w[i+1] for i in range(n-1)]
        mn_heap = []
        heapq.heapify(mn_heap)
        mx_heap = []
        heapq.heapify(mx_heap)
        for es in endSums:
            heapq.heappush(mn_heap, es)
            heapq.heappush(mx_heap, -es)
        k-=1
        mx_sum = w[0] + w[n-1]
        mn_sum = w[0] + w[n-1]
        while k and mn_heap and mx_heap:
            mn_top = heapq.heappop(mn_heap)
            mx_top = heapq.heappop(mx_heap)
            mx_top *= -1
            mx_sum += mx_top
            mn_sum += mn_top
            k -= 1
        return mx_sum - mn_sum
        