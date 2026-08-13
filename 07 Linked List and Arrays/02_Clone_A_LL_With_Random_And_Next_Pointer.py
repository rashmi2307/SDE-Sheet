# Given the head of a special linked list of n nodes where each node contains an additional pointer called 'random' which can point to any node in the list or null.

# Construct a deep copy of the linked list where,

# n new nodes are created with corresponding values as original linked list.
# The random pointers point to the corresponding new nodes as per their arrangement in the original list.
# Return the head of the newly constructed linked list.

# Note: For custom input, a n x 2 matrix is taken with each row having 2 values:[ val, random_index] where,

# val: an integer representing ListNode.val
# random_index: index of the node (0 - n-1) that the random pointer points to, otherwise -1.

# Example 1
# Input: [[1, -1], [2, 0], [3, 4], [4, 1], [5, 2]]
# Output: 1 2 3 4 5, true
# Explanation: All the nodes in the new list have same corresponding values as original nodes.
# All the random pointers point to their corresponding nodes in the new list.
# 'true' represents that the nodes and references were created new.

# Example 2
# Input: [[5, -1], [3, -1], [2, 1], [1, 1]]
# Output: 5 3 2 1, true
# Explanation: All the nodes in the new list have same corresponding values as original nodes.
# All the random pointers point to their corresponding nodes in the new list.
# 'true' represents that the nodes and references were created new.
# [[5, -1], [3, -1], [2, -1], [1, -1]] will be incorrect, although it has the same values.






"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from typing import Optional
from xml.dom import Node

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        self.insertCopyInBetween(head)
        self.connectRandomPointers(head)
        
        return self.getDeepCopyList(head)

    def insertCopyInBetween(self,head):
        temp = head
        while temp:
            copy = Node(temp.val)

            nextElement = temp.next

            copy.next = nextElement

            temp.next = copy

            temp = nextElement
        

    def connectRandomPointers(self,head):
        temp = head
        while temp:
            copyNode = temp.next

            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None
            temp = temp.next.next


    def getDeepCopyList(self, head):
        temp = head

        dummyNode = Node(-1)
        res = dummyNode

        while temp:
            # Take the copy
            res.next = temp.next
            res = res.next

            # Restore original list
            temp.next = temp.next.next
            temp = temp.next

        return dummyNode.next