# Given the head of a singly linked list. Return true if a loop exists in the linked list or return false.

# A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer.

# Internally, pos is used to denote the index(0-based) of the node from where the loop starts. Note that pos is not passed as a parameter.

# Example 1
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1
# Output: true
# Explanation: The tail of the linked list connects to the node at 1st index.

# Example 2
# Input: head -> 1 -> 3 -> 7 -> 4, pos = -1
# Output: false
# Explanation: No loop is present in the linked list.







# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional
from typing import ListNode
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        st = set()
        while head:
            if head in st:
                return True
            st.add(head)
            head = head.next
        return False





class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
