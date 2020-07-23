class Solution1(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        if len(nums) == 0:
            return result
        
        curPermute = [] # small box inside of the big box "result"
        self.permuteCore(nums, curPermute, result)
        
        return result
        
    def permuteCore(self, nums, curPermute, result):
        if len(nums) == len(curPermute):
            result.append(curPermute[:])
            return
            
        for i in range(0, len(nums)):
            if nums[i] in curPermute:
                continue
                
            curPermute.append(nums[i])
            self.permuteCore(nums, curPermute, result)
            curPermute.pop()