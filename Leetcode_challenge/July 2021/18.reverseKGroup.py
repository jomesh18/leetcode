'''
Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]
 

Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
 

Follow-up: Can you solve the problem in O(1) extra memory space?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#to try
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         dummy = ListNode(0, curr)

#         curr = head

#         stack = []
        
#         prev = dummy
#         count = 1
#         while curr and count<k:
#             count += 1
#             stack.append(curr)
#             curr = curr.next
#         end = curr
#         nex = curr.next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next

def create_ll(head):
    start = ListNode(head[0])
    i = 1
    curr = start
    while i < len(head):
        curr.next = ListNode(head[i])
        i += 1
        curr = curr.next
    return start

def print_ll(start):
    curr = start
    res = []
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

head = [1,2,3,4,5]
k = 2
# Output: [2,1,4,3,5]

start = create_ll(head)
print(print_ll(start))

s = Solution()
ans = s.reverseKGroup(start, k)
print(print_ll(ans))
