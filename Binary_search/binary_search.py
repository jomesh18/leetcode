'''
Binary Search

Solution
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-9999 <= nums[i], target <= 9999
All the integers in nums are unique.
nums is sorted in an ascending order.
'''

class Solution:
    def search(self, nums: [int], target: int) -> int:
        length = len(nums)
        left, mid, right = 0, length//2, length
        def helper(left, mid, right):
        	

nums = [-1,0,3,5,9,12]
target = 9
# Output: 4

# nums = [-1,0,3,5,9,12]
# target = 2
# Output: -1

s = Solution()
print(s.search(nums, target))
