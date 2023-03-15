'''
958. Check Completeness of a Binary Tree
Medium

2908

36

Add to List

Share
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:


Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        level = [root]
        found_none = False
        while level:
            nex = []
            for node in level:
                if found_none:
                    if node.left or node.right:
                        return False
                else:
                    if not node.left:
                        found_none = True
                    else:
                        nex.append(node.left)
                    if not node.right:
                        found_none = True
                    elif found_none:
                        return False
                    else:
                        nex.append(node.right)
            level = nex
        return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def countNodes(node):
            if not node: return 0
            return 1 + countNodes(node.left) + countNodes(node.right)
        n = countNodes(root)
        def dfs(node, i, n):
            if not node: return True
            if i >= n: return False
            return dfs(node.left, 2*i+1, n) and dfs(node.right, 2*i+2, n)
        return dfs(root, 0, n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        none_found = False
        while q:
            node = q.popleft()
            if not node:
                none_found = True
            else:
                if none_found: return False
                q.extend([node.left, node.right])
        return True