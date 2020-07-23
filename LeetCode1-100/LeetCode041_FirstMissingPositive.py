# Array
# Time complecity does not satisfy requirement: O(n ** 2), since every time you check if curNum is in nums is another O(n)
# Well, you may be thinking about using a set for nums. Unfortunately, that doesn't satisfy the constant extra space requirement
class Solution1(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curNum = 1
        
        while curNum in nums:
            curNum += 1
                   
        return curNum

# Array
class Solution2(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums)):
            while nums[i] > 0 and nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]: # if 1) nums[i] is positive 2) since if nums[i] - 1 > len(nums), then there is definetly another number in between 3) Important: nums[i] is in the right position
                # note: this is actually not O(n ** 2) because this inner while loop will loop through very few times.
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] # switch to correct position

        for i in range(0, len(nums)):
            if nums[i] != i + 1: # if it nums[i] does not correspond to its correct value
                return i + 1
            
        return len(nums) + 1