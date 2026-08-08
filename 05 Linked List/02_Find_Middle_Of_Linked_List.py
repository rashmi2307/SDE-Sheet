# Given the head of a singly Linked List, return the middle node of the Linked List.

# If the Linked List has an even number of nodes, return the second middle one.

# Example 1
# Input: head -> 3 -> 8 -> 7 -> 1 -> 3
# Output(value at returned node): 7
# Explanation: There are 5 nodes, so the middle node is the 3rd Node, with value 7.

# Example 2
# Input: head -> 2 -> 9 -> 1 -> 4 -> 0 -> 4
# Output(value at returned node): 4
# Explanation: There are 6 nodes, thus both the 3rd and 4th nodes are middle. So the 2nd middle node (4th Node) is returned with value 4.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        mid = count//2 + 1

        temp = head

        while temp is not None:
            mid = mid - 1
            if mid == 0:
                break
            temp = temp.next
        return temp




class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow, fast = head, head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
        return slow