# Given string str containing just the characters '(', ')', '{', '}', '[' and ']', check if the input string is valid and return true if the string is balanced otherwise return false.

# Example 1
# Input: str = “()[{}()]”
# Output: True
# Explanation: As every open bracket has its corresponding close bracket. Match parentheses are in correct order hence they are balanced.

# Example 2
# Input: str = “[()”
# Output: False
# Explanation: As ‘[‘ does not have ‘]’ hence it is not valid and will return false.




class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()

                if (top == "(" and ch == ")") or \
                (top == "[" and ch == "]") or \
                (top == "{" and ch == "}"):
                    continue
                else:
                    return False

        return not stack