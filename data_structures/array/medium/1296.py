# 1296. Divide Array in Sets of K Consecutive Numbers

from typing import List, Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        num_count = Counter(nums)
        sorted_keys = sorted(num_count.keys())
        
        for num in sorted_keys:
            if num_count[num] > 0:
                count = num_count[num]
                for i in range(num, num + k):
                    if num_count[i] < count:
                        return False
                    num_count[i] -= count
        
        return True

'''
Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 109
'''