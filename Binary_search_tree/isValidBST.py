'''
 Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

 

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1

'''

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        l = r = True
        if root.left:
            l = (root.left.val<root.val) and self.isValidBST(root.left)
        if root.right:
            r = root.right.val>root.val and self.isValidBST(root.right)
        return l and r

def build_tree(root):
    start = TreeNode(root[0])
    curr = start
    i = 1
    q = deque([start])
    while i<len(root):
        curr = q.popleft()
        if curr:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            q.append(curr.left)
            i += 1
            if i<len(root):
                curr.right = TreeNode(root[i]) if root[i] is not None else None
                q.append(curr.right)
        i += 1
    return start

def print_tree(start):
    res = []
    q = deque([start])
    while any(q):
        curr = q.popleft()
        if curr:
            res.append(curr.val)
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

null = None

root = [2,1,3]
# Output: true

# root = [5,1,4,null,null,3,6]
# # Output: false

root = [5,4,6,null,null,3,7]
# Output: false

start = build_tree(root)
print(print_tree(start))
s = Solution()
print(s.isValidBST(start))
