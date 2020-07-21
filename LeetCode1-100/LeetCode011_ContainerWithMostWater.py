# Two-pointers
class Solution1(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater, left, right = 0, 0, len(height) - 1
        
        while left < right:
            # If we try to move the pointer at the longer line inwards, we won't be able to add any extra area because it is limited by the shorter line.
            # In other words, even if the longer line is longer than the shorter line, you only can calculate the area according to the shorter line.
            maxWater = max(maxWater, min(height[left], height[right]) * (right - left)) # min part (find shorter line then multiply it by the length from left to right to get area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return maxWater