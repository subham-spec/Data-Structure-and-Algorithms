# 79. Word Search
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def function_call(i, j, idx):
            if idx == len(word):
                return True
            if i<0 or j<0 or i==m or j==n or board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = ""

            if (function_call(i, j+1, idx+1) or 
                function_call(i+1, j, idx+1) or
                function_call(i-1, j, idx+1) or 
                function_call(i, j-1, idx+1)):
                return True

            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if function_call(i, j, 0):
                        return True
        
        return False

'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''