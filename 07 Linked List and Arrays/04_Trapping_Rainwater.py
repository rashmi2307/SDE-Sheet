# Given an array of non-negative integers, height representing the elevation of ground. Calculate the amount of water that can be trapped after rain.

# Example 1
# Input: height= [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
# Explanation: As seen from the diagram 1+1+2+1+1=6 unit of water can be trapped

# Example 2
# Input: height= [4, 2, 0, 3, 2, 5]
# Output: 9
# Expalanation: 2+4+1+2=9 unit of water can be trapped






# Optimal Solution: Two Pointer Approach
from git import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0
        left = 0
        right = n-1
        max_left, max_right = 0,0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                right -= 1
        return total_water





# Brute Force Approach
class Solution:
    # Function to calculate trapped rainwater using brute force approach
    def trap(self, height):
        n = len(height)
        
        # Variable to store total trapped water
        total_water = 0
        
        # Iterate over each bar in the elevation map
        for i in range(n):
            # Initialize max heights to the left and right of current bar
            max_left = 0
            max_right = 0
            
            # Find maximum height to the left of current bar
            for j in range(i + 1):
                if height[j] > max_left:
                    max_left = height[j]
            
            # Find maximum height to the right of current bar
            for j in range(i, n):
                if height[j] > max_right:
                    max_right = height[j]
            
            # Water trapped on current bar is min of max_left and max_right minus current height
            total_water += min(max_left, max_right) - height[i]
        
        # Return total trapped water
        return total_water