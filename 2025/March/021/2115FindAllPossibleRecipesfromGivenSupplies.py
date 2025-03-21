from collections import deque 
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # 1. What recipes are independent and what recipes are depend of others
        ans = []
        n : int = len(recipes)
        rd = {i : 0 for i in recipes} # recipes dependencies
        adj = {i : [] for i in recipes+supplies}
        ridx = {recipes[i] : i for i in range(n)}
        # Total operations = 100 * 100 = 10,000 -> low value
        # 100 operations max
        for i in range(n):
            rd[recipes[i]] = len(ingredients[i])
            for ingredient in ingredients[i]:
                if ingredient in adj.keys():
                    adj[ingredient].append(recipes[i]) # recipes[i] <- recipes[j] = ingredient (u)
            
        dq = deque(supplies)
        for recipe, d in rd.items():
            if d == 0:
                dq.append(recipe)
                ans.append(recipe)
        while dq:
            node = dq.popleft()
            for neigh in adj[node]:
                rd[neigh] -= 1
                if(rd[neigh] == 0):
                    dq.append(neigh)
                    ans.append(neigh)
        return ans