# Backtracking
class Solution1(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        if len(nums) == 0:
            return res
        
        curSubset = []
        start = 0
        
        self.subsetCore(nums, curSubset, res, start)
        return res
    
    def subsetCore(self, nums, curSubset, res, start):
        res.append(curSubset[:]) # no length requirements because curSubset may be any length
        
        for i in range(start, len(nums)):
            curSubset.append(nums[i])
            self.subsetCore(nums, curSubset, res, i + 1)
            curSubset.pop()