#include <iostream>
#include "TreeNode.cpp"

int findCeil(TreeNode* node, int x) {
    int ceil = -1;
    while(node){
        if(node->data == x){
            ceil = x;
            break;
        }
        else if(node->data < x)
            node = node->right;
        else{
            ceil = node->data;
            node = node->left;
        }
    }
    return ceil;
}