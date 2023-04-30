#include <bits/stdc++.h>
#include "treeNode.cpp"
using namespace std;

void levelOrder(TreeNode* root){
    if(root== NULL)
        return;
    queue<TreeNode*> q;
    q.push(root);
    while(!q.empty()){
        TreeNode* node = q.front();
        cout<<node->data<<' ';
        q.pop();
        if(node->left)
            q.push(node->left);
        if(node->right)
            q.push(node->right);
    }
}

int main(){
    //level 0
    TreeNode* root = new TreeNode(1);
    //level 1
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->left->right->left = new TreeNode(6);

    
    root->right = new TreeNode(3);
    root->right->left = new TreeNode(7);
    root->right->right = new TreeNode(8);
    root->right->right->left = new TreeNode(9);
    root->right->right->right = new TreeNode(10);

    //preOrderTraversal
    cout<<"PostOrder Traversal"<<endl;
    levelOrder(root);

    return 0;
}