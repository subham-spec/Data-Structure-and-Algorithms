# 41. First Missing Positive
from typing import List
class Solution:
    @staticmethod
    def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        # print(self)
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                Solution.swap(nums, i, nums[i] - 1)
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
    
if __name__ == "__main__":
    arr = [3,1,4,-1]
    ans = Solution().firstMissingPositive(arr)
    print('The missing number is ',ans)

'''
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
'''