# 205. Isomorphic Strings

class Solution:
    def checkboth(s, t):
        chars = dict()
        n = len(s)

        for i in range(n):
            s1 = s[i] in chars
            if s1 == False:
                chars[s[i]] = t[i]
            elif chars[s[i]] != t[i]:
                return False
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = Solution.checkboth(s, t)
        s2 = Solution.checkboth(t, s)

        if s1 == True and s2 == True:
            return True
        return False

'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''