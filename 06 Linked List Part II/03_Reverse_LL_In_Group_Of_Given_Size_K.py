# Given the head of a singly linked list containing integers, reverse the nodes of the list in groups of k and return the head of the modified list. If the number of nodes is not a multiple of k, then the remaining nodes at the end should be kept as is and not reversed.

# Do not change the values of the nodes, only change the links between nodes.

# Example 1
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output: head -> 2 -> 1 -> 4 -> 3 -> 5
# Explanation: The groups 1 -> 2 and 3 -> 4 were reversed as 2 -> 1 and 4 -> 3.

# Example 2
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 3
# Output: head -> 3 -> 2 -> 1 -> 4 -> 5
# Explanation: The groups 1 -> 2 -> 3 were reversed as 3 -> 2 -> 1.
# Note that 4 -> 5 was not reversed.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = self.getKthNode(groupPrev,k)
            if not kth:
                break

            groupNext = kth.next

            prev = groupNext
            curr = groupPrev.next

            for _ in range (k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
            
        return dummy.next
    
    def getKthNode(self,curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    