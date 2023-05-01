#include <bits/stdc++.h>
#include "TreeNode.cpp"
using namespace std;

vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> ans;
        if(!root)
            return ans;
        // mapping of items
        map<int, map<int, multiset<int>>> mp;
        queue<pair<TreeNode*, pair<int, int>>> q;

        q.push({root, {0, 0}});

        while(!q.empty()){
            pair<TreeNode*, pair<int, int>> front = q.front();
            q.pop();

            TreeNode* front_node = front.first;
            int hd = front.second.first;
            int vd = front.second.second;

            mp[hd][vd].insert(front_node->data);

            if(front_node->left)
                q.push({front_node->left, {hd-1, vd+1}});
            if(front_node->right)
                q.push({front_node->right, {hd+1, vd+1}});
        }
        for(auto i: mp){
            vector<int> curr;
            for (auto j: i.second){
                curr.insert(curr.end(), j.second.begin(), j.second.end());
            }
            ans.push_back(curr);
        }

        return ans;
    }