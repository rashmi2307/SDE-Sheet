# Given the heads of two linked lists A and B, containing positive integers. Find the node at which the two linked lists intersect. If they do intersect, return the node at which the intersection begins, otherwise return null.

# The Linked List will not contain any cycles. The linked lists must retain their original structure, given as per the input, after the function returns.

# Note: for custom input, the following parameters are required(your program is not provided with these parameters):

# intersectVal - The value of the node where the intersection occurs. This is -1 if there is no intersected node.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node(-1 if no intersection).
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node(-1 if no intersection).
# listA - The first linked list.
# listB - The second linked list.

# Example 1
# Input: listA: intersectVal = 4, skipA = 3, skipB = 2, head -> 1 -> 2 -> 3 -> 4 -> 5, listB: head -> 7 -> 8 -> 4 -> 5
# Output(value at returned node is displayed): 4
# Explanation: The two lists have nodes with values 4 and 5 as their tails.

# Example 2
# Input: listA: intersectVal = -1, skipA = -1, skipB = -1, head -> 1 -> 2 -> 3, listB: head -> 8 -> 9
# Output(value at returned node is displayed): null
# Explanation: The two lists do not intersect.







# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional
from typing import ListNode
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while headB:
            temp = headA
            while temp:
                if temp == headB:
                    return temp
                temp = temp.next
            headB = headB.next
        return None

    




class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        st = set()
        while headA:
            st.add(headA)
            headA = headA.next
        while headB:
            if headB in st:
                return headB
            headB = headB.next
        return None






class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d1, d2 = headA, headB
        while d1 != d2:
            d1 = headB if d1 is None else d1.next
            d2 = headA if d2 is None else d2.next
        return d1