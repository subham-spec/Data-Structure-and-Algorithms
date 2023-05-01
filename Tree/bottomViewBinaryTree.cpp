#include <bits/stdc++.h>
#include "TreeNode.cpp"
using namespace std;


vector <int> bottomView(TreeNode *root) {
        // Your Code Here
        vector<int> ans;
        if(root == NULL)
            return ans;
            
        map<int, int> mp;
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        
        while(!q.empty()){
            TreeNode* node = q.front().first;
            int pos = q.front().second;
            q.pop();
            
            mp[pos] = node->data;
            if(node->left)
                q.push({node->left, pos-1});
            if(node->right)
                q.push({node->right, pos+1});
        }
        
        
        for(auto i: mp)
            ans.push_back(i.second);
        
        return ans;
        
    }