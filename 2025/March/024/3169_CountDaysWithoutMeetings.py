class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x : (x[0], x[1]))
        cnt = 0
        INF = 10000
        mn = INF
        mx = 0
        #print(meetings)
        for meet in meetings:
            start = meet[0]
            end = meet[1]
            if(mn == INF):
                mn = start
                mx = end
            elif mx >= start:
                mx = max(mx, end)
            else:
                sz = mx - mn + 1
                cnt += sz
                mn = start
                mx = end
            #print(f"mn = {mn}, mx = {mx}")
        cnt += (mx - mn + 1)
        return days - cnt