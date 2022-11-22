'''
279. Perfect Squares
Medium

8223

359

Add to List

Share
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104
'''
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, int(n**.5) + 1) ]
        q = [n]
        level = 0
        visited = [0]*(n+1)
        visited[n] = 1
        while q:
            new_q = []
            for node in q:
                if node == 0:
                    return level
                for i, sq in enumerate(squares):
                    if node-sq < 0:
                        break
                    if  not visited[node-sq]:
                        new_q.append(node-sq)
                        visited[node-sq] = 1
            level += 1
            q = new_q
        return level
    