
#include <iostream>
#include "N_AryTreeNode.cpp"
using namespace std;

int maxDepth(Node* root) {
        if(!root)
            return 0;
        int maxi = 0;

        for(int i=0; i<root->children.size(); i++){
            maxi = max(maxi, maxDepth(root->children[i]));
        }

        return ++maxi;
    }