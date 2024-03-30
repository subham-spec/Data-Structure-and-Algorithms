# 992. Subarrays with K Different Integers
from typing import List
class Solution:
    def countSubarraysWithAtMostKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        i, j = 0, 0
        freq = Counter()

        while j < n:
            freq[nums[j]] += 1
            while i <= j and len(freq) > k:
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
                i += 1
            count += j-i+1
            j += 1

        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        at_most_k = self.countSubarraysWithAtMostKDistinct(nums, k)
        at_most_k_1 = self.countSubarraysWithAtMostKDistinct(nums, k - 1)
        
        return at_most_k - at_most_k_1


'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
'''