# 3120. Count the Number of Special Characters I

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_count = [0]*52

        for ch in word:
            if ord(ch)>=ord('a') and ord(ch)<=ord('z'):
                idx = ord(ch)-97
                char_count[idx] += 1
            else:
                idx = ord(ch)-39
                char_count[idx] += 1
        
        count = 0
        for i in range(26):
            if char_count[i] != 0 and char_count[i+26] != 0:
                count += 1
        
        return count

'''
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.

Example 1:
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters in word are 'a', 'b', and 'c'.

Example 2:
Input: word = "abc"
Output: 0
Explanation:
No character in word appears in uppercase.

Example 3:
Input: word = "abBCab"
Output: 1
Explanation:
The only special character in word is 'b'.

Constraints:
1 <= word.length <= 50
word consists of only lowercase and uppercase English letters.
'''