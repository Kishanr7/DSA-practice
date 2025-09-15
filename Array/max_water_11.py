# Algorithm Explanation:
# Problem: Given an array of heights, find two lines that together with the x-axis form a container, such that the container holds the most water.
# Approach:
# 1. Use two pointers, one at the start (left) and one at the end (right) of the array.
# 2. Calculate the area formed by the lines at the left and right pointers.
#    - Area = min(height[left], height[right]) * (right - left)
# 3. Update the maximum area found so far.
# 4. Move the pointer at the shorter line inward, hoping to find a taller line and possibly a larger area.
# 5. Repeat until the pointers meet.
# 6. Return the maximum area found.

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        max_area = max(max_area, width * current_height)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))