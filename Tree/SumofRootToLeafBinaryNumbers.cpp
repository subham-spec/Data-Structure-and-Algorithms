#include <iostream>
#include "treeNode.cpp"
using namespace std;

int sumRootToLeaf(TreeNode* root) {
        return sumOne(root, 0);
    }
    int sumOne(TreeNode* root, int ans){

        if(root == nullptr) return 0;

        int elem = root ->data;
        ans = ans * 2 + elem;

        if(root -> left == NULL && root -> right == NULL){
            return ans;
        }

        int leftSum = sumOne(root -> left, ans);
        int rightSum = sumOne(root -> right, ans);

        return leftSum + rightSum;

    }

/*
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
*/