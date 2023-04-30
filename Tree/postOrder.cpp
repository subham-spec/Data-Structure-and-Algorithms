#include <bits/stdc++.h>
#include "treeNode.cpp"
using namespace std;

// preOrder Traversal function
void postOrder(TreeNode* root){
    stack<TreeNode*> s;
    TreeNode* curr = root, *temp;
    while(curr || !s.empty()){
        if(curr){
            s.push(curr);
            curr = curr->left;
        }
        else{
            temp = s.top()->right;
            if(temp == NULL){
                temp = s.top();
                s.pop();
                cout<<temp->data<<' ';
                while(!s.empty() && temp == s.top()->right){
                    temp = s.top();
                    s.pop();
                    cout<<temp->data<<' ';
                }
            }
            else
                curr = temp;
        }
    }
    return;
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
    postOrder(root);

    return 0;
}