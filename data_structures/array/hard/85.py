# 85. Maximal Rectangle
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        for i in range(0, m):
            for j in range(0, n):
                if i == 0:
                    matrix[i][j] = int(matrix[i][j])
                elif matrix[i][j] == "1":
                    matrix[i][j] = int(matrix[i-1][j])+1
                else:
                    matrix[i][j] = 0

        # print(matrix)
        maxi = 0

        for i in range(0, m):
            for j in range(0, n):
                count = 1
                k = j-1
                while k>=0 and matrix[i][k]>=matrix[i][j]:
                    count += 1
                    k -= 1
                k = j+1
                while k<n and matrix[i][k]>=matrix[i][j]:
                    count += 1
                    k += 1
                maxi = max(maxi, count*matrix[i][j])

        return maxi
    
'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
'''