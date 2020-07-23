# Brute Force - Time limit exceeded
class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMax = max(nums)
        
        for i in range(0, len(nums)):
            curTotal = nums[i]
            for j in range(i+1, len(nums)):
                curTotal += nums[j]
                if curTotal > curMax:
                    curMax = curTotal
                    
        return curMax

# Prefix sum
import sys

class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        prefixSum = 0
        maxSum = -sys.maxsize
        prefixSumMin = 0
        
        for i in range(0, len(nums)):
            prefixSum += nums[i]
            maxSum = max(maxSum, prefixSum - prefixSumMin)
            prefixSumMin = min(prefixSumMin, prefixSum)

        return maxSum
# Greedy
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)
            
        return maxSum