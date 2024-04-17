# 988. Smallest String Starting From Leaf
from binaryTree.TreeNode import TreeNode
from typing import Optional

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        s = str()
        def findSmallest(curr, root):
            nonlocal s
            if not root.left and not root.right:
                ch = chr(root.val + 97)
                curr = ch + curr
                if not s:
                    s = curr
                elif curr < s:
                    s = curr
                return
            ch = chr(root.val + 97)
            if root.left:
                findSmallest(ch+curr, root.left)
            if root.right:
                findSmallest(ch+curr, root.right)

        findSmallest('', root)
        return s

'''
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

 

Example 1:


Input: root = [0,1,2,3,4,3,4]
Output: "dba"
Example 2:


Input: root = [25,1,3,1,3,0,2]
Output: "adz"
Example 3:


Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"
 

Constraints:

The number of nodes in the tree is in the range [1, 8500].
0 <= Node.val <= 25
'''