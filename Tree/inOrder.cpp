#include <bits/stdc++.h>
#include "treeNode.cpp"
using namespace std;

void inOrderTraversal(TreeNode* root){
    if(root == NULL)
        return;
    stack<TreeNode*> st;
    TreeNode* node = root;
    while(true){
        if(node != NULL){
            st.push(node);
            node = node->left;
        }
        else if(!st.empty()){
            node = st.top();
            st.pop();
            cout<<node->data<<' ';
            node = node->right;
        }
        else
            return;
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
    cout<<"PreOrder Traversal"<<endl;
    inOrderTraversal(root);

    return 0;
}