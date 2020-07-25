# Array (not follow up)
class Solution1(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i+1]:
                return i
            
        return len(nums) - 1

# Binary Search
class Solution2(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2 # same as "(start + end) // 2" but prevents overflow if start and end are huge numbers.
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid + 1
                
        return start