# 605. Can Place Flowers

from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, j = 0, 0
        l = len(flowerbed)
        k = 1 if l > 1 else 0 

        while j < l and n > 0:
            if flowerbed[i] == 0 and flowerbed[j] == 0 and flowerbed[k] == 0:
                n -= 1
                flowerbed[j] = 1
                j += 2
            else: 
                j += 1
            i = j-1
            if j+1<l: 
                k = j+1 

        return n == 0

'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''