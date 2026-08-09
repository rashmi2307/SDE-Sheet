# Given two non-empty linked lists linkedList1 and linkedList2 which represent two non-negative integers.

# The digits are stored in reverse order with each node storing one digit.

# Add two numbers and return the sum as a linked list.

# The sum Linked List will be in reverse order as well.

# The Two given Linked Lists represent numbers without any leading zeros, except when the number is zero itself.

# Example 1
# Input: linkedList1 = [5, 4], linkedList2 = [4]
# Output: [9, 4]
# Explanation: linkedList1 = 45, linkedList2 = 4.
# linkedList1 + linkedList2 = 45 + 4 = 49.
# The sum is 49 and when prepare the linked list we reverse the number [9, 4]

# Example 2
# Input: linkedList1 = [4, 5, 6], linkedList2 = [1, 2, 3]
# Output: [5, 7, 9]
# Explanation: linkedList1 = 654, linkedList2 = 321.
# linkedList1 + linkedList2 = 654 + 321 = 975.
# The sum is 975 and when prepare the linked list we reverse the number [5, 7, 9]The sum




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        temp = dummy_node
        carry = 0

        while (l1 is not None or l2 is not None) or carry:
            sum_val = 0
            if l1 is not None:
                sum_val += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_val += l2.val
                l2 = l2.next

            sum_val += carry

            carry = sum_val // 10

            node = ListNode(sum_val % 10)

            temp.next = node

            temp = temp.next

        return dummy_node.next
