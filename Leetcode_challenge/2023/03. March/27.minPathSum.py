'''
64. Minimum Path Sum
Medium

10055

130

Add to List

Share
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = list(accumulate(grid[0]))
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                dp[j] = grid[i][j] + min(dp[j-1] if j > 0 else float('inf'), dp[j])
        return dp[-1]