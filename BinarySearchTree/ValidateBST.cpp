#include <iostream>
#include "TreeNode.cpp"
using namespace std;
bool isValidBST(TreeNode* root) {
        vector<int> inOrder;
        // inorder traversal
        traverse(root, inOrder);

        int size = inOrder.size();
        for(int i=1; i<size; i++){
            if(inOrder[i]<=inOrder[i-1])
                return false;
        }

        return true;
    }

    void traverse(TreeNode* root, vector<int> &inOrder){
        if(!root)
            return;
        
        if(root->left)
            traverse(root->left, inOrder);
        inOrder.push_back(root->data);
        if(root->right)
            traverse(root->right, inOrder);
    }