'''
2962. Count Subarrays Where Max Element Appears at Least K Times
Medium

1112

54

Add to List

Share
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        max_ = max(nums)
        n = len(nums)
        l = 0
        count = Counter()
        for i, num in enumerate(nums):
            count[num] += 1
            while count[max_] >= k:
                ans += (n-i)
                count[nums[l]] -= 1
                l += 1
        return ans
