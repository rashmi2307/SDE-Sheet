# Implement a Last-In-First-Out (LIFO) stack using a single queue. The implemented stack should support the following operations: push, pop, top, and isEmpty.

# Implement the QueueStack class:

# void push(int x): Pushes element x onto the stack.

# int pop(): Removes and returns the top element of the stack.

# int top(): Returns the top element of the stack without removing it.

# boolean isEmpty(): Returns true if the stack is empty, false otherwise.

# Example 1
# Input:
# ["QueueStack", "push", "push", "pop", "top", "isEmpty"]
# [[], [4], [8], [], [], []]
# Output: [null, null, null, 8, 4, false]
# Explanation:
# QueueStack stack = new QueueStack();
# stack.push(4);
# stack.push(8);
# stack.pop(); // returns 8
# stack.top(); // returns 4
# stack.isEmpty(); // returns false

# Example 2
# Input:
# ["QueueStack", "isEmpty"]
# [[]]
# Output:[null, true]
# Explanation:
#  QueueStack stack = new QueueStack();
# stack.isEmpty(); // returns true





from queue import Queue

class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        s = self.q.qsize()
        self.q.put(x)
        for _ in range (s):
            self.q.put(self.q.get())

    def pop(self) -> int:
        n = self.q.queue[0]
        self.q.get()
        return n

    def top(self) -> int:
        return self.q.queue[0]

    def empty(self) -> bool:
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()