# 409. Longest Palindrome

from typing import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter([val for val in s])
        ans = 0
        have_odd = False

        for key, val in count.items():
            ans += val
            if val&1:
                ans -= 1
                have_odd = True

        if have_odd:
            ans += 1
        return ans

'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''