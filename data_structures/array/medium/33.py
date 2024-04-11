# 33. Search in Rotated Sorted Array
from typing import List
class Solution:
    def findPeak(self, nums):
        l, r = 0, len(nums)-1
        mid = 0

        while l<=r:
            mid = l + (r-l)//2
            if (mid == 0 or nums[mid] >= nums[mid-1]) and (mid == len(nums)-1 or nums[mid] >= nums[mid+1]):
                return mid
            elif nums[mid] < nums[0]:
                r = mid - 1
            else:
                l = mid + 1
    def search(self, nums: List[int], target: int) -> int:
        peak = self.findPeak(nums)
        print(peak)
        def binarySearch(l, r):
            while(l <= r):
                mid = l+(r-l)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            return -1

        if target >= nums[0]:
            return binarySearch(0, peak)
        return binarySearch(peak+1, len(nums)-1)

'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''