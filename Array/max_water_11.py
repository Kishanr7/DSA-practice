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