
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include "treeNode.cpp"
using namespace std;


vector<int> distanceK(TreeNode* root, TreeNode* target, int k){
        vector<int> ans;
        if(root == NULL)
            return ans;

        // marking the parents for the nodes below
        map<TreeNode*, TreeNode*> mp;
        queue<TreeNode*> q;
        q.push(root);
        mp[root] = NULL;

        while(!q.empty()){
            TreeNode* node = q.front();
            q.pop();

            if(node->left){
                q.push(node->left);
                mp[node->left] = node;
            }
            if(node->right){
                q.push(node->right);
                mp[node->right] = node;
            }
        }

        // traversing the k distance
        queue<TreeNode*> p;
        p.push(target);
        int count = k;
        // set to store that the node are visited or not
        set<TreeNode*> s;
        // counter for k
        while(!p.empty() && count > 0){
            int size = p.size();
            for(int i=0; i<size; i++){
                TreeNode* node = p.front();
                cout<<node->data;
                s.insert(node);
                p.pop();
                if(node->left && !s.count(node->left))
                    p.push(node->left);
                if(node->right && !s.count(node->right))
                    p.push(node->right);
                if(mp[node] && !s.count(mp[node]))
                    p.push(mp[node]);
            }
            cout<<endl;
            --count;
        }

        while(!p.empty()){
            int val = p.front()->data;
            ans.push_back(val);
            p.pop();
        }
        return ans;
    }

/*
All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
*/