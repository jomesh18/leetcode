'''
Find K-th Smallest Pair Distance

Solution
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
 

Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
   Hide Hint #1  
Binary search for the answer. How can you check how many pairs have distance <= X?
'''

# naive solution, O(n*n)
class Solution:
    def smallestDistancePair(self, nums: [int], k: int) -> int:
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    ans.append(abs(nums[i]-nums[j]))
        ans.sort()
        return ans[k-1]
        # return sorted([abs(nums[i]-nums[j]) for i in range(len(nums)) for j in range(len(nums)) if i!=j])[k-1]

nums = [1,3,1]
k = 1
# Output: 0
# nums = [1,1,1]
# k = 2
# # Output: 0
nums = [1,6,1]
k = 3
# # Output: 5
nums = [62,100,4]
k = 2
# Expected:58

s = Solution()
print(s.smallestDistancePair(nums, k))
