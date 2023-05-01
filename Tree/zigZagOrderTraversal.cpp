#include <bits/stdc++.h>
using namespace std;

struct TreeNode{
    int data;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int data){
        this->data = data;
    }
};

vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
    vector<vector<int>> ans;
    if(root == NULL)
        return ans;
    queue<TreeNode*> q;

    q.push(root);
    bool flag = true;
    while(!q.empty()){
        vector<int> curr;
        int l = q.size();
        for(int i=0; i<l; i++){
            TreeNode* node = q.front();
            q.pop();
            if(node->left != NULL)
                q.push(node->left);
            if(node->right != NULL)
                q.push(node->right);
            curr.push_back(node->data);
        }

        if(flag)
            ans.push_back(curr);
        else{
            reverse(curr.begin(), curr.end());
            ans.push_back(curr);
        }           
        flag = !flag;
    }
    return ans;
}