# 15. 3 Sum

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4, -1, -1, 0 , 1 , 2
        nums.sort(key=None, reverse=False)

        ans = []
        l = len(nums)-3

        for i in range(0, l+1):
            if nums[i] > 0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j<k:
                i_sum = nums[i]+nums[j]+nums[k]
                if i_sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    curr = j
                    while(j<k and nums[curr]==nums[j]):
                        j += 1
                    curr = k
                    while(k>j and nums[curr]==nums[k]):
                        k -= 1
                elif i_sum < 0:
                    j += 1
                else:
                    k -= 1
        return ans

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''