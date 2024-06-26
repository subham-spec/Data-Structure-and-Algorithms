# 3114. Latest Time You Can Obtain After Replacing Characters

class Solution:
    def findLatestTime(self, s: str) -> str:
        def createSecondValue(val):
            if val[0] != '?' and val[1] != '?':
                return val
            elif val[0] == '?' and val[1] == '?':
                return "59"
            elif val[0] == '?' and val[1] != '?':
                return '5'+val[1]
            else:
                return val[0]+'9'

        def createFirstValue(val):
            if val[0] == '?' and val[1] == '?':
                return "11"
            elif val[0]=='?' and val[1]!='?' and (val[1]=='0' or val[1]=='1'):
                return '1'+val[1]
            elif val[0]=='?' and val[1]!='?':
                return '0'+val[1]
            elif val[0]!='?' and val[0]=='0' and val[1]=='?':
                return val[0]+'9'
            elif val[0]!='?' and val[1]=='?':
                return val[0]+'1'
            else:
                return val
        
        # Creating MM
        MM = createSecondValue(s[3:])
        # Creating HH
        HH = createFirstValue(s[:2])

        return HH+':'+MM

'''
You are given a string s representing a 12-hour format time where some of the digits (possibly none) are replaced with a "?".

12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59. The earliest 12-hour time is 00:00, and the latest is 11:59.

You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is a valid 12-hour format time and is the latest possible.

Return the resulting string.

 

Example 1:

Input: s = "1?:?4"

Output: "11:54"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "11:54".

Example 2:

Input: s = "0?:5?"

Output: "09:59"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "09:59".

 

Constraints:

s.length == 5
s[2] is equal to the character ":".
All characters except s[2] are digits or "?" characters.
The input is generated such that there is at least one time between "00:00" and "11:59" that you can obtain after replacing the "?" characters.
'''