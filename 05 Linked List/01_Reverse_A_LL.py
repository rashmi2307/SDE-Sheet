# Given the head of a singly linked list. Reverse the given linked list and return the head of the modified list.

# Example 1
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5
# Output: head -> 5 -> 4 -> 3 -> 2 -> 1
# Explanation: All the links are reversed and the head now points to the last node of the original list.

# Example 2
# Input: head -> 6 -> 8
# Output: head -> 8 -> 6
# Explanation: All the links are reversed and the head now points to the last node of the original list.
# This can be seen like: 6 <- 8 <- head.



# Brute Force Approach:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        temp = head

        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        temp = head

        while temp:
            temp.val = stack.pop()
            temp = temp.next
        
        return head



# Optimal approach is to use three pointers to reverse the linked list in place. This approach uses O(1) extra space.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        temp = head

        while temp:
            front = temp.next

            temp.next = prev

            prev = temp

            temp = front

        return prev