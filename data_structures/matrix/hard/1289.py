# 1289. Minimum Falling Path Sum II

from typing import List
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def minis(row):
            couples = []
            for val, idx in row:
                if len(couples) < 2:
                    couples.append((val, idx))
                elif couples[1][0] > val:
                    couples.pop()
                    couples.append((val, idx))
                couples.sort()

            return couples

        first_row = [(val, idx) for idx, val in enumerate(grid[0])]
        dp = minis(first_row)

        for row in range(1, n):
            next_dp = []
            for col in range(n):
                val = grid[row][col]
                mini = float("inf")

                for pval, pcol in dp:
                    if col != pcol:
                        mini = min(mini, val+pval)
                next_dp.append((mini, col))
                next_dp = minis(next_dp)
            dp = next_dp

        return min([val for val, idx in dp])

'''
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

 

Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.
Example 2:

Input: grid = [[7]]
Output: 7
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99
'''