#include <iostream>
#include "TreeNode.cpp"
using namespace std;

TreeNode* searchBST(TreeNode* root, int val) {
        if(!root)
            return NULL;
        if(root->data == val)
            return root;
        if(root->data > val)
            return searchBST(root->left, val);
        return searchBST(root->right, val);
    }