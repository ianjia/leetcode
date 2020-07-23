# Binary Search
class Solution1(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """  
        start = 0
        end = len(nums) - 1
            
        while start <= end:
            mid = (end + start) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
            
        return start

# Binary Search (modified)
class Solution2(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        
        if length == 0:
            return 0
        elif nums[length-1] < target:
            return length
        
        start, end = 0, length - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
                
        if nums[start] >= target:
            return start
        else:
            return end

# Iteration
class Solution3(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """              
        for i in range(0, len(nums)):
            if target <= nums[i]:
                return i
                
        return len(nums)