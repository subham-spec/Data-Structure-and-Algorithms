#include <bits/stdc++.h>
#include "TreeNode.cpp"
using namespace std;

vector<int> topView(TreeNode *root)
    {
        vector<int> ans;
        //Your code here
        if(root == NULL)
            return ans;
            
        map<int, int> mp;
        queue<pair<TreeNode*, int>> q;
        
        q.push({root, 0});
        
        while(!q.empty()){
            TreeNode* front = q.front().first;
            int pos = q.front().second;
            q.pop();
            
            if(mp.find(pos) == mp.end())
                mp[pos] = front->data;
            
            if(front->left)
                q.push({front->left, pos-1});
            if(front->right)
                q.push({front->right, pos+1});
        }
        
        
        for(auto i: mp)
            ans.push_back(i.second);
            
        return ans;
    }