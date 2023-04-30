#include <bits/stdc++.h>
using namespace std;
struct TreeNode{
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
    TreeNode(int data){
        this->data = data;
        right = NULL;
        left = NULL;
    }
};
