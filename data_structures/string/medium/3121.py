# 3121. Count the Number of Special Characters II

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_count = [0]*52

        for ch in word:
            if ord(ch)>=ord('a') and ord(ch)<=ord('z'):
                idx = ord(ch)-97
                check_idx = idx+26
                if char_count[check_idx] == 0:
                    char_count[idx] += 1
                else:
                    char_count[idx] = 0
            else:
                idx = ord(ch)-39
                char_count[idx] += 1
        
        count = 0
        for i in range(26):
            if char_count[i] != 0 and char_count[i+26] != 0:
                count += 1
        
        return count

'''
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

 

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

There are no special characters in word.

Example 3:

Input: word = "AbBCab"

Output: 0

Explanation:

There are no special characters in word.

 

Constraints:

1 <= word.length <= 2 * 105
word consists of only lowercase and uppercase English letters.
'''