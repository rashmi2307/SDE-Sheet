# Implement a First-In-First-Out (FIFO) queue using two stacks. The implemented queue should support the following operations: push, pop, peek, and isEmpty.

# Implement the StackQueue class:

# void push(int x): Adds element x to the end of the queue.

# int pop(): Removes and returns the front element of the queue.

# int peek(): Returns the front element of the queue without removing it.

# boolean isEmpty(): Returns true if the queue is empty, false otherwise.

# Example 1
# Input:
# ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]
# [[], [4], [8], [], [], []]
# Output:[null, null, null, 4, 8, false]
# Explanation:
# StackQueue queue = new StackQueue();
# queue.push(4);
# queue.push(8);
# queue.pop(); // returns 4
# queue.peek(); // returns 8
# queue.isEmpty(); // returns false

# Example 2
# Input:
# ["StackQueue", "isEmpty"]
# [[]]
# Output: [null, true]
# Explanation:
# StackQueue queue = new StackQueue();
# queue.isEmpty(); // returns true






class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self) -> int:
        if not self.st1:
            print("Stack is empty")
            return -1
        top_element = self.st1.pop()
        return top_element

    def peek(self) -> int:
        if not self.st1:
            print("Stack is empty")
            return -1
        return self.st1[-1]

    def empty(self) -> bool:
        return not self.st1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()