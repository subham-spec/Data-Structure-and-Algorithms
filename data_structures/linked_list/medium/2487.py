# 2487. Remove Nodes From Linked List

from linked_list.ListNode import ListNode
from typing import Optional
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        head = reverse(head)
        
        curr = head
        while curr and curr.next:
            if curr.next.val < curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        head = reverse(head)
        return head

'''
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
'''