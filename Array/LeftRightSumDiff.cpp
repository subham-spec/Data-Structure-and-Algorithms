#include <iostream>
using namespace std;

vector<int> leftRigthDifference(vector<int>& nums) {
        int right = 0,  left = 0 ;
        vector<int> ans;
        
        for(auto i : nums)
            right += i; // 25

        for(int i = 0 ; i<nums.size() ; i++){ 
            right -= nums[i]; // 15
            ans.push_back(abs(left-right));
            left += nums[i];
        }
        
        return ans;
    }