'''
52. N-Queens II
Hard

2100

218

Add to List

Share
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9
Accepted
237,862
Submissions
350,437
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        queens, xy_diff, xy_sum = [], [], []
        self.ans = 0
        def backtrack(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n: 
                self.ans += 1
                return
            for q in range(n):
                if q not in queens and p+q not in xy_sum and p-q not in xy_diff:
                    backtrack(queens+[q], xy_diff+[(p-q)], xy_sum+[(p+q)])
        backtrack([], [], [])
        return self.ans
        