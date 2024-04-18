# 200. Number of Islands

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid)-1, len(grid[0])-1

        # Recursive function
        def calc_island(i, j):
            grid[i][j] = "0"
            # Left
            if not j==0 and grid[i][j-1]=="1":
                calc_island(i, j-1)
            # Top
            if not i==0 and grid[i-1][j]=="1":
                calc_island(i-1, j)
            # Right
            if not j==n and grid[i][j+1]=="1":
                calc_island(i, j+1)
            # Bottom
            if not i==m and grid[i+1][j]=="1":
                calc_island(i+1, j)

        counter = 0
        for i in range(0, m+1):
            for j in range(0, n+1):
                if grid[i][j] == "1":
                    counter += 1
                    calc_island(i, j)

        return counter

'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''