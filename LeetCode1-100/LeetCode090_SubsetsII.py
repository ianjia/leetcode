# Backtracking
class Solution1(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        if len(nums) == 0:
            return res
        
        start = 0
        curSubset = []
        
        nums = sorted(nums) # sort nums first to help check if statements when backtracking
        
        self.subsetCore(nums, res, curSubset, start)
        return res
    
    def subsetCore(self, nums, res, curSubset, start):
        res.append(curSubset[:])
        
        for i in range(start, len(nums)):
            if i == start or nums[i] != nums[i-1]: # if 1) i == start (i is the first) 2) since the array is sorted, you can check for duplicates
                curSubset.append(nums[i])
                self.subsetCore(nums, res, curSubset, i + 1)
                curSubset.pop()