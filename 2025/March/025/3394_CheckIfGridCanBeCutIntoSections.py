class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
        # x-axis: [0,1] [0,2] [2,3] [3,4] >> [0,2] [2,3] [3,4] 
        # y-axis: [0,1] [0,3] [0,4] [2,3] >> [0,4] -> impossible
        x_axis = []
        y_axis = []

        for rect in rectangles:
            x1, y1, x2, y2 = rect
            x_axis.append([x1, x2])
            y_axis.append([y1, y2])
        
        x_axis.sort(key = lambda x : (x[0], x[1]))
        y_axis.sort(key = lambda x : (x[0], x[1]))

        #print(f"x_axis = {x_axis}")
        #print(f"y_axis = {y_axis}")

        cnt = 0
        mx = -1
        for x in x_axis:
            start = x[0]
            end = x[1]

            if(mx == -1):
                mx = end
                continue

            if(mx > start):
                mx = max(mx, end)
                continue
            cnt += 1
            mx = end
        
        if(cnt >= 2): 
            return True
        
        cnt = 0
        mx = -1
        for y in y_axis:
            start = y[0]
            end = y[1]

            if(mx == -1):
                mx = end
                continue

            if(mx > start):
                mx = max(mx, end)
                continue
            cnt += 1
            mx = end
        
        return cnt >= 2
            