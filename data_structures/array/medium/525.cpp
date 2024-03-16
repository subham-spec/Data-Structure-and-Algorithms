// Contiguous Array
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        map<int, int> mp;
        mp.insert({0, -1});
        int sum = 0, maxi = 0;

        for(int i=0; i<nums.size(); i++) {
            if(nums[i] == 0)
                --sum;
            else
                ++sum;
            if(mp.count(sum))
                maxi = max(maxi, i-mp[sum]);
            else
                mp.insert({sum, i});
        }
        return maxi;
    }
};

/*
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
*/