'''
Minimum Falling Path Sum
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
'''
class Solution:
    def minFallingPathSum(self, matrix: [[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0]*n for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        for i in range(1, m):
            for j in range(n):
                dp[i][j] =  dp[i-1][j]
                if j > 0: dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                if j < n-1: dp[i][j] = min(dp[i][j], dp[i-1][j+1])
                dp[i][j] =  dp[i][j] + matrix[i][j]
        # print(dp)
        return min(dp[m-1])

matrix = [[-84,-36,2],[87,-79,10],[42,10,63]]

sol = Solution()
print(sol.minFallingPathSum(matrix))
