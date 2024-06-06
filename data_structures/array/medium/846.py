# 846. Hand of Straights

from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        i = 0
        while i < len(hand):
            if hand[i] is None:
                i += 1
                continue
            start = hand[i]
            count = 0
            j = i
            while j < len(hand) and count < groupSize:
                if hand[j] is None:
                    j += 1
                    continue
                if hand[j] == start + count - 1:
                    j += 1
                    continue
                if hand[j] > start + count:
                    return False
                count += 1
                hand[j] = None
                j += 1
            if count < groupSize:
                return False
        return True

'''
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
'''