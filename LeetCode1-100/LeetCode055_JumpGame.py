# Dynamic Probraming - does not pass time limit because O(n ** 2)
class Solution1(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return True
        
        dp = [False] * len(nums)
        dp[0] = True
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if dp[j] and nums[j] >= i - j: # if 1) the starting jump is valid 2) the distance you will jump can reach the distance between j and i
                    dp[i] = True
                    break
                    
        return dp[-1]

# Greedy
class Solution2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """  
        maxPos = nums[0]
        
        for i in range(0, len(nums)):
            if maxPos < i: # cannot jump to destination
                return False
            maxPos = max(maxPos, nums[i] + i) # max(current max position, how far you can jump + the extra distance you start off with)
            
        return True