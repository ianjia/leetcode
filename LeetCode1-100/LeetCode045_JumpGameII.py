# Dynamic Probraming - does not pass time limit because O(n ** 2)
import sys

class Solution1(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        
        dp = [sys.maxsize] * len(nums)
        dp[0] = 0
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if dp[j] != sys.maxsize and nums[j] >= i - j:
                    dp[i] = dp[j] + 1
                    break
                    
        return dp[len(dp) - 1]

# Greedy
class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
    
        # max pos one could reach
        maxPos = nums[0]
        # max number of steps one could take
        maxJumps = nums[0]
        res = 1
        
        for i in range(0, len(nums)):
            if maxJumps < i: # if the max number of jumps one can take cannot reach position
                res += 1
                maxJumps = maxPos
            maxPos = max(maxPos, nums[i] + i) # max(current max position, how far you can jump + the extra distance you start off with)
                
        return res