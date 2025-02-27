'''
1028. Recover a Tree From Preorder Traversal
Solved
Hard
Topics
Companies
Hint
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 

Example 1:


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 

Constraints:

The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 109
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.i = 0
        def helper(depth):
            if self.i == len(traversal):
                return None
            dashes = 0
            while self.i < len(traversal) and traversal[self.i+dashes] == '-':
                dashes += 1

            if dashes != depth:
                return None
            
            self.i += dashes
            num = 0
            while self.i < len(traversal) and traversal[self.i].isdigit():
                num = num * 10 + int(traversal[self.i])
                self.i += 1

            node = TreeNode(num)
            node.left = helper(depth+1)
            node.right = helper(depth+1)

            return node

        return helper(0)