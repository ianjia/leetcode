# Two-pointers
class Solution1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        
        for i in range(0, len(nums)):
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i-1] != nums[i]:
                twoSumRes = self.twoSum(nums, -nums[i], i+1) # a + b = -c
                for elem in twoSumRes:
                    elem.insert(0, nums[i])
                    res.append(elem)
                 
        return res
        
    def twoSum(self, nums, target, start):
        result = []
        left, right = start, len(nums) - 1
        
        while left < right:
            if left != start and nums[left] == nums[left-1]:
                left += 1
                continue
        
            if (nums[left] + nums[right] == target):
                result.append([nums[left], nums[right]])
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -=1
      
        return result