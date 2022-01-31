'''
Maximal Square

Solution
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
'''
class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        def helper(i, j):
            if i == m or j == n: return 0
            if dp[i][j] >= 0: return dp[i][j]
            ans = min(helper(i, j+1), helper(i+1, j), helper(i+1, j+1)) + 1 if matrix[i][j] == "1" else 0
            dp[i][j] = ans
            return ans
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    ans = max(ans, helper(i, j))
        return ans*ans


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4

# matrix = [["1", "1", "1"], ["1", "1", "0"]]
# Output: 4

sol = Solution()
print(sol.maximalSquare(matrix))
