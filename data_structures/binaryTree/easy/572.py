# 572. Subtree of Another Tree

from typing import Optional
from binaryTree.TreeNode import TreeNode
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def validateSameTree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            return (
                validateSameTree(root1.left, root2.left) 
                and 
                validateSameTree(root1.right, root2.right)
            )

        if not root:
            return False
        if root.val == subRoot.val:
            ans = validateSameTree(root, subRoot)
            if ans == True:
                return True
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
'''