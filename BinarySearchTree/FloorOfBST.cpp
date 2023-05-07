#include <iostream>
#include "TreeNode.cpp"

int floor(TreeNode* root, int x) {
    // Code here
    int floor = -1;
    
    while(root){
        if(root->data == x)
            return x;
        if(root->data > x)
            root = root->left;
        else{
            floor = root->data;
            root = root->right;
        }
    }
    
    return floor;
}