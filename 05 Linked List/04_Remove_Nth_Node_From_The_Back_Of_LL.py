# Given the head of a singly linked list and an integer n. Remove the nth node from the back of the linked List and return the head of the modified list. The value of n will always be less than or equal to the number of nodes in the linked list.

# Example 1
# Input: linkedList = 1 -> 2 -> 3 -> 4 -> 5, n = 2
# Output: 1 -> 2 -> 3 -> 5
# Explanation: The 2nd node from the back was the node with value 4.

# Example 2
# Input: linkedList = 5 -> 4 -> 3 -> 2 -> 1, n = 5
# Output: 4 -> 3 -> 2 -> 1
# Explanation: The 5th node from the back is the first node.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None:
            return head

        length = 0
        temp = head

        while temp is not None:
            length += 1
            temp = temp.next
            
        if length == n:
            return head.next

        temp = head
        res = length - n

        while temp:
            res = res - 1
            if res == 0:
                break
            temp = temp.next
        temp.next = temp.next.next

        return head





class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        slow,fast = dummy,dummy

        for _ in range (n+1):
            fast = fast.next
        
        while fast is not None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next