#include <iostream>
#include "TreeNode.cpp"
using namespace std;

TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(root == NULL)
            return new TreeNode(val);
        insert(root, val, root, 'l');

        return root;
    }
    void insert(TreeNode* root, int val, TreeNode* parent, char ch){
        if(root == NULL){
            if(ch == 'l')
                parent->left = new TreeNode(val);
            else
                parent->right = new TreeNode(val);
            return;
        }
        if(root->data < val)
            insert(root->right, val, root, 'r');
        else
            insert(root->left, val, root, 'l');
    }