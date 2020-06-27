# Array
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        leftProduct = 1
        rightProduct = 1      
        
        for i in range(0, len(nums)):
            res[i] *= leftProduct
            leftProduct *= nums[i]
            
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= rightProduct
            rightProduct *= nums[i]
            
        return res