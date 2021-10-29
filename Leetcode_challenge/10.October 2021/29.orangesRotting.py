'''
994. Rotting Oranges
Medium

You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.

Accepted
283,028
Submissions
556,957
'''
class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        fresh = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                fresh.add((i, j))
        level = 0
        visited = set()
        def bfs(i, j, level):
            if not fresh: return
            q = [(i, j)]
            visited.add((i, j))
            while q:
                siz = len(q)
                level += 1
                temp = []
                for _ in range(siz):
                    x, y = q.pop()
                    for u, v in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                        if 0<=u<m and 0<=v<n and (u, v) not in visited and grid[u][v] != 0:
                            visited.add((u, v))
                            if grid[u][v] == 1:
                                fresh.remove((u, v))
                                if not fresh:
                                    break
                            temp.append((u, v))
                q = temp             
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    bfs(i, j, level)
                    break
            break
        return level if not fresh else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# grid = [[2,1,1],[0,1,1],[1,0,1]]
# # Output: -1

# grid = [[0,2]]
# # Output: 0

sol = Solution()
print(sol.orangesRotting(grid))
