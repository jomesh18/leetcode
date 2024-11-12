'''
3097. Shortest Subarray With OR at Least K II
Medium

680

64

Add to List

Share
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

 

Example 1:

Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:

Input: nums = [2,1,8], k = 10

Output: 3

Explanation:

The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:

Input: nums = [1,2], k = 0

Output: 1

Explanation:

The subarray [1] has OR value of 1. Hence, we return 1.

 

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 109
0 <= k <= 109
'''
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits = [0]*30
        l = 0
        ans = len(nums) + 1
        def find_num(bits):
            curr = 0
            for i in range(len(bits)-1, -1, -1):
                curr <<= 1
                if bits[i]:
                    curr |= 1
            return curr
        
        for r in range(len(nums)):
            curr = nums[r]
            i = 0
            while curr:
                bits[i] += (curr & 1)
                curr >>= 1
                i += 1
            while l <= r and find_num(bits) >= k:
                ans = min(ans, r-l+1)
                curr = nums[l]
                j = 0
                while curr:
                    bits[j] -= (curr & 1)
                    curr >>= 1
                    j += 1
                l += 1
        return ans if ans != (len(nums)+1) else -1