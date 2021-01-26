'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

 

Constraints:

	The number of the nodes in the list is in the range [0, 104].
	-105 <= Node.val <= 105
	pos is -1 or a valid index in the linked-list.

 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LL:
	def __init__(self):
		self.head = ListNode(None)

	def addAtTail(self, val):
		current = self.head
		if self.head.val is None:
			self.head.val = val
		else:
			while current.next:
				current = current.next
			current.next = ListNode(val)

	def __str__(self):
		ret_str = ''
		current = self.head
		while current:
			ret_str += str(current.val) + ' --> '
			current = current.next
		return ret_str

class Solution:
	def detectCycle(self, head: ListNode) -> ListNode:
		if head is None:
			return head
		visited = set()
		current = head
		while current:
			if current in visited:
				return current
			visited.add(current)
			current = current.next
		return current

ll = LL()
ll.addAtTail(1)
ll.addAtTail(2)
ll.addAtTail(3)
print(ll)
s = Solution()
s.detectCycle(ll)

#try with floyd's algorithm
