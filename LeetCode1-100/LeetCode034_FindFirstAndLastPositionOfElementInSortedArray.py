# Binary Search (modified)
class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        
        return [self.getFirstPos(nums, target), self.getLastPos(nums, target)]
    
    def getFirstPos(self, nums, target):
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
        
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        
        return -1
    
    def getLastPos(self, nums, target):
        start, end = 0, len(nums) - 1   
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
        
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        
        return -1