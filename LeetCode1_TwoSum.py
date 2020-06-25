# Brute Force
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Dictionary
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        pos = 0
        while pos < len(nums):
            if (target - nums[pos]) not in dictionary:
            #checks if the counterpart of nums[pos] is in dictionary
            #for example, when 18/target - 7/nums[pos], the counterpart of nums[pos]/7 is 11 because 18 - 7 = 11
                dictionary[nums[pos]] = pos
                pos += 1
            else:
                return [dictionary[target - nums[pos]], pos]