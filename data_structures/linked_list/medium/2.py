# Add Two Numbers
from typing import Optional
from linked_list.ListNode import ListNode
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        final_ans = ans
        rem = 0

        while l1 and l2:
            val = l1.val+l2.val+rem
            rem = val//10
            ans.next = ListNode(val%10)
            ans = ans.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            val = l1.val+rem
            rem = val//10
            ans.next = ListNode(val%10)
            ans = ans.next
            l1 = l1.next
        
        while l2:
            val = l2.val+rem
            rem = val//10
            ans.next = ListNode(val%10)
            ans = ans.next
            l2 = l2.next

        if rem:
            ans.next = ListNode(rem)

        return final_ans.next
    
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''