# 1248. Count Number of Nice Subarrays

from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        key_fixes = defaultdict(int)

        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i]&1:
                count += 1
            nums[i] = count

        max_val = nums[-1]
        # print(nums)
        key_fixes[0] = 1
        for val in nums:
            key_fixes[val] += 1
        # print(key_fixes)
        ans = 0

        for prime in range(k, max_val+1):
            # print(prime)
            ans += (key_fixes[prime]*key_fixes[prime-k])

        return ans

'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
'''