# 438. Find All Anagrams in a String
from collections import Counter
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(s)
        if l<len(p):
            return []

        count_p = Counter()
        for ch in p:
            count_p[ch] += 1
        
        count_s = Counter()
        for j in range(0, len(p)-1):
            count_s[s[j]] += 1

        i, j = 0, len(p)-1
        ans = []
        while j < l:
            count_s[s[j]] += 1
            if count_s == count_p:
                ans.append(i)
            count_s[s[i]] -= 1
            if count_s[s[i]] == 0:
                del count_s[s[i]]
            i += 1
            j += 1
        
        return ans

'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''