# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 3 5 6 5 2 7 2 4 2 5 3 1 0 1 8 1 3
# 0 1 2 1 2 3 2 3 2 1 0 1 2 1 2 1 0

#   0
# 1   3
#  2
# 0 1 2 1 0 3 0
# 0 1 2 1 0 1 0

# lca(node1, node2, node3, node4) where depth1 = depth2 = depth3 = depth4 = lowerDepth

#         3 
#    5         1
#      2
#   7     4
#  8 9   10 11

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# 3 5 5 2 7 8 7 9 7 2  4 10  4 11  4  2  5  3  1  3
# 0 1 1 2 3 4 3 4 3 2  3  4  3  4  3  2  1  0  1  0

# depths = [8, 9, 10, 11]
# idx = [5, 7, 11, 13] -> 5-13 -> min depth = 2

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tour = []
        depths = []
        max_depth = -1
        l = -1
        ld = -1
        r = -1
        idx = 0
        def dfs(node, d):
            if(not node):
                return
            nonlocal max_depth, ld, idx, l, r
            max_depth = max(max_depth, d)
            tour.append(node)
            depths.append(d)
            if(max_depth == d):
                if(ld < max_depth):
                    l = idx
                    ld = max_depth
            
            if(max_depth == d):
                r = idx

            idx += 1

            if(not node.left and not node.right):
                return
            
            dfs(node.left, d + 1)
            
            idx += 1
            tour.append(node)
            depths.append(d)
            
            dfs(node.right, d + 1)

            idx += 1
            tour.append(node)
            depths.append(d)

        dfs(root, 0)

        lca_idx = 10000
        curr_depth = 10000
        for i in range(l, r+1):
            if(depths[i] < curr_depth):
                curr_depth = depths[i]
                lca_idx = i
        return tour[lca_idx]
        