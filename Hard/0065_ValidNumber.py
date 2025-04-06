class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {"d" : 1, "s" : 2, "." : 3}, # 0
            {"d" : 1, "." : 6, "e" : 5}, # 1
            {"." : 3, "d" : 1}, # 2
            {"d" : 4}, # 3
            {"d" : 4, "e" : 5}, # 4
            {"d" : 8, "s" : 7}, # 5
            {"d" : 6, "e" : 5}, # 6
            {"d" : 8}, # 7
            {"d" : 8} # 8
        ]

        curr = 0
        for c in s:
            if c.lower() == 'e':
                transition = "e"
            elif c in string.digits:
                transition = "d"
            elif c in ["+", "-"]:
                transition = "s"
            elif c == ".":
                transition = "."
            else:
                return False
            if transition not in states[curr]:
                return False
            curr = states[curr][transition]
        # Finish states
        if curr not in [1, 4, 6, 8]:
            return False
        return True 
            
        