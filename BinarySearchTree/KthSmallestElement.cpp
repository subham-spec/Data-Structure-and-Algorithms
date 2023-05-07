#include <iostream>
#include "TreeNode.cpp"
using namespace std;

int kthSmallest(TreeNode* root, int k) {
        vector<int> ans;

        inOrderTraversal(root, ans);

        return ans[k-1];
    }
    void inOrderTraversal(TreeNode* root, vector<int> &ans){
        if(root->left)
            inOrderTraversal(root->left, ans);
        ans.push_back(root->data);
        if(root->right)
            inOrderTraversal(root->right, ans);
    }