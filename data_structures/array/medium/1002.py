# 1002. Find Common Characters

from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        common_arr = [101]*26
        char_arr = ['a','b','c','d','e',
                    'f','g','h','i','j',
                    'k','l','m','n','o',
                    'p','q','r','s','t',
                    'u','v','w','x','y',
                    'z']
        for word in words:
            curr_arr = [0]*26
            for ch in word:
                idx = ord(ch)-97
                curr_arr[idx] += 1
            
            for i in range(26):
                common_arr[i] = min(common_arr[i], curr_arr[i])

        ans = []

        for i in range(26):
            val = common_arr[i]
            if val>0 and val<101:
                for j in range(val):
                    ans.append(char_arr[i])

        return ans

'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''