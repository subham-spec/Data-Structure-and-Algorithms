# 131. Palindrome Partitioning
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def findPalindromes(curr, idx, l):
            if idx == l:
                if curr not in ans:
                    ans.append(curr[:])

            for i in range(idx, l):
                substr = s[idx:i+1]
                if substr == substr[::-1]:
                    curr.append(substr)
                    findPalindromes(curr, i+1, l)
                    curr.pop()

        l = len(s)
        findPalindromes([], 0, l)
        return ans

'''
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''