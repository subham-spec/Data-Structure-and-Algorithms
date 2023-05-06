#include <iostream>
#include "N_AryTreeNode.cpp"
using namespace std;

vector<int> preorder(Node* root) {
        vector<int> ans;
        if(!root){
            return ans;
        }
        f(root,ans);
        return ans;
    }
    void f(Node* root , vector<int>&ans){
        ans.push_back(root->val);

        for(int i=0;i<root->children.size();i++){
            f(root->children[i],ans);
        }
    }