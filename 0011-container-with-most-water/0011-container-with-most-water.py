class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            width = right - left
            if height[left] < height[right]:
                max_water = max(max_water, width * height[left])
                left += 1
            else:
                max_water = max(max_water, width * height[right])
                right -= 1
                
        return max_water