#include <bits/stdc++.h>
#include "treeNode.cpp"
using namespace std;

// preOrder Traversal function
void preOrder(TreeNode* root){
    stack<TreeNode*> s;
    s.push(root);

    while(!s.empty()) {
        TreeNode* node = s.top();
        s.pop();
        cout << node->data << " ";

        if(node->right) s.push(node->right);
        if(node->left) s.push(node->left);
    }
} 



int main(){
    //level 0
    TreeNode* root = new TreeNode(1);
    //level 1
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);

    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    root->left->right->left = new TreeNode(6);

    root->right->left = new TreeNode(7);
    root->right->right = new TreeNode(8);

    root->right->right->left = new TreeNode(9);
    root->right->right->right = new TreeNode(10);

    //preOrderTraversal
    cout<<"PreOrder Traversal"<<endl;
    preOrder(root);

    return 0;
}
